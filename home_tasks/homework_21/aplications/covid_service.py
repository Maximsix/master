

from requests import get, post, Response
from .covid_app import covid


class CovidService:
    def __init__(self):
        self.__covid_api = f"{covid['covid_url']}"

    def get_summary_info(self):
        return get(f'{self.__covid_api}/summary')

    def get_country_status(self, country: str) -> Response:
        return get(f'{self.__covid_api}/country/{country}')


    def get_country_status(self, country: str) -> Response:
        return get(f'{self.__covid_api}/country/{country}')

    def get_city_status(self, country: str) -> Response:
        return get(f'{self.__covid_api}/live/country/{country}/status/confirmed')

