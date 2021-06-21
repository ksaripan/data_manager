from data_manager.models.fields.abstract_field import AbstractField

__all__ = [
    "IntegerField",
]


class IntegerField(AbstractField):
    def to_string(self, data):
        return str(data)

    def convert(self, data):
        return int(data) if data else None
