import os

__all__ = [
    "AbstractFileReader",
]


class AbstractFileReader:
    model = None
    splitter = None
    encoding = 'utf-8'

    def __init__(self) -> None:
        super().__init__()
        self.fields = self.model.get_fields()

    def run(self, file_path):
        file_path = os.path.expandvars(os.path.expanduser(file_path))
        self.prepare_read(file_path)
        data = self.read(file_path)
        self.post_read(data, file_path)
        return data

    def prepare_read(self, file_path):
        valid_file = self.validate_file(file_path)
        if not valid_file:
            raise RuntimeError(f'file_validation_failure: {file_path}')

    def validate_file(self, file_path):
        return os.path.exists(file_path)

    def read(self, file_path):
        data = list()
        with open(file_path, 'r', encoding=self.encoding) as f:
            extra = self.get_extra(file_path)
            for line in f:
                valid_line = self.validate_line(line)
                if not valid_line:
                    continue
                line = self.pre_process_line(line)
                d = self.process_line(line)
                d = self.post_process_line(d, extra)
                data.append(d)
        self.post_read(data, file_path)
        return data

    def get_extra(self, file_path):
        return dict()

    def validate_line(self, line):
        return line

    def pre_process_line(self, line):
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        return line

    def process_line(self, line):
        d = self.splitter.split(line, self.model)
        # Changes to tuple unpack feature that is remove in python3
        # idx = idx_value[0]
        # value = idx_value[1]
        # d = map(lambda idx_value: self.fields[idx_value[0]].from_string(idx_value[1]), enumerate(d))
        d = map(lambda idx_value: (
            self.fields[idx_value[0]].get_name(),
            self.fields[idx_value[0]].from_string(idx_value[1])
        ), enumerate(d))
        d = dict(d)
        return d

    def post_process_line(self, d, extra):
        return {**extra, **d}

    def post_read(self, data, file_path):
        pass
