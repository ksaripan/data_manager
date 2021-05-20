from data_manager.reader.splitter.abstract_splitter import AbstractDelimitedSplitter

__all__ = [
    'CSVSplitter',
    'PipeSplitter',
]


class CSVSplitter(AbstractDelimitedSplitter):
    delimiter = ','


class PipeSplitter(AbstractDelimitedSplitter):
    delimiter = '|'
