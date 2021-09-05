
import pytest


@pytest.mark.smoke
def test_grow_method_add_one_year(human):
    """
    this test check grow method that add one year to age attribute
    """
    human.grow()
    assert human.age == 19


@pytest.mark.smoke
def test_grow_method_dead_status(human, monkeypatch):
    """
    this test checked dead status when age limit > 100
    """
    monkeypatch.setattr(
        human, '_Human__age', 100
    )
    human.grow()
    assert human._Human__status == "dead"


def test_exception_in_grow_method(human, monkeypatch):
    """
    This test check got exception in called function (is_alive) when status
    is equal to dead
    """
    monkeypatch.setattr(
        human, '_Human__age', 100
    )
    human.grow()
    with pytest.raises(Exception):
        human.grow()


def test_return_result_method_alive_true(human):
    """
    This test check returned result (True) when status is equal to alive
    """
    assert human._Human__is_alive() is True


def test_exception_in_method_alive(human, monkeypatch):
    """
    This test check got exception when status is equal to dead
    """
    monkeypatch.setattr(
        human, "_Human__age", 100
    )
    human.grow()
    with pytest.raises(Exception):
        human._Human__is_alive()


@pytest.mark.smoke
def test_change_gender(human):
    """
    This test check changing gender on another gender
    """
    human.change_gender('female')
    assert human.gender == 'female'


def test_change_the_same_gender(human):
    """
    This test check changing gender on the same gender
    """
    with pytest.raises(Exception):
        human.change_gender("male")


def test_change_gendern_status_dead(human, monkeypatch):
    """
    This test check called function is_alive in change_gender function
    when status is equal to dead
    """
    monkeypatch.setattr(
        human, "_Human__age", 100
    )
    human.grow()
    with pytest.raises(Exception):
        human.change_gender("female")


def test_invalid_gender_method_change_gender(human):
    """
    This test check changing gender on not correct gender
    """
    with pytest.raises(Exception):
        human.change_gender(" ")


def test_validate_gender(human):
    """
    This test check not correct gender
    """
    with pytest.raises(Exception):
        human._Human__validate_gender("empty")


def test_validate_right_gender(human):
    """
    This test check that if gender is correct function doesn't return anything
    """
    assert human._Human__validate_gender("male") == None


def test_return_gender(human):
    """
    This test check return private attribute gender
    """
    assert human.gender == "male"


def test_return_age(human):
    """
    This test check return private attribute age
    """
    assert human.age == 18

# in tests for change gender no mock but should be
# I see some tests without mocks at all
