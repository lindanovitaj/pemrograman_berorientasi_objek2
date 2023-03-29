# LINDA NOVITA JULIYANTI
# 210510003
# D3

from abc import ABC, abstractmethod

class Kendaraan(ABC):
  @abstractmethod
  def start(self):
    pass

class Mobil(Kendaraan):
  def start(self):
    print("Menjalankan mesin mobil...")

class Motor(Kendaraan):
  def start(self):
    print("Menjalankan mesin motor...")

class Sportcar(Kendaraan):
  def start(self):
    print("Menjalankan mesin sportcar...")

kendaraan = [Mobil(), Motor(), Sportcar()]
for kendaraan in kendaraan:
  kendaraan.start()
