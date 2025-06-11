
import pytest
from mathCore import addWithEnv

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("VALOR1", "5")
    monkeypatch.setenv("VALOR2", "3")
def test_addWithEnv():
    result = addWithEnv()
    assert result == 8