import math

from tasks.helpers.enums.figure_types import FigureTypes
from tasks.logic.figure_calculator.figure import FigureABC


class Circular(FigureABC):
    __PI: float
    __radius: float

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")

        self.__PI = math.pi
        self.__radius = radius

        area = self.__PI * self.__radius ** 2

        super().__init__(FigureTypes.CIRCULAR, area)

        pass

    def __doc__(self):
        result_str = super().__doc__()
        result_str += f'Radius: {self.__radius};'
        return result_str
