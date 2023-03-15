class Pegawai:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")

pegawaiB = Pegawai("Minnie", "5789490")
pegawaiB.info()