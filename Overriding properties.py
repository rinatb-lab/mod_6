class Vehicle:
    def __init__(self, owner:str, __model:str,
                 __engine_power:int, __color:str ):
        self.owner = owner
        self.__model =__model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        print(f'Модель: {self.__model}')
        return self
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print('Модель: ',self.__model )
        print('Мощность: ',self.__engine_power)
        print('Цвет: ',self.get_color())
        print('Владелец:',self.owner)
        return self
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
            return self


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()





