# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .detr import build


def build_model(args):
    return build(args)

#
# Definition of build_model() : return build
# We need to go to detr.py
#
