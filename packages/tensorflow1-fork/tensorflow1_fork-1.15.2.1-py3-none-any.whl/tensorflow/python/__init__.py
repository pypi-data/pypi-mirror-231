# Copyright 2015 The tensorflow1 Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Import core names of tensorflow1.

Programs that want to build tensorflow1 Ops and Graphs without having to import
the constructors and utilities individually can import this file:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow1 as tf
"""

import ctypes
import importlib
import sys
import traceback

# TODO(drpng): write up instructions for editing this file in a doc and point to
# the doc instead.
# If you want to edit this file to expose modules in public tensorflow1 API, you
# need to follow these steps:
# 1. Consult with tensorflow1 team and get approval for adding a new API to the
#    public interface.
# 2. Document the module in the gen_docs_combined.py.
# 3. Import the module in the main tensorflow1 namespace by adding an import
#    statement in this file.
# 4. Sanitize the entry point by making sure that your module does not expose
#    transitively imported modules used for implementation, such as os, sys.

# go/tf-wildcard-import
# pylint: disable=wildcard-import,g-bad-import-order,g-import-not-at-top

import numpy as np

from tensorflow1.python import pywrap_tensorflow

# Protocol buffers
from tensorflow1.core.framework.graph_pb2 import *
from tensorflow1.core.framework.node_def_pb2 import *
from tensorflow1.core.framework.summary_pb2 import *
from tensorflow1.core.framework.attr_value_pb2 import *
from tensorflow1.core.protobuf.meta_graph_pb2 import TensorInfo
from tensorflow1.core.protobuf.meta_graph_pb2 import MetaGraphDef
from tensorflow1.core.protobuf.config_pb2 import *
from tensorflow1.core.protobuf.tensorflow1_server_pb2 import *
from tensorflow1.core.util.event_pb2 import *

# Framework
from tensorflow1.python.framework.framework_lib import *  # pylint: disable=redefined-builtin
from tensorflow1.python.framework.versions import *
from tensorflow1.python.framework import config
from tensorflow1.python.framework import errors
from tensorflow1.python.framework import graph_util

# Session
from tensorflow1.python.client.client_lib import *

# Ops
from tensorflow1.python.ops.standard_ops import *

# Namespaces
from tensorflow1.python.ops import initializers_ns as initializers

# pylint: enable=wildcard-import

# Bring in subpackages.
from tensorflow1.python import data
from tensorflow1.python import distribute
from tensorflow1.python import keras
from tensorflow1.python.feature_column import feature_column_lib as feature_column
from tensorflow1.python.layers import layers
from tensorflow1.python.module import module
from tensorflow1.python.ops import bitwise_ops as bitwise
from tensorflow1.python.ops import gradient_checker_v2
from tensorflow1.python.ops import image_ops as image
from tensorflow1.python.ops import manip_ops as manip
from tensorflow1.python.ops import metrics
from tensorflow1.python.ops import nn
from tensorflow1.python.ops import ragged
from tensorflow1.python.ops import sets
from tensorflow1.python.ops import stateful_random_ops
from tensorflow1.python.ops.distributions import distributions
from tensorflow1.python.ops.linalg import linalg
from tensorflow1.python.ops.losses import losses
from tensorflow1.python.ops.signal import signal
from tensorflow1.python.profiler import profiler
from tensorflow1.python.saved_model import saved_model
from tensorflow1.python.summary import summary
from tensorflow1.python.tpu import api
from tensorflow1.python.user_ops import user_ops
from tensorflow1.python.util import compat

# Import audio ops to make sure the ops are registered.
from tensorflow1.python.ops import gen_audio_ops as _

# Import boosted trees ops to make sure the ops are registered (but unused).
from tensorflow1.python.ops import gen_boosted_trees_ops as _gen_boosted_trees_ops

# Import cudnn rnn ops to make sure their ops are registered.
from tensorflow1.python.ops import gen_cudnn_rnn_ops as _

# Import rnn_ops to make sure their ops are registered.
from tensorflow1.python.ops import gen_rnn_ops as _

# Import the names from python/training.py as train.Name.
from tensorflow1.python.training import training as train

# Sub-package for performing i/o directly instead of via ops in a graph.
from tensorflow1.python.lib.io import python_io

# Make some application and test modules available.
from tensorflow1.python.platform import app
from tensorflow1.python.platform import flags
from tensorflow1.python.platform import gfile
from tensorflow1.python.platform import tf_logging as logging
from tensorflow1.python.platform import resource_loader
from tensorflow1.python.platform import sysconfig
from tensorflow1.python.platform import test

from tensorflow1.python.compat import v2_compat

from tensorflow1.python.util.all_util import make_all
from tensorflow1.python.util.tf_export import tf_export

# Eager execution
from tensorflow1.python.eager.context import executing_eagerly
from tensorflow1.python.eager.remote import connect_to_remote_host
from tensorflow1.python.eager.def_function import function
from tensorflow1.python.framework.ops import enable_eager_execution

# Check whether TF2_BEHAVIOR is turned on.
from tensorflow1.python.eager import monitoring as _monitoring
from tensorflow1.python import tf2 as _tf2
_tf2_gauge = _monitoring.BoolGauge('/tensorflow1/api/tf2_enable',
                                   'Environment variable TF2_BEHAVIOR is set".')
_tf2_gauge.get_cell().set(_tf2.enabled())

# Necessary for the symbols in this module to be taken into account by
# the namespace management system (API decorators).
from tensorflow1.python.ops import rnn
from tensorflow1.python.ops import rnn_cell

# XLA JIT compiler APIs.
from tensorflow1.python.compiler.xla import jit
from tensorflow1.python.compiler.xla import xla

# Required due to `rnn` and `rnn_cell` not being imported in `nn` directly
# (due to a circular dependency issue: rnn depends on layers).
nn.dynamic_rnn = rnn.dynamic_rnn
nn.static_rnn = rnn.static_rnn
nn.raw_rnn = rnn.raw_rnn
nn.bidirectional_dynamic_rnn = rnn.bidirectional_dynamic_rnn
nn.static_state_saving_rnn = rnn.static_state_saving_rnn
nn.rnn_cell = rnn_cell

# Export protos
# pylint: disable=undefined-variable
tf_export(v1=['AttrValue'])(AttrValue)
tf_export(v1=['ConfigProto'])(ConfigProto)
tf_export(v1=['Event', 'summary.Event'])(Event)
tf_export(v1=['GPUOptions'])(GPUOptions)
tf_export(v1=['GraphDef'])(GraphDef)
tf_export(v1=['GraphOptions'])(GraphOptions)
tf_export(v1=['HistogramProto'])(HistogramProto)
tf_export(v1=['LogMessage'])(LogMessage)
tf_export(v1=['MetaGraphDef'])(MetaGraphDef)
tf_export(v1=['NameAttrList'])(NameAttrList)
tf_export(v1=['NodeDef'])(NodeDef)
tf_export(v1=['OptimizerOptions'])(OptimizerOptions)
tf_export(v1=['RunMetadata'])(RunMetadata)
tf_export(v1=['RunOptions'])(RunOptions)
tf_export(v1=['SessionLog', 'summary.SessionLog'])(SessionLog)
tf_export(v1=['Summary', 'summary.Summary'])(Summary)
tf_export(v1=['summary.SummaryDescription'])(SummaryDescription)
tf_export(v1=['SummaryMetadata'])(SummaryMetadata)
tf_export(v1=['summary.TaggedRunMetadata'])(TaggedRunMetadata)
tf_export(v1=['TensorInfo'])(TensorInfo)
# pylint: enable=undefined-variable

# Special dunders that we choose to export:
_exported_dunders = set([
    '__version__',
    '__git_version__',
    '__compiler_version__',
    '__cxx11_abi_flag__',
    '__monolithic_build__',
])

# Expose symbols minus dunders, unless they are whitelisted above.
# This is necessary to export our dunders.
__all__ = [s for s in dir() if s in _exported_dunders or not s.startswith('_')]
