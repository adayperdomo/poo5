class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id = id
        self.tarea = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self):
        return(f"id: {self.id}, tarea: {self.tarea}, estado: {self.estado}")

    def update(self, Aid:int, Atarea:str, Aestado:bool):
        self.Aid = Aid
        self.Atarea = Atarea
        self.Astado = Aestado

    def delete(self):
        del self.id
        del self.tarea
        del self.estado

ejemplo = Tarea(69, "Mundo", False)
ejemplo.read()
ejemplo.update()
ejemplo.delete()