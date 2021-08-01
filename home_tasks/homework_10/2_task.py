
from typing import Union


class Employee:
    def __init__(self,
                 first_name: str,
                 second_name: str,
                 age: int,
                 registration: str,
                 gender: bool,
                 country: str,
                 city: str,
                 company: str,
                 position: str,
                 salary: int
                 ) -> Union[str, int, bool]:
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age
        self.__registration = registration
        self.__gender = gender
        self.__country = country
        self.__city = city
        self.__company = company
        self.__position = position
        self.__salary = salary

    @property
    def get_first_name(self):
        """
            get private object attribute -  first name
        """
        return self.__first_name

    @property
    def get_second_name(self):
        """
            get private object attribute - second name
        """
        return self.__second_name

    @property
    def get_age(self):
        """
            get private object attribute - age
        """
        return self.__age

    @property
    def get_registration(self):
        """
            get private object attribute - registration
        """
        return self.__registration

    @property
    def get_gender(self):
        """
            get private object attribute - gender (True = man, False - woman)
        """
        return self.__gender

    @property
    def get_country(self):
        """
            get private object attribute - country
        """
        return self.__country

    @property
    def get_city(self):
        """
            get private object attribute - city
        """
        return self.__city

    @property
    def get_company(self):
        """
            get private object attribute - company
        """
        return self.__company

    @property
    def get_position(self):
        """
            get private object attribute - position
        """
        return self.__position

    @property
    def get_salary(self):
        """
            get private object attribute - salary
        """
        return self.__salary


if __name__ == '__main__':
    employee_john = Employee(
        'John',
        'Dow',
         27,
        'Igoria Shamo boulevard 18',
        True,
        'Ukraine',
        'Kiev',
        'EVO',
        'product manager',
        1000
    )
