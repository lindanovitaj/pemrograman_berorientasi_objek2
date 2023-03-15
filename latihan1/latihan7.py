class Reamur:
    @staticmethod
    def to_fahrenheit(reamur):
        return (reamur * 9/4) + 32
    
    @staticmethod
    def to_kelvin(reamur):
        return reamur * 5/4 + 273.15
    
    @staticmethod
    def to_celcius(reamur):
        return reamur * 5/4
    
myreamur = 80
myfahrenheit = Reamur.to_fahrenheit(myreamur)
print(myfahrenheit)
