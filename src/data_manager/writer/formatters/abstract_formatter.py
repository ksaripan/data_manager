__all__ = [
    'AbstractFormatter',
]


class AbstractFormatter:
    def format_line(self, model, d):
        raise NotImplementedError()
