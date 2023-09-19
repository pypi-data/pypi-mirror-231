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


class TemplateType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "MAIL_NOTIFICATION_SINGLE": "MAIL_NOTIFICATION_SINGLE",
            "MAIL_NOTIFICATION_DIGEST": "MAIL_NOTIFICATION_DIGEST",
            "MAIL_ACTION_SEND": "MAIL_ACTION_SEND",
            "SIGNATURE_SMALL": "SIGNATURE_SMALL",
            "SIGNATURE_MEDIUM": "SIGNATURE_MEDIUM",
            "SIGNATURE_LARGE": "SIGNATURE_LARGE",
            "SIGNATURE_ALTERNATE_1": "SIGNATURE_ALTERNATE_1",
            "SIGNATURE_ALTERNATE_2": "SIGNATURE_ALTERNATE_2",
            "SEAL_SMALL": "SEAL_SMALL",
            "SEAL_MEDIUM": "SEAL_MEDIUM",
            "SEAL_LARGE": "SEAL_LARGE",
            "SEAL_ALTERNATE_1": "SEAL_ALTERNATE_1",
            "SEAL_ALTERNATE_2": "SEAL_ALTERNATE_2",
            "DOCKET": "DOCKET",
        }
    
    @schemas.classproperty
    def MAIL_NOTIFICATION_SINGLE(cls):
        return cls("MAIL_NOTIFICATION_SINGLE")
    
    @schemas.classproperty
    def MAIL_NOTIFICATION_DIGEST(cls):
        return cls("MAIL_NOTIFICATION_DIGEST")
    
    @schemas.classproperty
    def MAIL_ACTION_SEND(cls):
        return cls("MAIL_ACTION_SEND")
    
    @schemas.classproperty
    def SIGNATURE_SMALL(cls):
        return cls("SIGNATURE_SMALL")
    
    @schemas.classproperty
    def SIGNATURE_MEDIUM(cls):
        return cls("SIGNATURE_MEDIUM")
    
    @schemas.classproperty
    def SIGNATURE_LARGE(cls):
        return cls("SIGNATURE_LARGE")
    
    @schemas.classproperty
    def SIGNATURE_ALTERNATE_1(cls):
        return cls("SIGNATURE_ALTERNATE_1")
    
    @schemas.classproperty
    def SIGNATURE_ALTERNATE_2(cls):
        return cls("SIGNATURE_ALTERNATE_2")
    
    @schemas.classproperty
    def SEAL_SMALL(cls):
        return cls("SEAL_SMALL")
    
    @schemas.classproperty
    def SEAL_MEDIUM(cls):
        return cls("SEAL_MEDIUM")
    
    @schemas.classproperty
    def SEAL_LARGE(cls):
        return cls("SEAL_LARGE")
    
    @schemas.classproperty
    def SEAL_ALTERNATE_1(cls):
        return cls("SEAL_ALTERNATE_1")
    
    @schemas.classproperty
    def SEAL_ALTERNATE_2(cls):
        return cls("SEAL_ALTERNATE_2")
    
    @schemas.classproperty
    def DOCKET(cls):
        return cls("DOCKET")
