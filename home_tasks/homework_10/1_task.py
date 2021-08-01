
from typing import Union


class Company:
    def __init__(self,
                 company_name: str,
                 ceo: str,
                 address: str,
                 number_of_employees: int,
                 country: str,
                 city: str,
                 company_type: str,
                 foundation_date: int,
                 company_website: str
                 ) -> Union[str, int]: # constractoe should not return anything
        self.__company_name = company_name
        self.__ceo = ceo
        self.__address = address
        self.__number_of_employees = number_of_employees
        self.__country = country
        self.__city = city
        self.__company_type = company_type
        self.__foundation_date = foundation_date
        self.__company_website = company_website

    @property
    def get_company_name(self):
        """
            get private object attribute - company name
        """
        return self.__company_name

    @property
    def get_ceo_name(self):
        """
            get private object attribute - ceo name
        """
        return self.__ceo

    @property
    def get_company_address(self):
        """
            get private object attribute - company address
        """
        return self.__address

    @property
    def get_number_of_employees(self):
        """
            get private object attribute - number of employees
        """
        return self.__number_of_employees

    @property
    def get_company_country(self):
        """
            get private object attribute - company country
        """
        return self.__country

    @property
    def get_company_city(self):
        """
            get private object attribute - company city
        """
        return self.__city

    @property
    def get_company_type(self):
        """
            get private object attribute - company type
        """
        return self.__company_type

    @property
    def get_foundation_date(self):
        """
            get private object attribute - foundation date
        """
        return self.__foundation_date

    @property
    def get_company_website(self):
        """
            get private object attribute - company website
        """
        return self.__company_website


if __name__ == '__main__':
    my_company = Company(
        'EVO',
        'Ivan Portnoy',
        'Kharkivske shose, 201/203, Kyiv, 02000',
        1400,
        'Ukraine',
        'Kiev',
        'product company',
        2008,
        'https://evo.company/'
    )
# Well nice but no logic in this class only properties. I want to see methods with logic for changing state of object.
# -2 points
