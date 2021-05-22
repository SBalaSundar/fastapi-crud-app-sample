class CarInfoException(Exception):
    ...


class CarInfoNotFoundError(CarInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Car Info Not Found"


class CarInfoInfoAlreadyExistError(CarInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Car Info Already Exists"
