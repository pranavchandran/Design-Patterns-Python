# Monostate
class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old.'

class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f'{self.name} manages ${self.money_managed}'

        
if __name__ == '__main__':
    cfo1 = CFO()
    cfo1.name = 'Minna'
    cfo1.money_managed = 100000
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Kuttu'
    cfo2.money_managed = 9000
    print(cfo2, cfo1)