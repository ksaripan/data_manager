from decimal import Decimal

from data_manager.models import AbstractModel
from data_manager.models import fields
from data_manager.reader import CSVFileReader
from data_manager.writer import CSVFileWriter


class SampleModel(AbstractModel):
    fields = (
        fields.CharField('rec_type', start_position=0, length=1),
        fields.CharField('name', start_position=1, length=15),
        fields.DateField('birth_date', start_position=16, length=8, d_format='%Y%m%d'),
        fields.DecimalField('money', start_position=24, length=6, default_value=Decimal('0.00')),
    )


class SampleFileReader(CSVFileReader):
    model = SampleModel()
    skip_header = True
    delimiter = '|'

    def validate_line(self, line, line_number):
        return super().validate_line(line, line_number) and line[0] == 'D'


class SampleFileWriter(CSVFileWriter):
    model = SampleModel()
    delimiter = '|'

    def prepare_write(self, f, data):
        super().prepare_write(f, data)
        f.write('H|{n_line}'.format(n_line=len(data)))
        f.write(self.newline)


if __name__ == '__main__':
    reader = SampleFileReader()
    with open('./pipe_sample_file.csv', 'r') as f:
        data = reader.run(f)

    for d in data:
        print(d)

    writer = SampleFileWriter()
    with open('./out_pipe_sample_file.csv', 'w') as f:
        writer.run(f, data)
