from data_manager.models.fields.abstract_field import AbstractField, Constants

__all__ = [
    "EmptyField",
]


class EmptyField(AbstractField):
    EMPTY_FIELD_NAME = '_empty_field'

    def __init__(self) -> None:
        super().__init__(EmptyField.EMPTY_FIELD_NAME)

    def to_string(self, data):
        return ''

    def convert(self, data):
        return None
