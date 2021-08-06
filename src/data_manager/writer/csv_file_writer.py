import csv

from data_manager.writer import AbstractFileWriter

__all__ = [
    'CSVFileWriter',
]


class CSVFileWriter(AbstractFileWriter):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    quoting = csv.QUOTE_MINIMAL

    def get_adapter(self, resource_file):
        return csv.writer(resource_file, dialect=self.get_dialect())

    def get_dialect(self):
        class CSVDialect(csv.excel):
            delimiter = self.delimiter
            quotechar = self.quotechar
            doublequote = self.doublequote
            skipinitialspace = self.skipinitialspace
            lineterminator = self.newline
            quoting = self.quoting
        return CSVDialect

    def format_line(self, d):
        fields = self.model.get_fields()
        value_list = []
        for f in fields:
            value = d.get(f.get_name(), f.get_default_value())
            v_str = f.to_string(value)
            value_list.append(v_str)
        return value_list

    def write_line(self, f, line):
        v_list = self.format_line(line)
        f.writerow(v_list)
