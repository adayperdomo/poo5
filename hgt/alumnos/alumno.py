class Alumno:
    def __init__(self, nombre:str)->None:
        self.nombre = nombre

    # crud methods

    def read(self)->str:
        return self.nombre

    def update(self, nombre)->None:
        self.nombre = nombre
        
    def delete(self):
        self.nombre = None