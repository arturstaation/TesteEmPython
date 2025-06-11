from unittest import mock
from mathCore import addWithEnv
import pytest

@pytest.fixture()
def mock_env(monkeypatch):
    monkeypatch.setenv("VALOR1", "5")
    monkeypatch.setenv("VALOR2", "3")
def test_addWithEnv(mock_env):
    result = addWithEnv()
    assert result == 8