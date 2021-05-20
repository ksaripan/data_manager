__all__ = [
    'AbstractSplitter',
    'AbstractDelimitedSplitter',
]


class AbstractSplitter:
    def split(self, line, model):
        raise NotImplementedError()


class AbstractDelimitedSplitter(AbstractSplitter):
    delimiter = ''

    def split(self, line, model):
        return line.split(self.delimiter)
