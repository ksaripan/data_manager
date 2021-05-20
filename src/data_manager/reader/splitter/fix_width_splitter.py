from data_manager.reader.splitter.abstract_splitter import AbstractSplitter

__all__ = [
    'FixWidthSplitter',
]


class FixWidthSplitter(AbstractSplitter):
    def get_spec_list(self, model):
        fields = model.get_fields()
        spec_list = map(lambda field: (
            field.get_start_position(),
            field.get_length(),
        ), fields)
        return tuple(spec_list)

    def split(self, line, model):
        return [line[spec[0]:spec[0] + spec[1]] for spec in self.get_spec_list(model)]
