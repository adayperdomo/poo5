import pytest

from hgt.tarea import Tarea

@pytest.fixture

def tarea():
    return Tarea(69, "Mundo", False)

def test_tarea(tarea):
    assert tarea.read() == (69, "Mundo", False)

def test_read(tarea):
    assert tarea.read() == (69, "Mundo", False)

def test_update(tarea):
    tarea.update(69, "Mundo", False)

    assert tarea.read() == (69, "Mundo", False)

def test_delete(tarea):
    tarea.delete()

    assert tarea.read() == (69, "Mundo", False)
