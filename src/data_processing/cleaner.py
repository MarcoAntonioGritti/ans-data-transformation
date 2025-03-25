import os

def excluir_arquivo_zip(nome_arquivo_zip):
    try:
        if os.path.exists(nome_arquivo_zip):
            os.remove(nome_arquivo_zip)
            print(f"🗑️ Arquivo removido: {nome_arquivo_zip}")
    except Exception as e:
        print(f"Erro ao tentar remover o arquivo {nome_arquivo_zip}: {e}")