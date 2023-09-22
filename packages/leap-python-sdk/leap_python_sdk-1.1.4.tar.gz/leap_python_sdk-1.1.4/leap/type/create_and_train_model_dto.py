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

from leap.type.create_and_train_model_dto_image_sample_files import CreateAndTrainModelDtoImageSampleFiles
from leap.type.create_and_train_model_dto_image_sample_urls import CreateAndTrainModelDtoImageSampleUrls

class RequiredCreateAndTrainModelDto(TypedDict):
    pass

class OptionalCreateAndTrainModelDto(TypedDict, total=False):
    # Provide a name so you can more easily identify the model.
    name: str

    # This is the keyword you will use during image generation to trigger your custom subject. For example \"a photo of @me\".
    subjectKeyword: str

    # The subject type - a short description, usually a noun, that describes what the underlying model is learning. For example: person, man, woman, cat, dog, icon, style. Defaults to \"person\".
    subjectType: str

    # An optional webhook URL that will be called with a POST request when the model completes training or fails.
    webhookUrl: str

    imageSampleUrls: CreateAndTrainModelDtoImageSampleUrls

    imageSampleFiles: CreateAndTrainModelDtoImageSampleFiles

class CreateAndTrainModelDto(RequiredCreateAndTrainModelDto, OptionalCreateAndTrainModelDto):
    pass
