class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def read(self) -> str:
        return self.nombre
    
    def update(self, nombre) -> str:
        return self.nombre == nombre

    def delete(self) -> str:
        return self.nombre == None