from data_manager.models.fields.abstract_field import Constants
from .abstract_formatter import AbstractFormatter


class FixWidthFormatter(AbstractFormatter):
    def format_line(self, model, d):
        fields = model.get_fields()
        value_list = []

        for f in fields:
            value = d.get(f.get_name(), f.get_default_value())
            v_str = f.to_string(value)
            v_str = '%{align}{length}s'.format(
                align='-' if f.get_align() is Constants.ALIGN_LEFT else '',
                length=f.get_length(),
            ) % v_str
            value_list.append(v_str)
        line = ''.join(value_list)

        return line
