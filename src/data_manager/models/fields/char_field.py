from data_manager.models.fields.abstract_field import AbstractField

__all__ = [
    "CharField",
]


class CharField(AbstractField):
    def to_string(self, data):
        return data

    def convert(self, data):
        return data
