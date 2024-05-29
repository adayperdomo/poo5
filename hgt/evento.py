from hgt.tarea import Tarea

class Evento(Tarea):
    def __init__(self,id:int, tarea:str, estado:bool, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        super().__init__(id, tarea, estado)
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.hora = horaFin

    #Métodos CRUD
    def read(self):
        return super().read(),self.fechaInicio,self.horaInicio,self.fechaFin,self.hora

    def update(self, fechaInicio1, horaInicio1, fechaFin1, hora1):
        super().update()
        self.fechaInicio1 = fechaInicio1
        self.horaInicio1 = horaInicio1
        self.fechaFin1 = fechaFin1
        self.hora1 = hora1

    def delete(self):
        super().delete()
        self.fechaInicio = None
        self.horaInicio = None
        self.fechaFin = None
        self.fechaFin = None