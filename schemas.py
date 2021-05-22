from pydantic import BaseModel
from models import FuelType
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateCar(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearBox: int
    fuelType: FuelType


# TO support list and get APIs
class Car(CreateAndUpdateCar):
    id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]

