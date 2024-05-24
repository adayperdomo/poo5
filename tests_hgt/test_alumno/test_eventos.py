import pytest
from hgt.evento import Evento

@pytest.fixture
def evento():
    return Evento("24/05/2024", "18/06/2024", "23:59", "14:00")

def test_evento(evento):
    assert evento.read() == ("24/05/2024", "18/06/2024", "23:59", "14:00")

def test_read(evento):
    assert evento.read() == ("24/05/2024", "18/06/2024", "23:59", "14:00")

def test_update(evento):
    evento.update("24/05/2024", "18/06/2024", "23:59", "14:00")

    assert evento.read() == ("24/05/2024", "18/06/2024", "23:59", "14:00")

def test_delete(evento):
    evento.delete()

    assert evento.read() == ("24/05/2024", "18/06/2024", "23:59", "14:00")