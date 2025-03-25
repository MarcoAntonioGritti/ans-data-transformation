import os
from pdf_extraction.extractor import extrair_dados_pdf
from data_processing.transformer import substituir_abreviacoes
from storage.csv_handler import salvar_csv
from storage.zip_handler import compactar_arquivo
from data_processing.cleaner import excluir_arquivo_zip
from data_processing.validator import verificar_arquivo_pdf

def processar_pdf_para_zip(pdf_path: str, nome_arquivo_zip: str):
    try:
        # Passo 1: Excluir arquivo ZIP antigo
        excluir_arquivo_zip(nome_arquivo_zip)

        # Passo 2: Verificar se o arquivo é um PDF válido
        verificar_arquivo_pdf(pdf_path)

        # Passo 3: Extrair dados do PDF
        dados = extrair_dados_pdf(pdf_path)

        # Passo 4: Substituir abreviações
        df = substituir_abreviacoes(dados)
        
        # Passo 5: Salvar dados no formato CSV
        caminho_csv = "dados_extraidos.csv"
        salvar_csv(df.values.tolist(), caminho_csv)
        
        # Passo 6: Compactar o arquivo CSV
        compactar_arquivo(caminho_csv, nome_arquivo_zip)
        
        # Limpar arquivos temporários
        os.remove(caminho_csv)

        print(f"✅ Arquivo ZIP criado com sucesso: {nome_arquivo_zip}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    processar_pdf_para_zip("C:/Users/marco/Downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", "Teste_Marco_Antonio.zip")
