from .decimal_field import DecimalField

__all__ = [
    "IntegerField",
]


class IntegerField(DecimalField):
    def to_string(self, data):
        return str(data)

    def convert(self, data):
        data = DecimalField.convert(self, data)
        return int(data) if data else None
