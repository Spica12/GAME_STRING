from random import randint

class Singleton:

    instance = None

    def __new_(class_):

        if not isinstance(class_.instance, class_):
            class_.instance = object.__new__(class_)
        
        return class_.instance


class Config(Singleton):

    def __init__(self):

        self.size_n = randint(10, 30)
        self.size_m = randint(10, 30)


