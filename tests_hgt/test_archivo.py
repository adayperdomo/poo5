from hgt.listaTareas import ListaTareas
from hgt.archivo import Archivo
import pytest
import os

NOMBREARCHIVO = "archivo.txt"
INFO = (69, "Mundo", False) + ListaTareas.LIMITCHAR + (96, "Planeta", True)

@pytest.fixture
def archivo():
    return Archivo(NOMBREARCHIVO)

def test_ficheroLeer(archivo):
    os.remove(NOMBREARCHIVO)
    assert archivo.leer() == ""

def test_archivoLeer2(archivo):
    assert archivo.leer() == INFO

def test_archivoEscribir(archivo):
    assert archivo.escribir(INFO) == True

def test_archivoListaTarea(archivo):
    lista = ListaTareas()
    lista.load(archivo.leer())
    assert lista.read() == INFO