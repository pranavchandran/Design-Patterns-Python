import copy


class Address:
    def __init__(self, street_address, city, country) -> None:
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives {self.address}'
# address = Address('123 London', 'North London', 'UK')
# john = Person('Johny', Address('123 London', 'East London', 'UK'))
# jane = Person('Jane', address)
# print(john)
# print(jane)


# check deepcopy
john = Person('Johny', Address('123 London', 'East London', 'UK'))
jane = copy.deepcopy(john)
jane.name = 'Jane sasi'
jane.address.street_address = '124 padakulam'
jane.address.city = 'leio'
print(john)
print(jane)
