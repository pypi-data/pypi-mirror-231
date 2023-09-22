# coding: utf-8

"""
    Leap

    The Official Leap API

    The version of the OpenAPI document: 1.0
    Created by: https://tryleap.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from leap.type.model_v2_entity_image_samples import ModelV2EntityImageSamples

class RequiredModelV2Entity(TypedDict):
    id: str

    name: str

    createdAt: str

    subjectKeyword: str

    subjectType: str

    status: str

    imageSamples: ModelV2EntityImageSamples

class OptionalModelV2Entity(TypedDict, total=False):
    pass

class ModelV2Entity(RequiredModelV2Entity, OptionalModelV2Entity):
    pass
