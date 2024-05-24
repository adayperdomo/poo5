from hgt.tarea import Tarea

class ListaTareas:
    LIMITCHAR = "|&&|"

    def __init__(self):
        self.tarea = []

    def agregar(self, tarea:Tarea):
        self.tarea.append(tarea)

    #CRUD
    def read(self):
        result = ""
        for tarea in self.tarea:
            result += tarea
            if tarea != self.tarea[-1]:
                result += self.LIMITCHAR

        return result
    
    def load(self, data:str):
        tarea = data.split(self.LIMITCHAR)
        for tarea in tarea:
            self.tarea.append(tarea)

    def update(self, tarea:Tarea, nombre:str):
        for x in self.tarea:
            if x == tarea:
                x.update(nombre)
                break

    def delete(self, tarea:Tarea):
        for x in self.tarea:
            if x == tarea:
                x.delete()
                break

    
    def __str__(self):
        return self.read()
    
    def __len__(self):
        return  self.tarea.__len__()
    
    def __getitem__(self, index):
        return self.tarea[index]
    
    def __setitem__(self, index, value):
        self.tarea[index] = value

    def __delitem__(self, index):
        del self.tarea[index]

    def __iter__(self):
        return self.tarea.__iter__()
    
    def __next__(self):
        return self.tarea.__next__()
    
    def __contains__(self, item):
        return item in self.tarea
    
    def __eq__(self, other):
        return self.tarea == other.tarea
    
    def __ne__(self, other):
        return self.tarea != other.tarea
  