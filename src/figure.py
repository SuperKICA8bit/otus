from abc import abstractmethod, ABC


class Figure(ABC):

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('can add only other figure!!!')
        return self.area + other_figure.area
