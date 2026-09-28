import pytest
from src.validators.validators import (
    validar_entero_positivo,
    validar_fechas,
    validar_email
)

def test_validar_entero_positivo_valido():
    assert validar_entero_positivo(5, "campo") == 5
    assert validar_entero_positivo(10, "campo") == 10

def test_validar_entero_positivo_invalido():
    with pytest.raises(ValueError):
        validar_entero_positivo(-1, "campo")
    with pytest.raises(ValueError):
        validar_entero_positivo("10", "campo")
    with pytest.raises(ValueError):
        validar_entero_positivo("abc", "campo")
    with pytest.raises(ValueError):
        validar_entero_positivo(True, "campo")

def test_validar_email_valido():
    assert validar_email("test@club.com") == "test@club.com"

def test_validar_email_invalido():
    with pytest.raises(ValueError):
        validar_email("email-invalido")

def test_validar_fechas_calculo_horas():
    inicio = "2026-11-15 18:00:00"
    fin = "2026-11-15 20:00:00"
    horas = validar_fechas(inicio, fin)
    assert horas == 2

def test_validar_fechas_fin_anterior_a_inicio():
    inicio = "2026-11-15 20:00:00"
    fin = "2026-11-15 18:00:00"
    with pytest.raises(ValueError):
        validar_fechas(inicio, fin)