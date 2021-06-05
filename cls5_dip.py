# DIP
from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    parent = 0
    child = 1
    sibling = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser: #interface
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationshipBrowser): #lowlevel
    # because storage is a low level concern []
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.parent, child)
        )
        self.relations.append(
            (child, Relationship.child, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1]==Relationship.parent:
                yield r[2].name


class Research: #High Level
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.parent:
    #             print(f'John has a child called {r[2].name}.')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
print(Research.mro())



