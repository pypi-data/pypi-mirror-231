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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from mozart_api.models.source_type_enum import SourceTypeEnum


class ContentItem(BaseModel):
    """
    ContentItem
    """

    categories: Optional[conlist(StrictStr)] = None
    content_uri: StrictStr = Field(..., alias="contentUri")
    label: Optional[StrictStr] = None
    source: SourceTypeEnum = Field(...)
    __properties = ["categories", "contentUri", "label", "source"]

    @validator("categories")
    def categories_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ("music", "movie", "tv", "hdmi", "app"):
                raise ValueError(
                    "each list item must be one of ('music', 'movie', 'tv', 'hdmi', 'app')"
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
    def from_json(cls, json_str: str) -> ContentItem:
        """Create an instance of ContentItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict["source"] = self.source.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict["label"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContentItem:
        """Create an instance of ContentItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContentItem.parse_obj(obj)

        _obj = ContentItem.parse_obj(
            {
                "categories": obj.get("categories"),
                "content_uri": obj.get("contentUri"),
                "label": obj.get("label"),
                "source": SourceTypeEnum.from_dict(obj.get("source"))
                if obj.get("source") is not None
                else None,
            }
        )
        return _obj
