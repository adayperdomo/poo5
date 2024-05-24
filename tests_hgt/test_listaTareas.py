from hgt.listaTareas import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTarea1(lista):
    lista.agregar('69,"Mundo",False')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('69, "Mundo", False')
    lista.agregar('96, "Planeta", True')

    assert len(lista) == 2

    assert lista[0] == ('69, "Mundo", False')
    assert lista[1] == ('96, "Planeta", True')

def test_listaTareaDelete(lista):
    lista.agregar('24, "roberto", False')
    assert lista[0] == ('24, "roberto", False')

    del lista[0]
    assert len(lista) == 0

    assert '24, "roberto", False' not in lista

def test_listaRead(lista):
    lista.agregar('69, "Mundo", False')
    lista.agregar('96, "Planeta", True')

    assert lista.read() == ('69, "Mundo", False') + lista.LIMITCHAR + ('96, "Planeta", True')
    assert len(lista) == 2

    assert lista[0] == ('69, "Mundo", False')
    assert lista[1] == ('96, "Planeta", True')