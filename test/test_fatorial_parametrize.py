from functions.src import fatorial
import pytest

@pytest.mark.parametrize('entrada, esperado', [(0, 1),(1, 1),(-10, 0),(4, 24),(5, 120)])

def test_fatorial(entrada, esperado):
    assert fatorial.fatorial(entrada) == esperado