# Lol, it's comment :)
class RGBColor(object):
    """
    Color in RGB palette
    """
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    @classmethod
    def initWithRed_andGreen_andBlue(cls, red, green, blue):
        return cls(red, green, blue)

    @classmethod
    def initWhite(cls):
        return cls(255, 255, 255)

    @classmethod
    def initBlack(cls):
        return cls(0, 0, 0)

    def red(self, value):
        if value is not None:
            self._red = value
        else:
            return self._red

    def green(self, value):
        if value is not None:
            self._green = value
        else:
            return self._green

    def blue(self, value):
        if value is not None:
            self._blue = value
        else:
            return self._blue

    def __sub__(self, other):
        return self.__class__().initWithRed_andGreen_andBlue(
            self.red() - other.red(),
            self.green() - other.green(),
            self.blue() - other.blue()
        )

    def inverted(self):
        return self.__class__().initWhite() - self
