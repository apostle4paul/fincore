import pytest

from app.exceptions import (
    InvalidMemberDataError
)

from app.utils.validators import (
    validate_email,
    validate_name,
    validate_phone,
)


def test_valid_name():

    assert (
        validate_name("Abebe Kebede")
        == "Abebe Kebede"
    )


def test_empty_name():

    with pytest.raises(
        InvalidMemberDataError
    ):

        validate_name("")


def test_valid_phone():

    assert (
        validate_phone("0912345678")
        == "0912345678"
    )


def test_invalid_phone():

    with pytest.raises(
        InvalidMemberDataError
    ):

        validate_phone("12345")


def test_valid_email():

    assert (
        validate_email("TEST@example.com")
        == "test@example.com"
    )


def test_invalid_email():

    with pytest.raises(
        InvalidMemberDataError
    ):

        validate_email("invalid-email")