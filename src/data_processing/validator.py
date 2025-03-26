import pdfplumber
import os

# Verifica se a extensão do arquivo é .pdf
async def verificar_extensao_pdf(caminho_arquivo):
    try:
        _, extensao = os.path.splitext(caminho_arquivo)  # Obtém a extensão

        if not extensao:  # Se não tiver extensão
            raise ValueError("O arquivo não possui extensão!")

        if extensao.lower() == '.pdf':  # Compara corretamente
            print(f"✅ Extensão do arquivo é .pdf: {caminho_arquivo}")
            return True
        else:
            print(f"❌ Extensão inválida: {caminho_arquivo}")
            return False
    except Exception as e:
        print(f"❌ Erro ao verificar a extensão do arquivo: {e}")
        return False

# Verifica se o arquivo realmente é um PDF válido lendo os primeiros bytes
async def verificar_pdf_real(caminho_arquivo):
    try:
        # Tenta abrir o arquivo como um PDF
        with pdfplumber.open(caminho_arquivo) as doc:
            if doc.pages:  # Verifica se tem páginas
                print(f"✅ Arquivo PDF válido: {caminho_arquivo}")
                return True
            else:
                print(f"❌ O arquivo não contém páginas válidas: {caminho_arquivo}")
                return False
    except Exception as e:
        print(f"❌ Arquivo inválido ou corrompido: {caminho_arquivo} - Erro: {e}")
        return False

# Verifica se o arquivo é um PDF válido
async def verificar_arquivo_pdf(caminho_arquivo):
    if not await verificar_extensao_pdf(caminho_arquivo):
        return False
    return await verificar_pdf_real(caminho_arquivo)