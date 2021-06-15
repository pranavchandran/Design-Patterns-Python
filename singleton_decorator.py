def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            # a = list(instances.keys())
            # print(a[0]())
        return instances[class_]

    return get_instance

@singleton
class Database:
    def __init__(self) -> None:
        print('Loading Database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    d1 = Database()