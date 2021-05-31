# Single Responsibility Priciple

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # Bad method all in one class

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     f = open(filename, "r")
    #     print(f.read())

    # def low_from_web(self, uri):
    #     pass

j = Journal()
j.add_entry('I cried today')
j.add_entry('I solved')
# print(f'Jounral entries: \n{j}')

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
file = "./test1.txt"
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())

# a = Journal()
# a.entries = [str(x) for x in range(10)]
# print(a)
# j = Journal()
# j.add_entry('I cried today')
# j.add_entry('I solved')
# print(f'Jounral entries: \n{j}')