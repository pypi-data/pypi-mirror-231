# -*- encoding:utf-8 -*-
# Copyright (c) Alibaba, Inc. and its affiliates.
import tensorflow as tf

from easy_rec.python.layers.common_layers import layer_norm
from easy_rec.python.layers.keras.blocks import MLP
from easy_rec.python.layers.utils import Parameter

if tf.__version__ >= '2.0':
  tf = tf.compat.v1


class MaskBlock(tf.keras.layers.Layer):
  """MaskBlock use in MaskNet.

  Args:
    projection_dim: project dimension to reduce the computational cost.
    Default is `None` such that a full (`input_dim` by `aggregation_size`) matrix
    W is used. If enabled, a low-rank matrix W = U*V will be used, where U
    is of size `input_dim` by `projection_dim` and V is of size
    `projection_dim` by `aggregation_size`. `projection_dim` need to be smaller
    than `aggregation_size`/2 to improve the model efficiency. In practice, we've
    observed that `projection_dim` = d/4 consistently preserved the
    accuracy of a full-rank version.
  """

  def __init__(self, params, name='mask_block', reuse=None, **kwargs):
    super(MaskBlock, self).__init__(name, **kwargs)
    self.config = params.get_pb_config()
    self.l2_reg = params.l2_regularizer
    self._projection_dim = params.get_or_default('projection_dim', None)
    self.reuse = reuse

  def call(self, inputs, **kwargs):
    net, mask_input = inputs
    mask_input_dim = int(mask_input.shape[-1])
    if self.config.HasField('reduction_factor'):
      aggregation_size = int(mask_input_dim * self.config.reduction_factor)
    elif self.config.HasField('aggregation_size') is not None:
      aggregation_size = self.config.aggregation_size
    else:
      raise ValueError(
          'Need one of reduction factor or aggregation size for MaskBlock.')

    if self.config.input_layer_norm:
      input_name = net.name.replace(':', '_')
      net = layer_norm(net, reuse=tf.AUTO_REUSE, name='ln_' + input_name)

    # initializer = tf.initializers.variance_scaling()
    initializer = tf.glorot_uniform_initializer()

    if self._projection_dim is None:
      mask = tf.layers.dense(
          mask_input,
          aggregation_size,
          activation=tf.nn.relu,
          kernel_initializer=initializer,
          kernel_regularizer=self.l2_reg,
          name='%s/hidden' % self.name,
          reuse=self.reuse)
    else:
      u = tf.layers.dense(
          mask_input,
          self._projection_dim,
          kernel_initializer=initializer,
          kernel_regularizer=self.l2_reg,
          use_bias=False,
          name='%s/prj_u' % self.name,
          reuse=self.reuse)
      mask = tf.layers.dense(
          u,
          aggregation_size,
          activation=tf.nn.relu,
          kernel_initializer=initializer,
          kernel_regularizer=self.l2_reg,
          name='%s/prj_v' % self.name,
          reuse=self.reuse)
    mask = tf.layers.dense(
        mask, net.shape[-1], name='%s/mask' % self.name, reuse=self.reuse)
    masked_net = net * mask

    output_size = self.config.output_size
    hidden = tf.layers.dense(
        masked_net,
        output_size,
        use_bias=False,
        name='%s/output' % self.name,
        reuse=self.reuse)
    ln_hidden = layer_norm(
        hidden, name='%s/ln_output' % self.name, reuse=self.reuse)
    return tf.nn.relu(ln_hidden)


class MaskNet(tf.keras.layers.Layer):
  """MaskNet: Introducing Feature-Wise Multiplication to CTR Ranking Models by Instance-Guided Mask.

  Refer: https://arxiv.org/pdf/2102.07619.pdf
  """

  def __init__(self, params, name='mask_net', **kwargs):
    super(MaskNet, self).__init__(name, **kwargs)
    self.params = params
    self.config = params.get_pb_config()
    if self.config.HasField('mlp'):
      p = Parameter.make_from_pb(self.config.mlp)
      p.l2_regularizer = params.l2_regularizer
      self.mlp = MLP(p, name='%s/mlp' % name)
    else:
      self.mlp = None

  def call(self, inputs, training=None, **kwargs):
    if self.config.use_parallel:
      mask_outputs = []
      for i, block_conf in enumerate(self.config.mask_blocks):
        params = Parameter.make_from_pb(block_conf)
        params.l2_regularizer = self.params.l2_regularizer
        mask_layer = MaskBlock(params, name='%s/block_%d' % (self.name, i))
        mask_outputs.append(mask_layer((inputs, inputs)))
      all_mask_outputs = tf.concat(mask_outputs, axis=1)

      if self.mlp is not None:
        output = self.mlp(all_mask_outputs)
      else:
        output = all_mask_outputs
      return output
    else:
      net = inputs
      for i, block_conf in enumerate(self.config.mask_blocks):
        params = Parameter.make_from_pb(block_conf)
        params.l2_regularizer = self.params.l2_regularizer
        mask_layer = MaskBlock(params, name='%s/block_%d' % (self.name, i))
        net = mask_layer((net, inputs))

      if self.mlp is not None:
        output = self.mlp(net)
      else:
        output = net
      return output
