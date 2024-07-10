class Buah:
    def _init_(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def setNama(self, nama):
        self.nama = nama
    
    def setWarna(self, warna):
        self.warna = warna
    
    def setRasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"


class Mangga(Buah):
    def _init_(self, nama, warna, rasa, vitamin):
        super()._init_(nama, warna, rasa)
        self.vitamin = vitamin
    
    def setVitamin(self, vitamin):
        self.vitamin = vitamin
    
    def setInformation(self):
        info = super().information()
        return f"{info}, Vitamin: {self.vitamin}"


mangga1 = Mangga("Mangga Arumanis", "Hijau", "Manis", "Vitamin C")


print(mangga1.information())      
print(mangga1.setInformation())   
mangga1.setVitamin("Vitamin A")
print(mangga1.setInformation())