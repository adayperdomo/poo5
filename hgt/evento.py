from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.hora = horaFin

    #Métodos CRUD
    def read(self):
        super().read(),self.fechaInicio,self.horaInicio,self.fechaFin,self.hora

    def update(self, fechaInicio1, horaInicio1, fechaFin1, hora1):
        super().update()
        self.fechaInicio1 = fechaInicio1
        self.horaInicio1 = horaInicio1
        self.fechaFin1 = fechaFin1
        self.hora1 = hora1

    def delete(self):
        super().update()
        del self.fechaInicio
        del self.horaInicio
        del self.fechaFin
        del self.fechaFin