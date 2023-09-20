# -*- encoding:utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import math

import tensorflow as tf

from easy_rec.python.utils.activation import get_activation

if tf.__version__ >= '2.0':
  tf = tf.compat.v1


class NLinear(object):
  """N linear layers for N token (feature) embeddings.

  To understand this module, let's revise `tf.layers.dense`. When `tf.layers.dense` is
  applied to three-dimensional inputs of the shape
  ``(batch_size, n_tokens, d_embedding)``, then the same linear transformation is
  applied to each of ``n_tokens`` token (feature) embeddings.

  By contrast, `NLinear` allocates one linear layer per token (``n_tokens`` layers in total).
  One such layer can be represented as ``tf.layers.dense(d_in, d_out)``.
  So, the i-th linear transformation is applied to the i-th token embedding, as
  illustrated in the following pseudocode::

      layers = [tf.layers.dense(d_in, d_out) for _ in range(n_tokens)]
      x = tf.random.normal(batch_size, n_tokens, d_in)
      result = tf.stack([layers[i](x[:, i]) for i in range(n_tokens)], 1)

  Examples:
      .. testcode::

          batch_size = 2
          n_features = 3
          d_embedding_in = 4
          d_embedding_out = 5
          x = tf.random.normal(batch_size, n_features, d_embedding_in)
          m = NLinear(n_features, d_embedding_in, d_embedding_out)
          assert m(x).shape == (batch_size, n_features, d_embedding_out)
  """

  def __init__(self, n_tokens, d_in, d_out, bias=True, scope='nd_linear'):
    """Init with input shapes.

    Args:
        n_tokens: the number of tokens (features)
        d_in: the input dimension
        d_out: the output dimension
        bias: indicates if the underlying linear layers have biases
        scope: variable scope name
    """
    with tf.variable_scope(scope):
      self.weight = tf.get_variable(
          'weights', [1, n_tokens, d_in, d_out], dtype=tf.float32)
      if bias:
        initializer = tf.constant_initializer(0.0)
        self.bias = tf.get_variable(
            'bias', [1, n_tokens, d_out],
            dtype=tf.float32,
            initializer=initializer)
      else:
        self.bias = None

  def __call__(self, x, *args, **kwargs):
    if x.shape.ndims != 3:
      raise ValueError(
          'The input must have three dimensions (batch_size, n_tokens, d_embedding)'
      )
    if x.shape[2] != self.weight.shape[2]:
      raise ValueError('invalid input embedding dimension %d, expect %d' %
                       (int(x.shape[2]), int(self.weight.shape[2])))

    x = x[..., None] * self.weight  # [B, N, D, D_out]
    x = tf.reduce_sum(x, axis=-2)  # [B, N, D_out]
    if self.bias is not None:
      x = x + self.bias
    return x


class PeriodicEmbedding(tf.keras.layers.Layer):
  """Periodic embeddings for numerical features described in [1].

  References:
    * [1] Yury Gorishniy, Ivan Rubachev, Artem Babenko,
    "On Embeddings for Numerical Features in Tabular Deep Learning", 2022
    https://arxiv.org/pdf/2203.05556.pdf

  Attributes:
    embedding_dim: the embedding size, must be an even positive integer.
    sigma: the scale of the weight initialization.
      **This is a super important parameter which significantly affects performance**.
      Its optimal value can be dramatically different for different datasets, so
      no "default value" can exist for this parameter, and it must be tuned for
      each dataset. In the original paper, during hyperparameter tuning, this
      parameter was sampled from the distribution ``LogUniform[1e-2, 1e2]``.
      A similar grid would be ``[1e-2, 1e-1, 1e0, 1e1, 1e2]``.
      If possible, add more intermediate values to this grid.
    output_3d_tensor: whether to output a 3d tensor
    output_tensor_list: whether to output the list of embedding
  """

  def __init__(self, params, name='periodic_embedding', **kwargs):
    super(PeriodicEmbedding, self).__init__(name, **kwargs)
    params.check_required(['embedding_dim', 'sigma'])
    self.embedding_dim = int(params.embedding_dim)
    if self.embedding_dim % 2:
      raise ValueError('embedding_dim must be even')
    sigma = params.sigma
    self.initializer = tf.random_normal_initializer(stddev=sigma)
    self.add_linear_layer = params.get_or_default('add_linear_layer', True)
    self.linear_activation = params.get_or_default('linear_activation', 'relu')
    self.output_tensor_list = params.get_or_default('output_tensor_list', False)
    self.output_3d_tensor = params.get_or_default('output_3d_tensor', False)

  def call(self, inputs, **kwargs):
    if inputs.shape.ndims != 2:
      raise ValueError('inputs of PeriodicEmbedding must have 2 dimensions.')

    num_features = int(inputs.shape[-1])
    emb_dim = self.embedding_dim // 2
    with tf.variable_scope(self.name):
      c = tf.get_variable(
          'coefficients',
          shape=[1, num_features, emb_dim],
          initializer=self.initializer)

      features = inputs[..., None]  # [B, N, 1]
      v = 2 * math.pi * c * features  # [B, N, E]
      emb = tf.concat([tf.sin(v), tf.cos(v)], axis=-1)  # [B, N, 2E]

      dim = self.embedding_dim
      if self.add_linear_layer:
        linear = NLinear(num_features, dim, dim)
        emb = linear(emb)
        act = get_activation(self.linear_activation)
        if callable(act):
          emb = act(emb)
      output = tf.reshape(emb, [-1, num_features * dim])

      if self.output_tensor_list:
        return output, tf.unstack(emb, axis=1)
      if self.output_3d_tensor:
        return output, emb
      return output


class AutoDisEmbedding(tf.keras.layers.Layer):
  """An Embedding Learning Framework for Numerical Features in CTR Prediction.

  Refer: https://arxiv.org/pdf/2012.08986v2.pdf
  """

  def __init__(self, params, name='auto_dis_embedding', **kwargs):
    super(AutoDisEmbedding, self).__init__(name, **kwargs)
    params.check_required(['embedding_dim', 'num_bins', 'temperature'])
    self.emb_dim = int(params.embedding_dim)
    self.num_bins = int(params.num_bins)
    self.temperature = params.temperature
    self.keep_prob = params.get_or_default('keep_prob', 0.8)
    self.output_tensor_list = params.get_or_default('output_tensor_list', False)
    self.output_3d_tensor = params.get_or_default('output_3d_tensor', False)

  def call(self, inputs, **kwargs):
    if inputs.shape.ndims != 2:
      raise ValueError('inputs of AutoDisEmbedding must have 2 dimensions.')

    num_features = int(inputs.shape[-1])
    with tf.variable_scope(self.name):
      meta_emb = tf.get_variable(
          'meta_embedding', shape=[num_features, self.num_bins, self.emb_dim])
      w = tf.get_variable('project_w', shape=[1, num_features, self.num_bins])
      mat = tf.get_variable(
          'project_mat', shape=[num_features, self.num_bins, self.num_bins])

      x = tf.expand_dims(inputs, axis=-1)  # [B, N, 1]
      hidden = tf.nn.leaky_relu(w * x)  # [B, N, num_bin]
      # 低版本的tf(1.12) matmul 不支持广播，所以改成 einsum
      # y = tf.matmul(mat, hidden[..., None])  # [B, N, num_bin, 1]
      # y = tf.squeeze(y, axis=3)  # [B, N, num_bin]
      y = tf.einsum('nik,bnk->bni', mat, hidden)  # [B, N, num_bin]

      # keep_prob(float): if dropout_flag is True, keep_prob rate to keep connect
      alpha = self.keep_prob
      x_bar = y + alpha * hidden  # [B, N, num_bin]
      x_hat = tf.nn.softmax(x_bar / self.temperature)  # [B, N, num_bin]

      # emb = tf.matmul(x_hat[:, :, None, :], meta_emb)  # [B, N, 1, D]
      # emb = tf.squeeze(emb, axis=2)  # [B, N, D]
      emb = tf.einsum('bnk,nkd->bnd', x_hat, meta_emb)

      output = tf.reshape(emb, [-1, self.emb_dim * num_features])  # [B, N*D]

      if self.output_tensor_list:
        return output, tf.unstack(emb, axis=1)

      if self.output_3d_tensor:
        return output, emb
      return output
