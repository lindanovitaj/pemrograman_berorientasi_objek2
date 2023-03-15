class Bus:
    def __init__(self, terminal, tujuan):
        self.terminal = terminal
        self.tujuan = tujuan

    def info(self):
        print(f"Terminal: {self.terminal}\nTujuan: {self.tujuan}")

busA = Bus("Harjamukti Cirebon", "Cirebon - Bandung")
busA.info()
