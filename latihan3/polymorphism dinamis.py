class Kalkulator:
    def add(self, x, y, z = 0):
        return x + y + z
    def add(self, a, b, c=0):
        return a + b + c

cal = Kalkulator()
kul = Kalkulator()
b = cal.add(1, 0, 3)
c = kul.add(9,5)
print(b)
print(c)
