import pandas as pd

# Responsavel por transformar os dados extraidos
async def substituir_abreviacoes(df: pd.DataFrame) -> pd.DataFrame:
    try:
        legendas = {
            'OD': 'Seg. Odontológica',
            'AMB': 'Seg. Ambulatorial'
        }

        df.replace(legendas, inplace=True)

        print("✅ Abreviações substituídas com sucesso!")

        return df
    except Exception as e:
        print(f"❌ Ocorreu um erro ao substituir abreviações: {e}")
        return None