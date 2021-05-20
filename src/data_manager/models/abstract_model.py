__all__ = [
    "AbstractModel",
]


class AbstractModel:
    fields = []

    def get_fields(self):
        return self.fields
