class AbstractFileWriter:
    model = None
    formatter = None
    newline = '\n'
    encoding = 'utf-8'

    def run(self, f, data):
        self.prepare_write(f, data)
        self.write(f, data)
        self.post_write(f, data)

    def prepare_write(self, f, data):
        pass

    def write(self, f, data):
        for d in data:
            self.pre_write_line(f, d)
            self.write_line(f, d)
            self.post_write_line(f, d)

    def pre_write_line(self, f, line):
        pass

    def write_line(self, f, line):
        output_str = self.format_line(line)
        f.write(output_str)

    def format_line(self, line):
        return self.formatter.format_line(self.model, line)

    def post_write_line(self, f, line):
        f.write(self.newline)

    def post_write(self, f, data):
        pass
