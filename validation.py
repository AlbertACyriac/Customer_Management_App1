import re
from datetime import datetime

def validate_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validate_phone(phone):
    return phone.isdigit() and len(phone) in [10, 11]

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_boolean(value):
    return value.lower() in ["true", "false"]

def validate_fields(customer):
    return (
        isinstance(customer["id"], int) and
        validate_email(customer["email"]) and
        validate_phone(customer["phone"]) and
        validate_date(customer["date_joined"]) and
        isinstance(customer["membership_status"], str) and
        validate_float(customer["balance"]) and
        isinstance(customer["is_active"], bool)
    )