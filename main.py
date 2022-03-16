import math

class WritingShape:
    def __init__(self, shape, rows):
        self._shape = shape
        self._shape_prt = " ".join(shape.split("-")).title()
        self._rows = rows
        self._reverse_list = list(range(1, rows + 1))[::-1]

    @property
    def _shape_choices(self):
        return (
            ("triangle-1", self._tri_1),
            ("triangle-2", self._tri_2),
            ("triangle-3", self._tri_3),
            ("triangle-4", self._tri_4),
            ("arrow-up", self._arrow_up),
            ("arrow-down", self._arrow_down),
            ("arrow-right", self._arrow_right),
            ("arrow-left", self._arrow_left),
            ("diamond", self._diamond)
        )

    @property
    def __done_message(self):
        return f"\n{self._shape_prt}\n"

    @property
    def __not_available_message(self):
        return f"\nOdd number only... in order to print {self._shape_prt.lower()}\n"

    @staticmethod
    def _reverse_list(rows):
        return list(range(1, rows + 1))[::-1]

    @staticmethod
    def _tri_ascending_1(rows):
        str = ""
        for row in range(1, rows + 1):
            str += "* " * row + "\n"
        return str

    @staticmethod
    def _tri_descending_2(rows):
        str = ""
        for row in range(rows, 0, -1):
            str += "* " * row + "\n"
        return str

    @staticmethod
    def _tri_ascending_3(rows, status):
        a_list = WritingShape._reverse_list(rows)
        str = ""
        for i, row in enumerate(a_list):
            if status == "single":
                str += "  " * (row - 1) + "* " * (i + 1) + "\n"
            if status == "join":
                str += "  " * (row) + "* " * (i + 1) + "\n"
        return str
            
    @staticmethod
    def _tri_descending_4(rows):
        a_list = WritingShape._reverse_list(rows)
        str = ""
        for i, row in enumerate(a_list):
            str += "  " * i + "* " * row + "\n"
        return str

    @staticmethod
    def _tri_ascending_center(rows, status):
        a_list = WritingShape._reverse_list(rows)
        str = ""
        for i, row in enumerate(a_list):
            if status == "single":
                str += " " * (row - 1) + "* " * (i + 1) + "\n"
            if status == "join":
                str += " " * (row) + "* " * (i + 1) + "\n"
        return str

    @staticmethod
    def _tri_descending_center(rows):
        a_list = WritingShape._reverse_list(rows)
        str = ""
        for i, row in enumerate(a_list):
            str += " " * i + "* " * row + "\n"
        return str

    def write_shape(self):
        for shp, func in self._shape_choices:
            if shp == self._shape:
                return func()

    def _tri_1(self):
        return WritingShape._tri_ascending_1(self._rows) + self.__done_message

    def _tri_2(self):
        return WritingShape._tri_descending_2(self._rows) + self.__done_message

    def _tri_3(self):
        return WritingShape._tri_ascending_3(self._rows, "single") + self.__done_message

    def _tri_4(self):
        return WritingShape._tri_descending_4(self._rows) + self.__done_message

    def _arrow_up(self):
        return WritingShape._tri_ascending_center(self._rows, "single") + self.__done_message

    def _arrow_down(self):
        return WritingShape._tri_descending_center(self._rows) + self.__done_message

    def _arrow_right(self):
        if self._rows % 2 == 1:
            top = math.floor(self._rows / 2)
            bottom = self._rows - top
            return WritingShape._tri_ascending_1(top) +  WritingShape._tri_descending_2(bottom) + self.__done_message
        else:
            return self.__not_available_message

    def _arrow_left(self):
        if self._rows % 2 == 1:
            top = math.floor(self._rows / 2)
            bottom = self._rows - top
            return WritingShape._tri_ascending_3(top, "join") + WritingShape._tri_descending_4(bottom) + self.__done_message
        else:
            return self.__not_available_message

    def _diamond(self):
        if self._rows % 2 == 1:
            top = math.floor(self._rows / 2)
            bottom = self._rows - top
            return WritingShape._tri_ascending_center(top, "join") + WritingShape._tri_descending_center(bottom) + self.__done_message
        else:
            return self.__not_available_message

tri_1 = WritingShape("triangle-1", 5)
print(tri_1.write_shape() + "\n")

tri_2 = WritingShape("triangle-2", 5)
print(tri_2.write_shape() + "\n")

tri_3 = WritingShape("triangle-3", 5)
print(tri_3.write_shape() + "\n")

tri_4 = WritingShape("triangle-4", 5)
print(tri_4.write_shape() + "\n")

arrow_up = WritingShape("arrow-up", 5)
print(arrow_up.write_shape() + "\n")

arrow_down = WritingShape("arrow-down", 5)
print(arrow_down.write_shape() + "\n")

arrow_right = WritingShape("arrow-right", 9)
print(arrow_right.write_shape() + "\n")

arrow_left = WritingShape("arrow-left", 7)
print(arrow_left.write_shape() + "\n")

diamond = WritingShape("diamond", 9)
print(diamond.write_shape() + "\n")


