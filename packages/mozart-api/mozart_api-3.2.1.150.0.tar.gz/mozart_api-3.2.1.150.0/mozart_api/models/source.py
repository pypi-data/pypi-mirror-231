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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from mozart_api.models.source_type_enum import SourceTypeEnum


class Source(BaseModel):
    """
    Source
    """

    id: Optional[StrictStr] = None
    is_enabled: Optional[StrictBool] = Field(
        None,
        alias="isEnabled",
        description="some sources require an explicit activation or accept of terms before being enabled",
    )
    is_playable: Optional[StrictBool] = Field(None, alias="isPlayable")
    name: Optional[StrictStr] = None
    type: Optional[SourceTypeEnum] = None
    __properties = ["id", "isEnabled", "isPlayable", "name", "type"]

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
    def from_json(cls, json_str: str) -> Source:
        """Create an instance of Source from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict["type"] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Source:
        """Create an instance of Source from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Source.parse_obj(obj)

        _obj = Source.parse_obj(
            {
                "id": obj.get("id"),
                "is_enabled": obj.get("isEnabled"),
                "is_playable": obj.get("isPlayable"),
                "name": obj.get("name"),
                "type": SourceTypeEnum.from_dict(obj.get("type"))
                if obj.get("type") is not None
                else None,
            }
        )
        return _obj
