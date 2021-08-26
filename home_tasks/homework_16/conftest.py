
import pytest

from human import Human


@pytest.fixture
def human() -> Human:
    yield Human("john", 18, "male")



