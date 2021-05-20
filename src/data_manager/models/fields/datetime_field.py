import datetime

from data_manager.models.fields.abstract_field import AbstractField

__all__ = [
    "DatetimeField",
]


class DatetimeField(AbstractField):
    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None,
                 d_format='%Y-%m-%dT%H%M%S') -> None:
        super().__init__(name, strip, default_value, length, start_position)
        self.__format = d_format

    def to_string(self, data):
        return data.strftime(self.__format)

    def convert(self, data):
        return datetime.datetime.strptime(data, self.__format) if data else None
