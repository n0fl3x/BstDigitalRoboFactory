"""Схема валидации JSON-объекта и его полей."""


robot_validate_schema = {

    "title": "Robot",
    "description": "Robot(-s) info sent via JSON.",
    "type": "object",

    "properties": {

        "model": {
            "description": "2-symbols length string.",
            "type": "string",
            "minLength": 0,
            "maxLength": 2,
        },

        "version": {
            "description": "2-symbols length string.",
            "type": "string",
            "minLength": 0,
            "maxLength": 2,
        },

        "created": {
            "description": "Date and time of creation in '%Y-%m-%d %H:%M:%S' format.",
            "type": "string",
        },
    },

    "required": [
        "model",
        "version",
        "created",
    ],
}
