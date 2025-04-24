#  ___________________
#  Import LIBRARIESI
from enum import StrEnum
from pydantic import BaseModel
# from enum import Enum
#  Import FILES
#  ___________________


class FoodEnum(StrEnum):
    # class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
