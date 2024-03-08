from statistics import median

import math
from task_1.helpers.figure_types import FigureTypes
from task_1.helpers.triangle_types import TriangleTypes
from abc import ABC, abstractmethod


class FigureABC(ABC):
    __figure_type: FigureTypes
    __area: float

    def __init__(self, figure_type: FigureTypes, area: float):
        self.__figure_type = figure_type
        self.__area = area

    def get_area(self): return self.__area

    @abstractmethod
    def __doc__(self):
        return f'Figure: {self.__figure_type.name}; \nArea: {self.__area}; \n'


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


class Triangle(FigureABC):
    __sides_l: list

    __a_side: float
    __b_side: float
    __c_or_hypotenuse_side: float

    __s: float
    __height: float

    __triangle_type: TriangleTypes

    def __init__(self, side_1: float, side_2: float, side_3: float):

        self.__sides_l = [side_1, side_2, side_3]

        for i, side in enumerate(self.__sides_l):
            if side <= 0:
                raise ValueError(f"side_{i+1} must be > 0")

        area = -1

        is_found_triangle_type = False

        for i, index_element in enumerate([(0, 1, 2), (0, 2, 1), (1, 2, 0)]):
            self.__a_side = self.__sides_l[index_element[0]]
            self.__b_side = self.__sides_l[index_element[1]]
            self.__c_or_hypotenuse_side = self.__sides_l[index_element[2]]

            if self.__a_side ** 2 + self.__b_side ** 2 == self.__c_or_hypotenuse_side ** 2:
                self.__triangle_type = TriangleTypes.RIGHT

                area = (self.__a_side * self.__b_side) / 2

                self.__s = -1
                self.__height = -1

                is_found_triangle_type = True
                break

        if not is_found_triangle_type:
            for i, index_element in enumerate([(0, 1, 2), (0, 2, 1), (1, 2, 0)]):
                self.__a_side = self.__sides_l[index_element[0]]
                self.__b_side = self.__sides_l[index_element[1]]
                self.__c_or_hypotenuse_side = self.__sides_l[index_element[2]]

                if self.__a_side + self.__b_side <= self.__c_or_hypotenuse_side:
                    self.__triangle_type = TriangleTypes.WRONG_BROKEN
                    print("---> SUM OF TWO SIDE LENGTHS HAS TO EXCEED THE LENGTH OF THE THIRD SIDE <---")
                    super().__init__(FigureTypes.TRIANGLE, -1)
                    return


            self.__triangle_type = TriangleTypes.STANDARD

            self.__s = (self.__a_side + self.__b_side + self.__c_or_hypotenuse_side) / 2
            area = (self.__s * (self.__s - self.__a_side)
                    * (self.__s - self.__b_side)
                    * (self.__s - self.__c_or_hypotenuse_side)) ** (1 / 2)
            self.__height = area / ((1 / 2) * median(self.__sides_l))

        super().__init__(FigureTypes.TRIANGLE, area)

    def __doc__(self):
        result_str = super().__doc__()
        result_str += f'Triangle type: {self.__triangle_type.name}'

        if self.__triangle_type == TriangleTypes.STANDARD:
            result_str += f'\nHeight: {self.__height};'

        return result_str

