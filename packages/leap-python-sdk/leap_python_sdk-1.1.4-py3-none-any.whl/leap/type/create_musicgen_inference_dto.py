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


class RequiredCreateMusicgenInferenceDto(TypedDict):
    # A description of the music you want to generate.
    prompt: str

    # Select a mode, each option generates different results. Melody is best for melody, music is best for full songs
    mode: str

    # Duration of the generated audio in seconds. Max 30 seconds.
    duration: typing.Union[int, float]

class OptionalCreateMusicgenInferenceDto(TypedDict, total=False):
    pass

class CreateMusicgenInferenceDto(RequiredCreateMusicgenInferenceDto, OptionalCreateMusicgenInferenceDto):
    pass
