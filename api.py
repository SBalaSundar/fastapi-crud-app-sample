from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_cars, create_car, get_car_info_by_id, update_car_info, delete_car_info
from database import get_db
from exceptions import CarInfoException
from schemas import Car, CreateAndUpdateCar, PaginatedCarInfo

router = APIRouter()


# Example of Class based view
@cbv(router)
class Cars:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/cars", response_model=PaginatedCarInfo)
    def list_cars(self, limit: int = 10, offset: int = 0):

        cars_list = get_all_cars(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": cars_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/cars")
    def add_car(self, car_info: CreateAndUpdateCar):

        try:
            car_info = create_car(self.session, car_info)
            return car_info
        except CarInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular car
@router.get("/cars/{car_id}", response_model=Car)
def get_car_info(car_id: int, session: Session = Depends(get_db)):

    try:
        car_info = get_car_info_by_id(session, car_id)
        return car_info
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing car info
@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, new_info: CreateAndUpdateCar, session: Session = Depends(get_db)):

    try:
        car_info = update_car_info(session, car_id, new_info)
        return car_info
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a car info from the data base
@router.delete("/cars/{car_id}")
def delete_car(car_id: int, session: Session = Depends(get_db)):

    try:
        return delete_car_info(session, car_id)
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)