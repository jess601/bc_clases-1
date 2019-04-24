class Persona:
    nombre_persona = None
    edad_persona=None
    
    def __init__(self, un_nombre, una_edad):
        self.nombre_persona = un_nombre
        self.edad_persona = una_edad
        print("Hola soy una persona y me llamo", self.nombre_persona,"y mi edad es", self.edad_persona)

yo = Persona("pepito", 25)