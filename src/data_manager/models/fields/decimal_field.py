from decimal import Decimal

from data_manager.models.fields.abstract_field import AbstractField, Constants

__all__ = [
    "DecimalField",
]


class DecimalField(AbstractField):
    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None,
                 align=Constants.ALIGN_DEFAULT, delimiter=',', output_delimiter=None):
        AbstractField.__init__(self, name, strip, default_value, length, start_position, align)
        self.delimiter = delimiter
        self.output_delimiter = output_delimiter
        self.output_format = '{' + (':{}'.format(output_delimiter) if output_delimiter else '') + '}'

    def to_string(self, data):
        s = self.output_format.format(data)
        return s

    def convert(self, data):
        if not data:
            return None
        data = data.replace(self.delimiter, '')
        return Decimal(data)
