from statistics import median

from tasks.helpers.enums.figure_types import FigureTypes
from tasks.helpers.enums.triangle_types import TriangleTypes
from tasks.logic.figure_calculator.figure import FigureABC


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
                raise ValueError(f"side_{i + 1} must be > 0")

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

    def get_triangle_type(self):
        return self.__triangle_type.name

    def __doc__(self):
        result_str = super().__doc__()
        result_str += f'Triangle type: {self.__triangle_type.name}'

        if self.__triangle_type == TriangleTypes.STANDARD:
            result_str += f'\nHeight: {self.__height};'

        return result_str