import pytest
from src.data_processing import excluir_arquivo_zip

# Teste para verificar se o arquivo zip é excluído corretamente quando ele existe
@pytest.mark.asyncio
async def test_excluir_arquivo_zip_file_exists(mocker):
    nome_arquivo_zip = "test.zip"
    
    # Mock para simular que o arquivo existe
    mocker.patch("os.path.exists", return_value=True)
    # Mock para a função os.remove
    mock_remove = mocker.patch("os.remove")
    
    # Chama a função a ser testada
    await excluir_arquivo_zip(nome_arquivo_zip)
    # Verifica se a função os.remove foi chamada com o nome do arquivo
    mock_remove.assert_called_once_with(nome_arquivo_zip)

# Teste para verificar se nada acontece quando o arquivo zip não existe
@pytest.mark.asyncio
async def test_excluir_arquivo_zip_file_does_not_exist(mocker):
    nome_arquivo_zip = "test.zip"
    
    # Mock para simular que o arquivo não existe
    mocker.patch("os.path.exists", return_value=False)
    # Mock para a função os.remove
    mock_remove = mocker.patch("os.remove")
    
    # Chama a função a ser testada
    await excluir_arquivo_zip(nome_arquivo_zip)
    # Verifica se a função os.remove não foi chamada
    mock_remove.assert_not_called()

# Teste para verificar o comportamento da função quando ocorre uma exceção ao tentar excluir o arquivo
@pytest.mark.asyncio
async def test_excluir_arquivo_zip_exception(mocker):
    nome_arquivo_zip = "test.zip"
    
    # Mock para simular que o arquivo existe
    mocker.patch("os.path.exists", return_value=True)
    # Mock para a função os.remove que lança uma exceção
    mocker.patch("os.remove", side_effect=Exception("Mocked exception"))
    # Mock para a função print
    mock_print = mocker.patch("builtins.print")
    
    # Chama a função a ser testada
    await excluir_arquivo_zip(nome_arquivo_zip)
    # Verifica se a mensagem de erro foi exibida corretamente
    mock_print.assert_called_with(f"Erro ao tentar remover o arquivo {nome_arquivo_zip}: Mocked exception")
