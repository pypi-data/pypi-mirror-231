# coding: utf-8

"""
    iparapheur

    iparapheur v5.x main core application.  The main link between every sub-services, integrating business code logic.   # noqa: E501

    The version of the OpenAPI document: DEVELOP
    Contact: iparapheur@libriciel.coop
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iparapheur_provisioning import schemas  # noqa: F401


class MetadataType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "TEXT": "TEXT",
            "DATE": "DATE",
            "INTEGER": "INTEGER",
            "FLOAT": "FLOAT",
            "BOOLEAN": "BOOLEAN",
            "URL": "URL",
        }
    
    @schemas.classproperty
    def TEXT(cls):
        return cls("TEXT")
    
    @schemas.classproperty
    def DATE(cls):
        return cls("DATE")
    
    @schemas.classproperty
    def INTEGER(cls):
        return cls("INTEGER")
    
    @schemas.classproperty
    def FLOAT(cls):
        return cls("FLOAT")
    
    @schemas.classproperty
    def BOOLEAN(cls):
        return cls("BOOLEAN")
    
    @schemas.classproperty
    def URL(cls):
        return cls("URL")
