import random
class Animal:
    def __init__(self, speed = 0, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def move(self, dx , dy, dz ):
        if dz < 0:
            print(f"It's too deep, i can't dive")
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed
            return self

    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):

    def __init__(self, speed):
         super().__init__(speed)
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
         self.dz = dz
         self._cords[2] = int(self._cords[2] - abs(dz) * self.speed / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal, ):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"
        # super().live
        # super().beak
        # super().speak()
        # super().attack()
        # super().move(dx:= 0,dy:= 0, dz:= 0)
        # super().get_cords()
        # super().dive_in(dz)
        # super().lay_eggs()






db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
