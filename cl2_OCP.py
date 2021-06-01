from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 2

class Product:
    def __init__(self, name, color, size):
        self.name = name 
        self.color = color
        self.size = size


#OCP = Open for extension, closed for modification.
# Bad method Older approach
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
    def filter_by_size_and_color(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Specification
class Specification:
    def is_satisfied(self, item): pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def is_satisfied(self, item, color):
        return item.color == color

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

# Combinator
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('TREE', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old approach):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'- {p.name} is green')

    bf = BetterFilter()
    print("Green products (new:")

    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'- {p.name} is green')

    print('Large Products')
    sl = SizeSpecification(Size.LARGE)
    sf = BetterFilter()

    for p in bf.filter(products, sl):
        print(f'{p.name} is Larger in size')

    print('Large blue items')
    # large_blue = AndSpecification(sl, ColorSpecification(Color.BLUE))
    large_blue = sl & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f'-{p.name} is large and blue')



# si = SizeSpecification(Size.SMALL)
# a1 = Product("django", Color.RED, Size.SMALL)
# print(a1.size)
# print(a1.__dict__)
# print(si.__dict__)
# isize =si.is_satisfied(a1)
# print(isize)








