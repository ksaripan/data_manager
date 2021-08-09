class Constants:
    ALIGN_LEFT = 'ALIGN_LEFT'
    ALIGN_RIGHT = 'ALIGN_RIGHT'
    ALIGN_DEFAULT = ALIGN_LEFT


class AbstractField:

    def __init__(self, name, strip=True, default_value=None, length=0, start_position=None, align=Constants.ALIGN_DEFAULT) -> None:
        super().__init__()
        self.__name = name
        self.__strip = strip
        self.__default_value = default_value
        self.__length = length
        self.__start_position = start_position
        self.__align = align

    def get_name(self):
        return self.__name

    def get_length(self):
        return self.__length

    def get_start_position(self):
        return self.__start_position

    def get_default_value(self):
        return self.__default_value

    def get_align(self):
        return self.__align

    def from_string(self, data):
        if self.__strip and data is not None:
            data = data.strip()
        result = self.convert(data)
        if result is None:
            return self.get_default_value()
        return result

    def to_string(self, data):
        raise NotImplementedError()

    def convert(self, data):
        raise NotImplementedError()
