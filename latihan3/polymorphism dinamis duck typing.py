class Sapi:
    def mooo(self):
        print("Moooo!")
    
class Manusia:
    def mooo(self):
        print("Saya bersuara seperti sapi!")

def bersuara(obj):
    obj.mooo()

sapi = Sapi()
manusia = Manusia()

bersuara(sapi)
bersuara(manusia)
