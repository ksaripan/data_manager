from data_manager.reader import AbstractFileReader

__all__ = [
    "FixWidthFileReader",
]


class FixWidthFileReader(AbstractFileReader):
    def get_adapter(self, resource_file):
        return resource_file

    def pre_process_line(self, line, line_number):
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        return super().pre_process_line(line, line_number)

    def process_line(self, line, line_number):
        d = self.split(line, self.model)
        return super().process_line(d, line_number)

    def get_spec_list(self, model):
        fields = model.get_fields()
        spec_list = map(lambda field: (
            field.get_start_position(),
            field.get_length(),
        ), fields)
        return tuple(spec_list)

    def split(self, line, model):
        return [line[spec[0]:spec[0] + spec[1]] for spec in self.get_spec_list(model)]
