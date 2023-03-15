class Laptop:
    def __init__(self, merk, warna):
     self.merk = merk
     self.warna = warna

    def info(self):
        print(f"Laptop {self.merk} berwarna {self.warna}")

laptopA = Laptop("Asus Notebook 15", "Navy")
laptopA.info() 