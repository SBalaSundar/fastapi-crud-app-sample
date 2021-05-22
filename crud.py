from typing import List
from sqlalchemy.orm import Session
from exceptions import CarInfoInfoAlreadyExistError, CarInfoNotFoundError
from models import CarInfo
from schemas import CreateCar, UpdateCar


# Function to get list of car info
def get_all_cars(session: Session, limit: int, offset: int) -> List[CarInfo]:
    return session.query(CarInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_car_info_by_id(session: Session, _id: int) -> CarInfo:
    car_info = session.query(CarInfo).get(_id)

    if car_info is None:
        raise CarInfoNotFoundError

    return car_info


# Function to add a new car info to the database
def create_car(session: Session, car_info: CreateCar) -> CarInfo:
    car_details = session.query(CarInfo).filter(CarInfo.manufacturer == car_info.manufacturer, CarInfo.modelName == car_info.modelName).first()
    if car_details is not None:
        raise CarInfoInfoAlreadyExistError

    new_car_info = CarInfo(**car_info.dict())
    session.add(new_car_info)
    session.commit()
    return new_car_info


# Function to update details of the car
def update_car_info(session: Session, _id: int, info_update: UpdateCar) -> CarInfo:
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    if info_update.manufacturer is not None:
        car_info.manufacturer = info_update.manufacturer

    if info_update.modelName is not None:
        car_info.modelName = info_update.modelName

    if info_update.fuelType is not None:
        car_info.fuelType = info_update.fuelType

    if info_update.cc is not None:
        car_info.cc = info_update.cc

    if info_update.gearBox is not None:
        car_info.gearBox = info_update.gearBox

    if info_update.onRoadPrice is not None:
        car_info.onRoadPrice = info_update.onRoadPrice

    if info_update.seatingCapacity is not None:
        car_info.seatingCapacity = info_update.seatingCapacity

    session.commit()

    return car_info


# Function to delete a car info from the db
def delete_car_info(session: Session, _id: int):
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    session.delete(car_info)
    session.commit()

    return
