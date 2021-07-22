from decimal import Decimal

from data_manager.models.fields.abstract_field import AbstractField

__all__ = [
    "DecimalField",
]


class DecimalField(AbstractField):
    def to_string(self, data):
        return str(data)

    def convert(self, data):
        return Decimal(data) if data else None
