


class Alive:
    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if isinstance(food, Fruit):
            self.fed = True
            print(f'{self.name} съел {food.name}')
        if isinstance(food, Flower):
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

#a = Alive(name:=None)




class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name




#p = Plant(name:=None)



class Mammal(Alive):
    pass

class Predator(Alive):
    pass

class Flower(Plant):
    pass


class Fruit(Plant):
     pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)