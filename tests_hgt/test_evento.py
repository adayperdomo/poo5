import pytest
from hgt.evento import Evento

@pytest.fixture
def evento():
    return Evento(69, "Mundo", False,"2023-05-28", "10:00", "2023-05-29", "18:00")

def test_evento(evento):
    assert evento.read() == (69, "Mundo", False,"2023-05-28", "10:00", "2023-05-29", "18:00")

def test_read(evento):
    assert evento.read() == (69, "Mundo", False,"2023-05-28", "10:00", "2023-05-29", "18:00")

def test_update(evento):
    evento.update(69, "Mundo", False,"2023-05-28", "10:00", "2023-05-29", "18:00")
    assert evento.read() == (69, "Mundo", False,"2023-05-28", "10:00", "2023-05-29", "18:00")

def test_delete(evento):
    evento.delete()
    assert evento.read() == (None,None,None,None, None, None, None)