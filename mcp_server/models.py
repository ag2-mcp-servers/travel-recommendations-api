# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:26:39+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, confloat, conint


class Source(BaseModel):
    example: Optional[str] = Field(
        None, description='A sample input to guide the user when resolving this issue'
    )
    parameter: Optional[str] = Field(
        None,
        description='The key of the URI path or query parameter that caused the error',
    )
    pointer: Optional[str] = Field(
        None,
        description='A JSON Pointer [RFC6901] to the associated entity in the request body that caused this error',
    )


class Error(BaseModel):
    code: Optional[int] = Field(
        None,
        description='A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error',
    )
    detail: Optional[str] = Field(
        None,
        description='An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized.',
    )
    source: Optional[Source] = Field(None, title='Error_Source')
    status: Optional[int] = Field(
        None,
        description='The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In the case of multiple errors, they must all have the same status.',
    )
    title: Optional[str] = Field(
        None,
        description='An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized',
    )


class Error400(BaseModel):
    errors: Optional[List[Error]] = None


class Error1(BaseModel):
    code: Optional[int] = Field(
        None,
        description='A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error',
    )
    detail: Optional[str] = Field(
        None,
        description='An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized.',
    )
    source: Optional[Source] = Field(None, title='Error_Source')
    status: Optional[int] = Field(
        None,
        description='The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In the case of multiple errors, they must all have the same status.',
    )
    title: Optional[str] = Field(
        None,
        description='An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized',
    )


class Error500(BaseModel):
    errors: Optional[List[Error1]] = None


class Links(BaseModel):
    self: Optional[str] = Field(None, description='Link to the same page.')


class Meta(BaseModel):
    count: Optional[conint(ge=0)] = Field(
        None, description='Total number of object(s) retrieved'
    )
    links: Optional[Links] = Field(
        None, description='Links related to the returned object(s)', title='Links'
    )


class GeoCode(BaseModel):
    latitude: Optional[confloat(ge=-90.0, le=90.0)] = Field(
        None,
        description='Latitude of the position expressed in decimal degrees (WSG 84), e.g. 6.244203. A positive value denotes northern hemisphere or the equator, and a negative value denotes southern hemisphere. The number of digits to represent the precision of the coordinate.',
        examples=[48.85837],
    )
    longitude: Optional[confloat(ge=-180.0, le=180.0)] = Field(
        None,
        description='Longitude of the position expressed in decimal degrees (WSG 84), e.g. -75.581211. A positive value denotes east longitude or the prime meridian, and a negative value denotes west longitude.  The number of digits to represent the precision of the coordinate.',
        examples=[2.294481],
    )


class RecommendedLocation(BaseModel):
    geoCode: Optional[GeoCode] = Field(
        None,
        description='Geographic coordinates describing the position of any location on the surface of Earth',
        title='GeoCode',
    )
    iataCode: Optional[str] = Field(
        None, description='IATA location code', examples=['PAR']
    )
    name: Optional[str] = Field(
        None,
        description='Label associated to the location (e.g. Eiffel Tower, Madison Square)',
        examples=['Eiffel Tower'],
    )
    subtype: Optional[str] = Field(
        None,
        description='Location sub-type (e.g. airport, port, rail-station, restaurant, atm...)',
    )
    relevance: Optional[float] = Field(
        None,
        description='percentage of similarity.\n\n0 for not similar to 1 for exactly the same',
    )
    type: Optional[str] = Field(None, description='Ressource type')


class Source2(BaseModel):
    example: Optional[str] = Field(
        None, description='A sample input to guide the user when resolving this issu'
    )
    parameter: Optional[str] = Field(
        None,
        description='The key of the URI path or query parameter that caused the error',
    )
    pointer: Optional[str] = Field(
        None,
        description='A JSON Pointer [RFC6901] to the associated entity in the request body that caused this error',
    )


class Warning(BaseModel):
    code: int = Field(
        ...,
        description='A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error',
    )
    detail: Optional[str] = Field(
        None,
        description='An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized.',
    )
    source: Optional[Source2] = Field(
        None, description='The Warning Source Definition', title='Warning_Source'
    )
    title: str = Field(
        ...,
        description='An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized',
    )


class ReferenceDataRecommendedLocationsGetResponse(BaseModel):
    data: Optional[List[RecommendedLocation]] = None
    meta: Optional[Meta] = None
    warnings: Optional[List[Warning]] = None
