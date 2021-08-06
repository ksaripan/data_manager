import csv

from data_manager.reader import AbstractFileReader

__all__ = [
    "CSVFileReader",
]


class CSVFileReader(AbstractFileReader):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

    def get_adapter(self, resource_file):
        return csv.reader(resource_file, dialect=self.get_dialect())

    def get_dialect(self):
        class CSVDialect(csv.excel):
            delimiter = self.delimiter
            quotechar = self.quotechar
            doublequote = self.doublequote
            skipinitialspace = self.skipinitialspace
            lineterminator = self.lineterminator
            quoting = self.quoting
        return CSVDialect



