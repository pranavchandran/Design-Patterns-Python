class AB(list):
    def __init__(self, end):
        for x in range(1,end):
            self.append(x)

a = AB(10)
print(a)