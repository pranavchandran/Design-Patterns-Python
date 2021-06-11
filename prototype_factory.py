import copy


class Address:
    def __init__(self, street_address, city, suite) -> None:
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.suite}'


class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 padakulam', 'London', 0))
    aux_office_employee = Employee('', Address('123Bo padakulam', 'London', 0))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


john = EmployeeFactory.new_main_office_employee('Hohny Kuttan', 109)
jane = EmployeeFactory.new_aux_office_employee('Jane', 510)
print(john)
print(jane)
