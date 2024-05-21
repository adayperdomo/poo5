from alumno import Alumno

class ListaAlumnos:
    LIMITCHAR = "|&&|"

    def __init__(self):
        self.alumnos = []

    def agregar(self, alumno:Alumno):
        self.alumnos.append(alumno)

    def read(self):
        result = ""
        for alumno in self.alumnos:
            result += alumno
            if alumno != self.alumnos[-1]:
                result += self.LIMITCHAR

        return result
    
    def load(self, data:str):
        alumnos = data.split(self.LIMITCHAR)
        for alumno in alumnos:
            self.alumnos.append(alumno)
    
    def update(self, alumno:Alumno, nombre:str):
        for a in self.alumnos:
            if a == alumno:
                a.update(nombre)
                break

    def delete(self, alumno:Alumno):
        for a in self.alumnos:
            if a == alumno:
                a.delete()
                break

    def __str__(self):
        return self.read()
    
    def __len__(self):
        return  self.alumnos.__len__()
    
    def __getitem__(self, index):
        return self.alumnos[index]
    
    def __setitem__(self, index, value):
        self.alumnos[index] = value

    def __delitem__(self, index):
        del self.alumnos[index]

    def __iter__(self):
        return self.alumnos.__iter__()
    
    def __next__(self):
        return self.alumnos.__next__()
    
    def __contains__(self, item):
        return item in self.alumnos
    
    def __eq__(self, other):
        return self.alumnos == other.alumnos
    
    def __ne__(self, other):
        return self.alumnos != other.alumnos