class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if not all(isinstance(x, (int, float)) for x in sides):
            print("Значения сторон должны быть числовыми!")
        if any(x <= 0 for x in sides):
            print("Стороны не могут быть отрицательными")
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_sides(self):
        return self.__sides

    def color(self):
        return self.__color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(x > 0 for x in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2 * 3.14)

    def radius(self):
        return self.__radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color,*[sides[0]] * 12)

    def get_volume(self):
        return self._Figure__sides[0] ** 3






circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
