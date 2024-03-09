from task_1.helpers.figure_types import FigureTypes
from abc import ABC, abstractmethod


class FigureABC(ABC):
    __figure_type: FigureTypes
    __area: float

    def __init__(self, figure_type: FigureTypes, area: float):
        self.__figure_type = figure_type
        self.__area = area

    def get_area(self): return self.__area

    def get_figure(self): return self.__figure_type.name

    @abstractmethod
    def __doc__(self):
        return f'Figure: {self.__figure_type.name}; \nArea: {self.__area}; \n'



