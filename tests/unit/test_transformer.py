import pytest
import pandas as pd
from src.data_processing import substituir_abreviacoes

# Teste para verificar se a função substitui corretamente as abreviações em um DataFrame
@pytest.mark.asyncio
async def test_substituir_abreviacoes_success():
    df = pd.DataFrame({
        'Tipo': ['OD', 'AMB', 'OD', 'AMB']  # Dados de entrada com abreviações
    })
    expected_df = pd.DataFrame({
        'Tipo': ['Seg. Odontológica', 'Seg. Ambulatorial', 'Seg. Odontológica', 'Seg. Ambulatorial']  # Resultado esperado
    })

    # Chama a função e verifica se o resultado é igual ao esperado
    result_df = await substituir_abreviacoes(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

# Teste para verificar o comportamento da função quando não há abreviações no DataFrame
@pytest.mark.asyncio
async def test_substituir_abreviacoes_no_abreviations():
    df = pd.DataFrame({
        'Tipo': ['Seg. Odontológica', 'Seg. Ambulatorial']  # Dados de entrada sem abreviações
    })
    expected_df = df.copy()  # O resultado esperado é o mesmo que o DataFrame de entrada

    # Chama a função e verifica se o resultado é igual ao esperado
    result_df = await substituir_abreviacoes(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

# Teste para verificar o comportamento da função com um DataFrame vazio
@pytest.mark.asyncio
async def test_substituir_abreviacoes_empty_dataframe():
    df = pd.DataFrame({'Tipo': []})  # DataFrame vazio
    expected_df = df.copy()  # O resultado esperado é também um DataFrame vazio

    # Chama a função e verifica se o resultado é igual ao esperado
    result_df = await substituir_abreviacoes(df)
    pd.testing.assert_frame_equal(result_df, expected_df)

# Teste para verificar o tratamento de exceções quando a entrada não é um DataFrame
@pytest.mark.asyncio
async def test_substituir_abreviacoes_exception_handling():
    df = "This is not a DataFrame"  # Entrada inválida

    # Verifica se a função retorna None ao receber uma entrada inválida
    result = await substituir_abreviacoes(df)
    assert result is None