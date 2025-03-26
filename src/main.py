import os
import asyncio
from src.pdf_extraction import extrair_dados_pdf,baixar_pdf
from src.data_processing import substituir_abreviacoes,excluir_arquivo_zip,verificar_arquivo_pdf
from src.storage import salvar_csv,compactar_arquivo

async def processar_pdf_para_zip(url_pdf: str, nome_arquivo_zip: str):
    pdf_path = "temp.pdf"  # Caminho temporário para salvar o PDF baixado
    try:
        # Passo 1: Baixar o PDF
        if not await baixar_pdf(url_pdf, pdf_path):
            return

        # Passo 2: Excluir arquivo ZIP antigo
        await excluir_arquivo_zip(nome_arquivo_zip)

        # Passo 3: Verificar se o arquivo é um PDF válido
        if not await verificar_arquivo_pdf(pdf_path):
            return

        # Passo 4: Extrair dados do PDF
        dados = await extrair_dados_pdf(pdf_path)
        if dados is None:
            return

        # Passo 5: Substituir abreviações
        df = await substituir_abreviacoes(dados)
        if df is None:
            return
        
        # Passo 6: Salvar dados no formato CSV
        caminho_csv = "dados_extraidos.csv"
        salvar_csv(df.values.tolist(), caminho_csv)
        
        # Passo 7: Compactar o arquivo CSV
        compactar_arquivo(caminho_csv, nome_arquivo_zip)
        
        # Limpar arquivos temporários
        os.remove(caminho_csv)
        os.remove(pdf_path)

        print(f"✅ Arquivo ZIP criado com sucesso: {nome_arquivo_zip}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    url_pdf = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    asyncio.run(processar_pdf_para_zip(url_pdf, "Teste_Marco_Antonio.zip"))