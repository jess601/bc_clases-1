# En el archivo persona.py Crear una clase Persona con atributo nombre
# Despues instanciar un objeto de tipo persona

class Dino:
    patas = 4
    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Hola soy un dinosaurio",", me llamo", self.nombre," y tengo", self.patas, "patas")

    def get_patas(self):
        return self.patas
    
    def set_patas(self, cantidad):
        self.patas = cantidad
    
    def cortar_pata(self):
        self.patas = self.patas - 1

pepito = Dino("Pepito")