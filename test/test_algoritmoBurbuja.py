from src.algoritmoBurbuja import algoritmoBurbuja
import pytest

def test_algoritmoBurbuja():
  assert algoritmoBurbuja([28,4,255,1]) == [1, 4, 28, 255]