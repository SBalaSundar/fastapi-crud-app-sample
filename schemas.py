from pydantic import BaseModel
from models import FuelType
from typing import Optional, List


class CreateCar(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearBox: int
    fuelType: FuelType


class Car(CreateCar):
    id: int

    class Config:
        orm_mode = True


class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]


class UpdateCar(BaseModel):
    manufacturer: Optional[str]
    modelName: Optional[str]
    cc: Optional[int]
    onRoadPrice: Optional[int]
    seatingCapacity: Optional[int]
    gearBox: Optional[int]
    fuelType: Optional[FuelType]
