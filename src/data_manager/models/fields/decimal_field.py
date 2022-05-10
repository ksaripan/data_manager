from decimal import Decimal

from data_manager.models.fields.abstract_field import AbstractField, Constants

__all__ = [
    "DecimalField",
]


class DecimalField(AbstractField):
    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None,
                 align=Constants.ALIGN_DEFAULT, delimiter=',', output_delimiter=None, decimal_places=None):
        AbstractField.__init__(self, name, strip, default_value, length, start_position, align)
        self.delimiter = delimiter
        self.output_delimiter = output_delimiter
        self.output_format = '{' + (':{}'.format(output_delimiter) if output_delimiter else '') + '}'

        # Normally decimal places is not required, this is added to support fix width without delimiter
        # Ex. 1000 with decimal places = 2, then the result should be 10.00
        self.decimal_places = decimal_places

    def to_string(self, data):
        s = self.output_format.format(data)
        return s

    def convert(self, data):
        if not data:
            return None
        data = data.replace(self.delimiter, '')
        if self.decimal_places:
            data = data[:-self.decimal_places] + '.' + data[-self.decimal_places:]
        # Handle data with leading-zero
        # Ex. 00-49.00
        data = data.lstrip('0')
        # Handle data with all zero
        # Ex. 0000
        if len(data) == 0:
            data = '0.00'
        return Decimal(data)
