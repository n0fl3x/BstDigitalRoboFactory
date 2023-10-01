from datetime import datetime

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from .schemas import robot_validate_schema


def validate_json(json_data: dict) -> bool:
    """Валидатор входящего JSON'а на основании схемы из schemas.py."""

    try:
        validate(
            instance=json_data,
            schema=robot_validate_schema,
        )
    except ValidationError:
        return False
    return True


def validate_datetime_field(datetime_text: str) -> bool:
    """Валидатор формата и корректности datetime поля."""

    try:
        if datetime_text != datetime.strptime(datetime_text, "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d %H:%M:%S')\
                or datetime.strptime(datetime_text, "%Y-%m-%d %H:%M:%S") > datetime.now():
            raise ValueError
        return True
    except ValueError:
        return False
