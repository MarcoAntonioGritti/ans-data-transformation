import pytest
import aiohttp
from src.pdf_extraction import baixar_pdf
import asyncio

# Teste para verificar o comportamento da função baixar_pdf com uma URL inválida
@pytest.mark.asyncio
async def test_baixar_pdf_invalid_url(mocker):
    url = "invalid-url"
    caminho_arquivo = "test.pdf"

    # Mock aiohttp.ClientSession para simular um erro de URL inválida
    mocker.patch("aiohttp.ClientSession.get", side_effect=aiohttp.InvalidURL("Invalid URL"))

    # Chama a função com a URL inválida
    result = await baixar_pdf(url, caminho_arquivo)

    # Verifica se o resultado é False
    assert result is False

# Teste para verificar o comportamento da função baixar_pdf em caso de erro de conexão
@pytest.mark.asyncio
async def test_baixar_pdf_connection_error(mocker):
    url = "http://example.com/test.pdf"
    caminho_arquivo = "test.pdf"

    # Mock aiohttp.ClientSession para simular um erro de conexão
    mocker.patch("aiohttp.ClientSession.get", side_effect=aiohttp.ClientConnectionError("Connection error"))

    # Chama a função com uma URL que gera erro de conexão
    result = await baixar_pdf(url, caminho_arquivo)

    # Verifica se o resultado é False
    assert result is False

# Teste para verificar o comportamento da função baixar_pdf em caso de erro de timeout
@pytest.mark.asyncio
async def test_baixar_pdf_timeout_error(mocker):
    url = "http://example.com/test.pdf"
    caminho_arquivo = "test.pdf"

    # Mock aiohttp.ClientSession para simular um erro de timeout
    mocker.patch("aiohttp.ClientSession.get", side_effect=asyncio.TimeoutError("Timeout error"))

    # Chama a função com uma URL que gera erro de timeout
    result = await baixar_pdf(url, caminho_arquivo)

    # Verifica se o resultado é False
    assert result is False

# Teste para verificar o comportamento da função baixar_pdf quando a resposta é vazia
@pytest.mark.asyncio
async def test_baixar_pdf_empty_response(mocker):
    url = "http://example.com/test.pdf"
    caminho_arquivo = "test.pdf"

    # Mock aiohttp.ClientSession para retornar uma resposta vazia
    mock_response = mocker.AsyncMock()
    mock_response.__aenter__.return_value = mock_response
    mock_response.read.return_value = b""
    mock_response.raise_for_status = mocker.AsyncMock(return_value=None)


    mocker.patch("aiohttp.ClientSession.get", return_value=mock_response)

    # Mock open para simular a escrita em arquivo
    mocker.patch("builtins.open", mocker.mock_open())

    # Chama a função com uma URL que retorna resposta vazia
    result = await baixar_pdf(url, caminho_arquivo)

    # Verifica se o resultado é True (arquivo vazio ainda é considerado válido)
    assert result is True


# Teste para verificar o comportamento da função baixar_pdf quando o conteúdo é parcial
@pytest.mark.asyncio
async def test_baixar_pdf_partial_content(mocker):
    url = "http://example.com/test.pdf"
    caminho_arquivo = "test.pdf"
    partial_content = b"%PDF-1.4 partial content"

    # Mock aiohttp.ClientSession para retornar conteúdo parcial
    mock_response = mocker.AsyncMock()
    mock_response.__aenter__.return_value = mock_response
    mock_response.read.return_value = partial_content
    mock_response.raise_for_status = mocker.AsyncMock(return_value=None)
    mocker.patch("aiohttp.ClientSession.get", return_value=mock_response)

    # Mock open para simular a escrita em arquivo
    mocked_file = mocker.patch("builtins.open", mocker.mock_open())

    # Chama a função com uma URL que retorna conteúdo parcial
    result = await baixar_pdf(url, caminho_arquivo)

    # Verifica se o resultado é True e se o conteúdo foi escrito no arquivo
    assert result is True
    mocked_file().write.assert_called_once_with(partial_content)
