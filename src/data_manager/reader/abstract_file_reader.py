import os

from data_manager.models import EmptyField

__all__ = [
    "AbstractFileReader",
]


class AbstractFileReader:
    model = None
    skip_header = False

    def __init__(self) -> None:
        super().__init__()
        self.fields = self.model.get_fields()

    def run(self, resource_file):
        self.prepare_read(resource_file)
        data = self.read(resource_file)
        self.post_read(data, resource_file)
        return data

    def prepare_read(self, resource_file):
        pass

    def get_adapter(self, resource_file):
        raise NotImplementedError()

    def read(self, resource_file):
        data = list()
        extra = self.get_extra(resource_file)
        line_number = -1
        adapter = self.get_adapter(resource_file)
        for line in adapter:
            line_number += 1
            valid_line = self.validate_line(line, line_number)
            if not valid_line:
                continue
            line = self.pre_process_line(line, line_number)
            d = self.process_line(line, line_number)
            d = self.post_process_line(d, extra, line_number)
            data.append(d)
        self.post_read(data, resource_file)
        return data

    def get_extra(self, resource_file):
        return dict()

    def validate_line(self, line, line_number):
        # skip if header
        skip = not (self.skip_header and line_number == 0)
        return skip and line

    def pre_process_line(self, line, line_number):
        return line

    def process_line(self, data, line_number):
        data_length = len(data)
        d = dict()
        for idx in range(len(self.fields)):
            f = self.fields[idx]
            field_name = f.get_name()
            field_value = f.from_string(data[idx] if idx < data_length else None)
            d[field_name] = field_value
        # Remove empty field
        d.pop(EmptyField.EMPTY_FIELD_NAME, None)
        return d

    def post_process_line(self, d, extra, line_number):
        return {**extra, **d}

    def post_read(self, data, file_path):
        pass
