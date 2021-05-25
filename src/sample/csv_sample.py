from data_manager.models import AbstractModel
from data_manager.models import fields
from data_manager.reader import AbstractFileReader, CSVSplitter


class SampleModel(AbstractModel):
    fields = (
        fields.CharField('rec_type', start_position=0, length=1),
        fields.CharField('name', start_position=1, length=15),
        fields.DateField('birth_date', start_position=16, length=8, d_format='%Y%m%d'),
        fields.DecimalField('money', start_position=24, length=6),
    )


class SampleFileReader(AbstractFileReader):
    model = SampleModel()
    splitter = CSVSplitter()
    skip_header = True

    def validate_line(self, line, line_number):
        return super().validate_line(line, line_number) and line[0] == 'D'


if __name__ == '__main__':
    reader = SampleFileReader()

    with open('./csv_sample_file.csv', 'r') as f:
        data = reader.run(f)
        for d in data:
            print(d)
