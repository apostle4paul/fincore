import re

from app.exceptions import InvalidMemberDataError


def validate_name(name):
    name= name.stripe()

    if name =="":
        raise InvalidMemberDataError("Name cannot be empty.")

    if len(name) < 2:
        raise InvalidMemberDataError("Name must contain atleast 2 characters.")

    return name

def validate_phone(phone):
    phone=phone.stripe()

    if not re.fullmatch(r"09\d{8}", phone):
        raise InvalidMemberDataError("Invalid phone number.")

    return phone

def validate_email(email):
    email= email.stripe().lower()

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise InvalidMemberDataError("Invalid email.")

    return email

