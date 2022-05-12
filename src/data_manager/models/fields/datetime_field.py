import datetime

from .abstract_field import AbstractField, Constants

__all__ = [
    "DatetimeField",
]


class DatetimeField(AbstractField):
    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None, align=Constants.ALIGN_DEFAULT,
                 d_format='%Y-%m-%dT%H%M%S') -> None:
        super().__init__(name, strip, default_value, length, start_position, align)
        self.__format = d_format

    def to_string(self, data):
        return data.strftime(self.__format) if data else ''

    def convert(self, data):
        try:
            return datetime.datetime.strptime(data, self.__format) if data else None
        except ValueError:
            return self.get_default_value()
