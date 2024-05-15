from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio, horaInicio, fechaFin, horaFin):
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.hora = horaFin

      #Métodos CRUD
    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass