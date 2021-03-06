# 1st_task


class Matrix:

    def __init__(self, our_matrix):
        self.our_matrix = our_matrix

    def __str__(self):
        """Т.е. представялем каждую строчку матрицы как строку"""
        kostil = ''
        for row in self.our_matrix:
            kostil += str(row) + '\n'
        return kostil

    def __add__(self, other):
        """Суммируем каждую строчку первой матрицы с каждой строчкой второй матрицы,
        далее пользуемся приеммом из метода __str__"""

        i = 0
        final_matrix = []
        if len(self.our_matrix) == len(other.our_matrix):
            while i < len(self.our_matrix):
                summary_matrix = [row_First_Matrix + row_Second_Matrix for
                                  row_First_Matrix, row_Second_Matrix in zip(self.our_matrix[i], other.our_matrix[i])]
                final_matrix.append(summary_matrix)

                i += 1

            second_kostil = ''

            for row in final_matrix:
                second_kostil += str(row) + '\n'
            return second_kostil

        else:
            return "Матрицы должны быть соразмерны!"


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_Two = Matrix([[2, 3, 4], [5, 6, 7]])

print(matrix + matrix_Two)

# 2nd_task
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(size)
        self.size = size

    @property
    def how_tissue(self):
        return self.size / 6.5 + 0.5


class Jacket(Clothes):

    def __init__(self, name, height):
        super().__init__(height)
        self.height = height

    @property
    def how_tissue(self):
        return self.height * 2 + 0.3


my_Jacket = Jacket("Panderson", 60)
my_Coat = Coat("BBs", 60)

print(my_Jacket.how_tissue, my_Coat.how_tissue)

# 3d_task

class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        new_cell = Cell(self.cells + other.cells)
        return new_cell

    def __sub__(self, other):
        new_cell = Cell(self.cells - other.cells)
        if self.cells > other.cells:
            return new_cell
        else:
            return "Разносить должна быть больше нуля!"

    def __mul__(self, other):
        new_cell = Cell(self.cells * other.cells)
        return new_cell

    def __truediv__(self, other):
        new_cell = Cell(round(self.cells / other.cells))
        return new_cell

    def make_order(self, cnt):
        """full_row - количество полных строк
           cells_in_not_full_row - количество клеток в неполной строке
           cnt - прокидывает пользователь - кол-во клеток в строке"""
        full_row = self.cells // cnt
        cells_in_not_full_row = self.cells % cnt
        final = ''
        i = 0
        if cells_in_not_full_row == 0:
            n = 0
        else:
            n = 1
        while i < full_row + n:
            if i < full_row:
                final += cnt * '*'
                final += '\n'
                i += 1
            elif i >= full_row:
                final += cells_in_not_full_row * '*'
                i += 1
        return final


first_Cell = Cell(34)
second_Cell = Cell(10)
third_Cell = first_Cell * second_Cell
fourth_Cell = first_Cell / second_Cell
fifth_Cell = first_Cell + second_Cell
sixth_Cell = first_Cell - second_Cell

print(third_Cell.cells)
print(fourth_Cell.cells)
print(fifth_Cell.cells)
print(sixth_Cell.cells)
print(first_Cell.make_order(8))


