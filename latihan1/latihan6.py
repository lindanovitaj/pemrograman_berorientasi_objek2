class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
print(Kalkulator.add(6, 9))
print(Kalkulator.subtract(9, 8))
print(Kalkulator.multiply(4, 7))
print(Kalkulator.divide(10, 2))