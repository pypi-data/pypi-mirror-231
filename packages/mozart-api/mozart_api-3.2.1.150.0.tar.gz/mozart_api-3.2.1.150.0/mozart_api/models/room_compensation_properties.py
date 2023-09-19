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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, validator
from mozart_api.models.latency_profile import LatencyProfile


class RoomCompensationProperties(BaseModel):
    """
    RoomCompensationProperties
    """

    value: Optional[StrictStr] = Field(
        None,
        description="The type of roomcompensation used / to use. simple:   For speakers without external speakers. advanced:   For products with external speakers or other advanced multichannel capabilities.   This requires that at least action in the other properties of RoomCompensationProperties is set. ",
    )
    action: Optional[StrictStr] = Field(
        None,
        description="Must be set if room compensation type is advanced. runAll:   Do measurements on all connected speakers. continue:   Continue from and including the speaker where last interrupted (stopped or failed). useSpeakerList:   Do measurements on the speakers in the list property. ",
    )
    continue_on_error: Optional[StrictBool] = Field(
        None,
        alias="continueOnError",
        description="On failing measurement on a speaker, default behavior is to stop measurement and skip the remaining speakers. Setting continueOnError to true will make the measurement process continue and finish measurement on all speakers, even though an error ocurred on one of the speakers. ",
    )
    latency_profile: Optional[LatencyProfile] = Field(None, alias="latencyProfile")
    skip_automatic_role_assignment: Optional[StrictBool] = Field(
        None,
        alias="skipAutomaticRoleAssignment",
        description="Skip calculation of automatic role assignment.",
    )
    speaker_list: Optional[conlist(StrictStr)] = Field(
        None,
        alias="speakerList",
        description="List of speaker IDs to include in room compensation / automatic role assignment measurement. Relevant e.g. if you want to create a speaker group without the external speakers included. This can not be used for doing measurements on a partial speaker group, only on all speakers in an existing group or for all speakers in a new group. ",
    )
    speaker_preset: Optional[conint(strict=True, le=255, ge=0)] = Field(
        None,
        alias="speakerPreset",
        description="The Powerlink preset to use for the external PL/WPL speakers.",
    )
    __properties = [
        "value",
        "action",
        "continueOnError",
        "latencyProfile",
        "skipAutomaticRoleAssignment",
        "speakerList",
        "speakerPreset",
    ]

    @validator("value")
    def value_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("simple", "advanced"):
            raise ValueError("must be one of enum values ('simple', 'advanced')")
        return value

    @validator("action")
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("runAll", "continue", "useSpeakerList"):
            raise ValueError(
                "must be one of enum values ('runAll', 'continue', 'useSpeakerList')"
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
    def from_json(cls, json_str: str) -> RoomCompensationProperties:
        """Create an instance of RoomCompensationProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of latency_profile
        if self.latency_profile:
            _dict["latencyProfile"] = self.latency_profile.to_dict()
        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict["action"] = None

        # set to None if continue_on_error (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.continue_on_error is None
            and "continue_on_error" in self.__fields_set__
        ):
            _dict["continueOnError"] = None

        # set to None if skip_automatic_role_assignment (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.skip_automatic_role_assignment is None
            and "skip_automatic_role_assignment" in self.__fields_set__
        ):
            _dict["skipAutomaticRoleAssignment"] = None

        # set to None if speaker_list (nullable) is None
        # and __fields_set__ contains the field
        if self.speaker_list is None and "speaker_list" in self.__fields_set__:
            _dict["speakerList"] = None

        # set to None if speaker_preset (nullable) is None
        # and __fields_set__ contains the field
        if self.speaker_preset is None and "speaker_preset" in self.__fields_set__:
            _dict["speakerPreset"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomCompensationProperties:
        """Create an instance of RoomCompensationProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomCompensationProperties.parse_obj(obj)

        _obj = RoomCompensationProperties.parse_obj(
            {
                "value": obj.get("value"),
                "action": obj.get("action"),
                "continue_on_error": obj.get("continueOnError"),
                "latency_profile": LatencyProfile.from_dict(obj.get("latencyProfile"))
                if obj.get("latencyProfile") is not None
                else None,
                "skip_automatic_role_assignment": obj.get(
                    "skipAutomaticRoleAssignment"
                ),
                "speaker_list": obj.get("speakerList"),
                "speaker_preset": obj.get("speakerPreset"),
            }
        )
        return _obj
