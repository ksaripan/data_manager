from .abstract_formatter import AbstractFormatter

__all__ = [
    'DelimitedFormatter',
    'CSVDelimitedFormatter',
    'PipeDelimitedFormatter',
]


class DelimitedFormatter(AbstractFormatter):
    delimiter = None

    def format_line(self, model, d):
        fields = model.get_fields()
        line = map(lambda f: f.to_string(
            d.get(
                f.get_name(),
                f.get_default_value(),
            )
        ), fields)
        return self.delimiter.join(line)


class CSVDelimitedFormatter(DelimitedFormatter):
    delimiter = ','


class PipeDelimitedFormatter(DelimitedFormatter):
    delimiter = '|'
