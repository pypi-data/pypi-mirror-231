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


class PageTypeRepresentation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            totalElements = schemas.Int64Schema
            totalPages = schemas.Int32Schema
            size = schemas.Int32Schema
            
            
            class content(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TypeRepresentation']:
                        return TypeRepresentation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TypeRepresentation'], typing.List['TypeRepresentation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'content':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TypeRepresentation':
                    return super().__getitem__(i)
            number = schemas.Int32Schema
        
            @staticmethod
            def sort() -> typing.Type['SortObject']:
                return SortObject
            numberOfElements = schemas.Int32Schema
        
            @staticmethod
            def pageable() -> typing.Type['PageableObject']:
                return PageableObject
            first = schemas.BoolSchema
            last = schemas.BoolSchema
            empty = schemas.BoolSchema
            __annotations__ = {
                "totalElements": totalElements,
                "totalPages": totalPages,
                "size": size,
                "content": content,
                "number": number,
                "sort": sort,
                "numberOfElements": numberOfElements,
                "pageable": pageable,
                "first": first,
                "last": last,
                "empty": empty,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalElements"]) -> MetaOapg.properties.totalElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> 'SortObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfElements"]) -> MetaOapg.properties.numberOfElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageable"]) -> 'PageableObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty"]) -> MetaOapg.properties.empty: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["totalElements", "totalPages", "size", "content", "number", "sort", "numberOfElements", "pageable", "first", "last", "empty", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalElements"]) -> typing.Union[MetaOapg.properties.totalElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> typing.Union[MetaOapg.properties.totalPages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> typing.Union[MetaOapg.properties.content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union['SortObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfElements"]) -> typing.Union[MetaOapg.properties.numberOfElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageable"]) -> typing.Union['PageableObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["empty"]) -> typing.Union[MetaOapg.properties.empty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["totalElements", "totalPages", "size", "content", "number", "sort", "numberOfElements", "pageable", "first", "last", "empty", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        totalElements: typing.Union[MetaOapg.properties.totalElements, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        content: typing.Union[MetaOapg.properties.content, list, tuple, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sort: typing.Union['SortObject', schemas.Unset] = schemas.unset,
        numberOfElements: typing.Union[MetaOapg.properties.numberOfElements, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageable: typing.Union['PageableObject', schemas.Unset] = schemas.unset,
        first: typing.Union[MetaOapg.properties.first, bool, schemas.Unset] = schemas.unset,
        last: typing.Union[MetaOapg.properties.last, bool, schemas.Unset] = schemas.unset,
        empty: typing.Union[MetaOapg.properties.empty, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageTypeRepresentation':
        return super().__new__(
            cls,
            *_args,
            totalElements=totalElements,
            totalPages=totalPages,
            size=size,
            content=content,
            number=number,
            sort=sort,
            numberOfElements=numberOfElements,
            pageable=pageable,
            first=first,
            last=last,
            empty=empty,
            _configuration=_configuration,
            **kwargs,
        )

from iparapheur_provisioning.model.pageable_object import PageableObject
from iparapheur_provisioning.model.sort_object import SortObject
from iparapheur_provisioning.model.type_representation import TypeRepresentation
