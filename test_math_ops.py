import pytest
from math_ops import suma, resta, multiplica, divide, suma_lista

@pytest.mark.parametrize("func, a, b, esperado", [
    (suma,        2,  3,  5),
    (resta,       5,  2,  3),
    (multiplica,  4,  3, 12),
    (divide,     10,  2,  5),
])
def test_operaciones_basicas(func, a, b, esperado):
    assert func(a, b) == esperado

def test_divide_por_cero():
    with pytest.raises(ValueError) as excinfo:
        divide(3, 0)
    assert "No se puede dividir por cero" in str(excinfo.value)

@pytest.fixture
def lista_numeros():
    return [1, 2, 3, 4, 5]

def test_suma_lista(lista_numeros):
    assert suma_lista(lista_numeros) == 15
