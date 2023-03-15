class Tabung:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def volume(self):
            return 3.14 * (self.jari_jari * self.jari_jari * self.tinggi)
    
tabungA = Tabung(7, 13)
print(f"Volume Tabung : {tabungA.volume()}")
