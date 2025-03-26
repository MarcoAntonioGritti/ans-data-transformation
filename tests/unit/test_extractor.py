import pytest
import pandas as pd
from unittest.mock import MagicMock
from src.pdf_extraction import extrair_dados_pdf

expected_data = {
        "PROCEDIMENTO": ["PROC1", "PROC2"],
        "RN": ["RN1", "RN2"],
        "VIGÊNCIA": ["2023-01-01", "2023-01-02"],
        "OD": ["OD1", "OD2"],
        "AMB": ["AMB1", "AMB2"],
        "HCO": ["HCO1", "HCO2"],
        "HSO": ["HSO1", "HSO2"],
        "REF": ["REF1", "REF2"],
        "PAC": ["PAC1", "PAC2"],
        "DUT": ["DUT1", "DUT2"],
        "SUBGRUPO": ["SUB1", "SUB2"],
        "GRUPO": ["GRP1", "GRP2"],
        "CAPÍTULO": ["CAP1", "CAP2"],
    }

@pytest.mark.asyncio
async def test_extrair_dados_pdf_multiple_pages(mocker):
    # Mocka o comportamento do pdfplumber para simular um PDF com múltiplas páginas
    mock_pdfplumber_open = mocker.patch("src.pdf_extraction.extractor.pdfplumber.open")
    mock_page1 = MagicMock()
    # Define a tabela extraída da primeira página
    mock_page1.extract_table.return_value = [
        ["PROC1", "RN1", "2023-01-01", "OD1", "AMB1", "HCO1", "HSO1", "REF1", "PAC1", "DUT1", "SUB1", "GRP1", "CAP1"]
    ]
    mock_page2 = MagicMock()
    # Define a tabela extraída da segunda página
    mock_page2.extract_table.return_value = [
        ["PROC2", "RN2", "2023-01-02", "OD2", "AMB2", "HCO2", "HSO2", "REF2", "PAC2", "DUT2", "SUB2", "GRP2", "CAP2"]
    ]
    # Simula as páginas do PDF
    mock_pdfplumber_open.return_value.__enter__.return_value.pages = [mock_page1, mock_page2]

    # Chama a função a ser testada
    pdf_path = "dummy_path.pdf"
    result = await extrair_dados_pdf(pdf_path)

    # Define o DataFrame esperado
    expected_data = {
        "PROCEDIMENTO": ["PROC1", "PROC2"],
        "RN": ["RN1", "RN2"],
        "VIGÊNCIA": ["2023-01-01", "2023-01-02"],
        "OD": ["OD1", "OD2"],
        "AMB": ["AMB1", "AMB2"],
        "HCO": ["HCO1", "HCO2"],
        "HSO": ["HSO1", "HSO2"],
        "REF": ["REF1", "REF2"],
        "PAC": ["PAC1", "PAC2"],
        "DUT": ["DUT1", "DUT2"],
        "SUBGRUPO": ["SUB1", "SUB2"],
        "GRUPO": ["GRP1", "GRP2"],
        "CAPÍTULO": ["CAP1", "CAP2"],
    }
    expected_df = pd.DataFrame(expected_data)

    # Verifica se o resultado é igual ao esperado
    pd.testing.assert_frame_equal(result, expected_df)
    # Verifica se o método pdfplumber.open foi chamado corretamente
    mock_pdfplumber_open.assert_called_once_with(pdf_path)
    # Verifica se as tabelas foram extraídas das páginas
    assert mock_page1.extract_table.called
    assert mock_page2.extract_table.called

@pytest.mark.asyncio
async def test_extrair_dados_pdf_empty_pdf(mocker):
    # Mocka o comportamento do pdfplumber para simular um PDF vazio
    mock_pdfplumber_open = mocker.patch("src.pdf_extraction.extractor.pdfplumber.open")
    # Simula um PDF sem páginas
    mock_pdfplumber_open.return_value.__enter__.return_value.pages = []

    # Chama a função a ser testada
    pdf_path = "dummy_path.pdf"
    result = await extrair_dados_pdf(pdf_path)

    # Define o DataFrame esperado para um PDF vazio
    expected_df = pd.DataFrame(columns=["PROCEDIMENTO", "RN", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"])

    # Verifica se o resultado é igual ao esperado
    pd.testing.assert_frame_equal(result, expected_df)
    # Verifica se o método pdfplumber.open foi chamado corretamente
    mock_pdfplumber_open.assert_called_once_with(pdf_path)

@pytest.mark.asyncio
async def test_extrair_dados_pdf_partial_table(mocker):
    # Mocka o comportamento do pdfplumber para simular um PDF com uma tabela parcialmente preenchida
    mock_pdfplumber_open = mocker.patch("src.pdf_extraction.extractor.pdfplumber.open")
    mock_page = MagicMock()
    # Define a tabela extraída com valores ausentes
    mock_page.extract_table.return_value = [
        ["PROC1", "RN1", "2023-01-01", "OD1", None, "HCO1", "HSO1", "REF1", "PAC1", "DUT1", "SUB1", "GRP1", "CAP1"]
    ]
    # Simula uma única página no PDF
    mock_pdfplumber_open.return_value.__enter__.return_value.pages = [mock_page]

    # Chama a função a ser testada
    pdf_path = "dummy_path.pdf"
    result = await extrair_dados_pdf(pdf_path)

    # Define o DataFrame esperado para a tabela parcialmente preenchida
    expected_data = {
        "PROCEDIMENTO": ["PROC1"],
        "RN": ["RN1"],
        "VIGÊNCIA": ["2023-01-01"],
        "OD": ["OD1"],
        "AMB": [None],
        "HCO": ["HCO1"],
        "HSO": ["HSO1"],
        "REF": ["REF1"],
        "PAC": ["PAC1"],
        "DUT": ["DUT1"],
        "SUBGRUPO": ["SUB1"],
        "GRUPO": ["GRP1"],
        "CAPÍTULO": ["CAP1"],
    }
    expected_df = pd.DataFrame(expected_data)

    # Verifica se o resultado é igual ao esperado
    pd.testing.assert_frame_equal(result, expected_df)
    # Verifica se o método pdfplumber.open foi chamado corretamente
    mock_pdfplumber_open.assert_called_once_with(pdf_path)
    # Verifica se a tabela foi extraída da página
    mock_page.extract_table.assert_called_once()