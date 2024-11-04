class MagicToyBox(type):
    def __init__(cls, name, bases, attrs):
        cls._toy_counter = 0
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwds):
        cls._toy_counter += 1
        return super().__call__(*args, **kwds)
    

class Toy(metaclass = MagicToyBox):
    def __init__(self, fun_shape):
        self.fun_shape = fun_shape

toy1 = Toy("🚗")
toy2 = Toy("🐵")
toy3 = Toy("🐬")

print(f"How many toys in the box? {Toy._toy_counter}")