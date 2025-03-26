import os
import pandas as pd
import pytest
from src.storage import salvar_csv

# Fixture para fornecer dados de exemplo para os testes
@pytest.fixture
def sample_data():
    return [
        ["col1", "col2", "col3"],  # Linha de cabeçalho
        [1, 2, 3],                # Primeira linha de dados
        [4, 5, 6],                # Segunda linha de dados
        [7, 8, 9]                 # Terceira linha de dados
    ]

# Teste para verificar se a função salvar_csv cria um arquivo no caminho especificado
def test_salvar_csv_creates_file(sample_data, tmp_path):
    caminho_arquivo = tmp_path / "output.csv"  # Caminho temporário para o arquivo
    salvar_csv(sample_data, str(caminho_arquivo))  # Chama a função para salvar o CSV
    assert os.path.exists(caminho_arquivo)  # Verifica se o arquivo foi criado

# Teste para verificar o conteúdo do arquivo CSV criado pela função salvar_csv
def test_salvar_csv_content(sample_data, tmp_path):
    caminho_arquivo = tmp_path / "output.csv"  # Caminho temporário para o arquivo
    salvar_csv(sample_data, str(caminho_arquivo))  # Chama a função para salvar o CSV
    df = pd.read_csv(caminho_arquivo)  # Lê o arquivo CSV em um DataFrame
    assert df.shape == (3, 3)  # Verifica se o DataFrame tem 3 linhas e 3 colunas
    assert list(df.columns) == sample_data[0]  # Verifica se o cabeçalho corresponde aos dados de exemplo
    assert df.iloc[0].tolist() == sample_data[1]  # Verifica se a primeira linha corresponde aos dados de exemplo

# Teste para mockar o método pandas DataFrame.to_csv e verificar se ele é chamado corretamente
def test_salvar_csv_mocked(mocker, sample_data):
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")  # Mocka o método to_csv
    salvar_csv(sample_data, "mocked_path.csv")  # Chama a função com um caminho mockado
    mock_to_csv.assert_called_once_with("mocked_path.csv", index=False)  # Verifica se o método foi chamado uma vez com os argumentos corretos