# Abstract base class
from abc import ABC
from enum import Enum

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('THis tea is delicious')

class Cofee(HotDrink):
    def consume(self):
        print('This coffee is delcious.')

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water,'
                f' pour {amount}ml, enjoy')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water,'
                f' pour {amount}ml, enjoy!')
        return Cofee()

def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = 0
        TEA = 1
    
    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        s = input(f'Please pick drink (0-{len(self.factories)-1}: ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


# if __name__ == '__main__':
#     entry = input("what kind of drink you like?")
#     drink = make_drink(entry)
#     drink.consume()

# second phase
if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
