import pandas as pd

#Ira salvar os dados extraidos em um arquivo csv
def salvar_csv(dados: list, caminho_arquivo: str):
    df = pd.DataFrame(dados[1:], columns=dados[0])  # A primeira linha é o cabeçalho
    df.to_csv(caminho_arquivo, index=False)