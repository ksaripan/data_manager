from data_manager.models.fields.abstract_field import AbstractField

__all__ = [
    "BooleanField",
]


class BooleanField(AbstractField):
    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None, true_string='T',
                 false_string='F') -> None:
        super().__init__(name, strip, default_value, length, start_position)
        self.__true_string = true_string
        self.__false_string = false_string

    def to_string(self, data):
        return self.__true_string if data else self.__false_string

    def convert(self, data):
        return True if data == self.__true_string else False
