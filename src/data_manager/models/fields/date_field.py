from data_manager.models.fields.abstract_field import Constants
from data_manager.models.fields.datetime_field import DatetimeField

__all__ = [
    "DateField",
]


class DateField(DatetimeField):

    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None, align=Constants.ALIGN_DEFAULT,
                 d_format='%Y-%m-%d') -> None:
        super().__init__(name, strip, default_value, length, start_position, align, d_format)

    def convert(self, data):
        result = super().convert(data)
        return result.date() if result else None
