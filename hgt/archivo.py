class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        try:
            f = open(self.nombre, "rt")
        except FileNotFoundError:
            return ""
        with f:
            return f.readline()
        
    def escribir(self, info):
        try:
            w = open(self.nombre, "wt")
        except:
            raise Exception("Fallo")
        with w:
            w.write(info)
            return True