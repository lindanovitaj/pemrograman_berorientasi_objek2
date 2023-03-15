class Komik:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")

komikA = Komik("Slam Dunk", "Takehiko Inoue")
komikA.info()