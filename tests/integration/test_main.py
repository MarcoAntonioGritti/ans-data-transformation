import pytest
import os
from src.main import processar_pdf_para_zip

@pytest.mark.asyncio
async def test_processar_pdf_para_zip_integration():
    url_pdf = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    nome_arquivo_zip = "Teste_Integration.zip"

    # Executa o fluxo completo
    await processar_pdf_para_zip(url_pdf, nome_arquivo_zip)

    # Verifica se o arquivo ZIP foi criado
    assert os.path.exists(nome_arquivo_zip)

    # Limpa o arquivo gerado
    os.remove(nome_arquivo_zip)