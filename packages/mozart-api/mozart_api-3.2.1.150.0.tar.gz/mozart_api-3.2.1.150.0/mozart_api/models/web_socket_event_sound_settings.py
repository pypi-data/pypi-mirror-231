# coding: utf-8

"""
    Mozart platform API

    API for interacting with the Mozart platform.

    The version of the OpenAPI document: 0.2.0
    Contact: support@bang-olufsen.dk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from mozart_api.models.sound_settings import SoundSettings


class WebSocketEventSoundSettings(BaseModel):
    """
    WebSocketEventSoundSettings
    """

    event_data: Optional[SoundSettings] = Field(None, alias="eventData")
    event_type: Optional[StrictStr] = Field(None, alias="eventType")
    __properties = ["eventData", "eventType"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WebSocketEventSoundSettings:
        """Create an instance of WebSocketEventSoundSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of event_data
        if self.event_data:
            _dict["eventData"] = self.event_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebSocketEventSoundSettings:
        """Create an instance of WebSocketEventSoundSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebSocketEventSoundSettings.parse_obj(obj)

        _obj = WebSocketEventSoundSettings.parse_obj(
            {
                "event_data": SoundSettings.from_dict(obj.get("eventData"))
                if obj.get("eventData") is not None
                else None,
                "event_type": obj.get("eventType"),
            }
        )
        return _obj
