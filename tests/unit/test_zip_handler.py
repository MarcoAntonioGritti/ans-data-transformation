import os
import zipfile
import pytest
from src.storage import compactar_arquivo

# Fixture para simular o comportamento do módulo zipfile.ZipFile
@pytest.fixture
def mock_zipfile(mocker):
    return mocker.patch("src.storage.zip_handler.zipfile.ZipFile")

# Fixture para simular o comportamento da função os.path.basename
@pytest.fixture
def mock_os_basename(mocker):
    return mocker.patch("src.storage.zip_handler.os.path.basename")

# Teste para verificar se a função compactar_arquivo cria um arquivo ZIP corretamente
def test_compactar_arquivo_creates_zip(mock_zipfile, mock_os_basename):
    # Arrange: Configura os valores de entrada e o comportamento simulado
    csv_path = "test.csv"  # Caminho do arquivo CSV
    nome_zip = "test.zip"  # Nome do arquivo ZIP a ser criado
    mock_os_basename.return_value = "test.csv"  # Simula o retorno de os.path.basename

    # Act: Chama a função compactar_arquivo
    compactar_arquivo(csv_path, nome_zip)

    # Assert: Verifica se o arquivo ZIP foi criado e o arquivo CSV foi adicionado corretamente
    mock_zipfile.assert_called_once_with(nome_zip, 'w', zipfile.ZIP_DEFLATED)
    mock_zipfile.return_value.__enter__.return_value.write.assert_called_once_with(csv_path, "test.csv")

# Teste para verificar o comportamento da função compactar_arquivo com um caminho de arquivo vazio
def test_compactar_arquivo_handles_empty_file(mock_zipfile, mock_os_basename):
    # Arrange: Configura os valores de entrada e o comportamento simulado
    csv_path = ""  # Caminho vazio do arquivo CSV
    nome_zip = "empty.zip"  # Nome do arquivo ZIP a ser criado
    mock_os_basename.return_value = ""  # Simula o retorno de os.path.basename como vazio

    # Act: Chama a função compactar_arquivo
    compactar_arquivo(csv_path, nome_zip)

    # Assert: Verifica se o arquivo ZIP foi criado e o comportamento com o caminho vazio
    mock_zipfile.assert_called_once_with(nome_zip, 'w', zipfile.ZIP_DEFLATED)
    mock_zipfile.return_value.__enter__.return_value.write.assert_called_once_with(csv_path, "")