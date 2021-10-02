import pytest

from aplications.covid_service import CovidService


@pytest.fixture(scope="session")
def covid_service() -> CovidService:
    yield CovidService()

