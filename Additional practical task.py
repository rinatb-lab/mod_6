
class Figure:
    def __init__(self, __color , *args):
        self.__sides = []
        #self.__color = [0, 0, 0]
        self.__color = list(__color)

        # Заполнение списка __sides
        for __side in args:
            self.__sides.append(__side)
        #print(self.__sides)
        # Окончательное определение списка __sides
        #в зависимости от количества сторон
        Figure.checking_sides(self)
        #print(self.__sides)
    sides_count = 0

    def checking_sides(self):  #проверка числа сторон и заполнение __sides
        #print(len(self.__sides))
        if len(self.__sides) > 1:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        else:
            for i in range(1, self.sides_count):
                self.__sides.append(self.__sides[0])
        return self.__sides
    def __is_valid_color(self, r, g, b):
        y = [r, g, b]
        start, end = 0, 255
        in_range = all(start <= num <= end for num in y)
        if in_range and all(isinstance(n, int) for n in y):
            self.__color = y
        else:
            return
        return self.__color    
    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)
        #print(self.__color)
        return self.__color
    def get_color(self):
        return f'{self.__color}'

    side1 = False

    def __is_valid_sides(self, *new_sides):
        z = [*new_sides]
        #print(len(z))
        #print(self.sides_count)
        #print(self.side1)
        if self.sides_count == len(z):
            for j in range(len(z)):
                if z[j] > 0 and isinstance(z[j], int): #целое и положительное число
                    self.side1 = True
                else:
                    self.side1 = False
                #print(self.side1)
                return self.side1

    def get_sides(self):
        return f'{self.__sides}'

    def set_sides(self, *new_sides):
        z = [*new_sides]
        self.__is_valid_sides(*new_sides)
        #print(self.__sides)
        #print(self.side1)
        if self.side1:
            self.__sides = z
        #print(self.__sides)
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color , *__sides)
        Figure.__color = __color
        self.sides_count = 1
        super().get_sides()
        super().__len__()
    _RADIUS = 0
    sides_count = 1

    def get_square(self):
        len_circle = super().__len__()
        s = int(len_circle)**2/(4 * 3.14)
        return f'Площадь круга = {s}'
    def radius(self):
        len_circle = super().__len__()
        self._RADIUS = int(len_circle)/(2 * 3.14)
        return f'Радиус круга = {self._RADIUS}'

class Triangle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color , *__sides)
        self.sides_count = 3
        super().get_sides()
        super().__len__()
    sides_count = 3

class Cube(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color , *__sides)
        Figure.__color = __color
        super().get_sides()
        super().__len__()

    sides_count = 12

    def cube_volume(self):
        cube_side = cube1.get_sides()
        v = int(cube_side[1]) ** 3
        return f'Объем куба = {v}'



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

#Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
#print(cube1.self)

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

## Проверка периметра (круга), это и есть длина:
print(len(circle1))
## Проверка объёма (куба):
print(cube1.cube_volume())
print(circle1.get_square())
print(circle1.radius())

