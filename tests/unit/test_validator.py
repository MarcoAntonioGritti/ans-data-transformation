import pytest
import pdfplumber
from src.data_processing import verificar_pdf_real

# Teste para verificar se a função `verificar_pdf_real` retorna True para um PDF válido
@pytest.mark.asyncio
async def test_verificar_pdf_real_valid_pdf(mocker):
    caminho_arquivo = "valid.pdf"
    
    # Mockando pdfplumber.open para simular um PDF válido com páginas
    mock_open = mocker.patch("pdfplumber.open")
    mock_open.return_value.__enter__.return_value.pages = [mocker.Mock()]
    
    # Chamando a função e verificando se o resultado é True
    result = await verificar_pdf_real(caminho_arquivo)
    assert result == True

# Teste para verificar se a função `verificar_pdf_real` retorna False para um PDF sem páginas
@pytest.mark.asyncio
async def test_verificar_pdf_real_invalid_pdf_no_pages(mocker):
    caminho_arquivo = "invalid_no_pages.pdf"
    
    # Mockando pdfplumber.open para simular um PDF sem páginas
    mock_open = mocker.patch("pdfplumber.open")
    mock_open.return_value.__enter__.return_value.pages = []
    
    # Chamando a função e verificando se o resultado é False
    result = await verificar_pdf_real(caminho_arquivo)
    assert result == False

# Teste para verificar se a função `verificar_pdf_real` retorna False para um PDF corrompido
@pytest.mark.asyncio
async def test_verificar_pdf_real_corrupted_pdf(mocker):
    caminho_arquivo = "corrupted.pdf"
    
    # Mockando pdfplumber.open para lançar uma exceção simulando um arquivo corrompido
    mocker.patch("pdfplumber.open", side_effect=Exception("Corrupted file"))
    
    # Chamando a função e verificando se o resultado é False
    result = await verificar_pdf_real(caminho_arquivo)
    assert result == False