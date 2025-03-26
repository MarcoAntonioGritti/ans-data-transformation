import pdfplumber
import pandas as pd

# Extraí os dados do PDF e organiza em formato estruturado.
async def extrair_dados_pdf(pdf_path):
    dados = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Iterar sobre as páginas do PDF
            for page in pdf.pages:
                # Extrair tabela da página
                tabela = page.extract_table()

                # Adicionar cada linha da tabela à lista de dados
                if tabela:
                    for row in tabela:
                        dados.append(row)

        # Criar o DataFrame com as linhas extraídas e colunas definidas
        colunas = ["PROCEDIMENTO", "RN", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]
        df = pd.DataFrame(dados, columns=colunas)

        print("✅ Dados extraídos com sucesso!")

        return df

    except Exception as e:
        print(f"❌ Ocorreu um erro ao extrair dados do PDF: {e}")
        return None