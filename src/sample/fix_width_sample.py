from decimal import Decimal

from data_manager.models import AbstractModel
from data_manager.models import fields
from data_manager.models.fields.abstract_field import Constants
from data_manager.reader import FixWidthFileReader
from data_manager.writer import FixWidthFileWriter


class SampleModel(AbstractModel):
    fields = (
        fields.CharField('rec_type', start_position=0, length=1),
        fields.CharField('name', start_position=1, length=15),
        fields.DateField('birth_date', start_position=16, length=8, d_format='%Y%m%d'),
        fields.DecimalField('money', start_position=24, length=6, align=Constants.ALIGN_RIGHT, default_value=Decimal('0.00')),
    )


class SampleFileReader(FixWidthFileReader):
    model = SampleModel()
    skip_header = True

    def validate_line(self, line, line_number):
        return super().validate_line(line, line_number) and line[0] == 'D'


class SampleFileWriter(FixWidthFileWriter):
    model = SampleModel()


if __name__ == '__main__':
    reader = SampleFileReader()
    with open('./fix_width_sample_file.txt', 'r') as f:
        data = reader.run(f)

    for d in data:
        print(d)

    writer = SampleFileWriter()
    with open('./out_fix_width_sample_file.txt', 'w') as f:
        writer.run(f, data)
