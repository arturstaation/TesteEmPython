from main import main
import pytest
from unittest.mock import MagicMock
from unittest import mock

@mock.patch('main.add')
def test_main_error(mock_add):
    mock_add.return_value = 5
    with pytest.raises(Exception, match="O resultado da adição não é o esperado."):
        main()

@pytest.fixture()
def mock_env(monkeypatch):
    monkeypatch.setenv("CHAMAR_ULTIMA_FUNCAO", True)


@mock.patch('main.addWithEnv')
@mock.patch('main.addWithException')
@mock.patch('main.add')
def test_main_2(mock_add, mock_add_with_exception, mock_add_with_env):
    mock_add.return_value = 8
    mock_add_with_exception.return_value = 8
    mock_add_with_env.return_value = 8
    main()
    assert mock_add_with_env.call_count  == 0

@mock.patch('main.addWithEnv')
@mock.patch('main.addWithException')
@mock.patch('main.add')
def test_main(mock_add, mock_add_with_exception,mock_add_with_env, mock_env):
    mock_add.return_value = 8
    mock_add_with_exception.return_value = 8
    mock_add_with_env.return_value = 8
    main()
    assert mock_add_with_env.call_count == 1
