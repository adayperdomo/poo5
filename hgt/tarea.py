class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id = id
        self.tarea = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self):
        return self.id,self.tarea,self.estado

    def update(self, id:int, tarea:str, estado:bool):
        self.id = id
        self.tarea = tarea
        self.stado = estado

    def delete(self):
        self.id = None
        self.tarea = None
        self.estado = None
