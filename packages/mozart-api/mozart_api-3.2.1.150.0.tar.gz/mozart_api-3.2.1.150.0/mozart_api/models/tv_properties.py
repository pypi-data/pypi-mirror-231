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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from mozart_api.models.tv_integration_types import TvIntegrationTypes


class TvProperties(BaseModel):
    """
    TvProperties
    """

    integration_supported: Optional[TvIntegrationTypes] = Field(
        None, alias="integrationSupported"
    )
    name: Optional[StrictStr] = None
    year: Optional[StrictInt] = None
    __properties = ["integrationSupported", "name", "year"]

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
    def from_json(cls, json_str: str) -> TvProperties:
        """Create an instance of TvProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of integration_supported
        if self.integration_supported:
            _dict["integrationSupported"] = self.integration_supported.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict["name"] = None

        # set to None if year (nullable) is None
        # and __fields_set__ contains the field
        if self.year is None and "year" in self.__fields_set__:
            _dict["year"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TvProperties:
        """Create an instance of TvProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TvProperties.parse_obj(obj)

        _obj = TvProperties.parse_obj(
            {
                "integration_supported": TvIntegrationTypes.from_dict(
                    obj.get("integrationSupported")
                )
                if obj.get("integrationSupported") is not None
                else None,
                "name": obj.get("name"),
                "year": obj.get("year"),
            }
        )
        return _obj
