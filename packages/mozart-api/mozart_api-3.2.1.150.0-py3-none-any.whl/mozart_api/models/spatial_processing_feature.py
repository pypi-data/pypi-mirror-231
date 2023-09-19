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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from mozart_api.models.spatial_processing import SpatialProcessing


class SpatialProcessingFeature(BaseModel):
    """
    SpatialProcessingFeature
    """

    value: StrictStr = Field(..., description="Selected spatial-processing value")
    default: SpatialProcessing = Field(...)
    range: conlist(SpatialProcessing, unique_items=True) = Field(
        ..., description="spatial-processing range"
    )
    __properties = ["value", "default", "range"]

    @validator("value")
    def value_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("direct", "trueimage", "downmix"):
            raise ValueError(
                "must be one of enum values ('direct', 'trueimage', 'downmix')"
            )
        return value

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
    def from_json(cls, json_str: str) -> SpatialProcessingFeature:
        """Create an instance of SpatialProcessingFeature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict["default"] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in range (list)
        _items = []
        if self.range:
            for _item in self.range:
                if _item:
                    _items.append(_item.to_dict())
            _dict["range"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpatialProcessingFeature:
        """Create an instance of SpatialProcessingFeature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpatialProcessingFeature.parse_obj(obj)

        _obj = SpatialProcessingFeature.parse_obj(
            {
                "value": obj.get("value"),
                "default": SpatialProcessing.from_dict(obj.get("default"))
                if obj.get("default") is not None
                else None,
                "range": [
                    SpatialProcessing.from_dict(_item) for _item in obj.get("range")
                ]
                if obj.get("range") is not None
                else None,
            }
        )
        return _obj
