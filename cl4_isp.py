# ISP
from typing import AbstractSet
from abc import ABCMeta, abstractmethod

class Machine:
    def print1(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print1(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print1(self, document):
        pass
    def fax(self, document):
        pass 
    def scan(self, document):
        raise NotImplementedError("Printer cannot scan")
        # return super().scan(document)

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print1(self, document):
        print(document)
        
class Photocopier(Printer, Scanner):
    def print1(self, document): pass
    def scan(self, document): pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document): pass

    @abstractmethod
    def scan(self, document): pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    @abstractmethod
    def print1(self, document):
        self.printer.print(document)
    @abstractmethod
    def scan(self, document):
        self.scanner.scan(document)

old = OldFashionedPrinter()
old.scan('atext')