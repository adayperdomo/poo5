import pytest

from hgt.alumnos.alumno import Alumno

@pytest.fixture
def alumno():
    return Alumno('Juan')

def test_alumno(alumno):
    assert alumno.read() == 'Juan'

def test_read(alumno):
    assert alumno.read() == 'Juan'

def test_update(alumno):
    alumno.update('Pedro')

    assert alumno.read() == 'Pedro'

def test_delete(alumno):
    alumno.delete()
    
    assert alumno.read() == None