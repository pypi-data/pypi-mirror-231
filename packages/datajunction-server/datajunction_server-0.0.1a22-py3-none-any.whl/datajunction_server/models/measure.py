"""
Models for measures.
"""
import enum
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.sql.schema import Column as SqlaColumn
from sqlalchemy.types import Enum
from sqlmodel import Field, Relationship

from datajunction_server.models.base import BaseSQLModel

if TYPE_CHECKING:
    from datajunction_server.models import Column


class AggregationRule(str, enum.Enum):
    """
    Type of allowed aggregation for a given measure.
    """

    ADDITIVE = "additive"
    NON_ADDITIVE = "non-additive"
    SEMI_ADDITIVE = "semi-additive"


class Measure(BaseSQLModel, table=True):  # type: ignore
    """
    Measure class.

    Measure is a basic data modelling concept that helps with making Metric nodes portable,
    that is, so they can be computed on various DJ nodes using the same Metric definitions.

    By default, if a node column is not a Dimension or Dimension attribute then it should
    be a Measure.
    """

    __tablename__ = "measures"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    columns: List["Column"] = Relationship(back_populates="measure")
    additive: AggregationRule = Field(
        default=AggregationRule.NON_ADDITIVE,
        sa_column=SqlaColumn(Enum(AggregationRule)),
    )
