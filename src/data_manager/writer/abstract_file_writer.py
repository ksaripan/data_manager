class AbstractFileWriter:
    model = None
    newline = '\n'

    def run(self, f, data):
        self.prepare_write(f, data)
        self.write(f, data)
        self.post_write(f, data)

    def prepare_write(self, f, data):
        pass

    def write(self, f, data):
        adapter = self.get_adapter(f)
        for d in data:
            self.pre_write_line(adapter, d)
            self.write_line(adapter, d)
            self.post_write_line(adapter, d)

    def pre_write_line(self, adapter, line):
        pass

    def write_line(self, adapter, line):
        output_str = self.format_line(line)
        adapter.write(output_str)
        adapter.write(self.newline)

    def get_adapter(self, resource_file):
        raise NotImplementedError()

    def format_line(self, line):
        raise NotImplementedError()

    def post_write_line(self, adapter, line):
        pass

    def post_write(self, f, data):
        pass
