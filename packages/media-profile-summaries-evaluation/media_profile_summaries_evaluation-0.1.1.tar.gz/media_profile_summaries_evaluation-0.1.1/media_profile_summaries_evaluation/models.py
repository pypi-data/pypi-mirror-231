"""Helper pydantic models"""
from typing import Optional
from pydantic import BaseModel


class Person(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat person entity"""

    text: str
    value: str


class Organisation(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat organisation entity"""

    text: str
    value: str


class Region(BaseModel, extra="allow", from_attributes=True):
    """Representation of region of Bowler Hat location entity"""

    name: str
    country: str


class Location(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat location entity"""

    value: str
    regions: Optional[list[Region]] = None


class Monetary(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat monetary_value entity"""

    value: float
    currency: str


class Datetime(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat datetime entity"""

    value: str


class Entities(BaseModel, extra="allow", from_attributes=True):
    """Common Bowler Hat entity type container"""

    person: Optional[list[Person]] = None
    organisation: Optional[list[Organisation]] = None
    location: Optional[list[Location]] = None
    datetime: Optional[list[Datetime]] = None
    monetary_value: Optional[list[Monetary]] = None


class BowlerHat(BaseModel, extra="allow", from_attributes=True):
    """Representation of Bowler Hat result"""

    id: Optional[int] = None
    document_language: Optional[dict[str, int]] = None
    entities: Optional[Entities] = None
    references: Optional[list[int]] = None
