import aiohttp

async def baixar_pdf(url: str, caminho_arquivo: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Verifica se houve algum erro na requisição
                with open(caminho_arquivo, 'wb') as f:
                    f.write(await response.read())
        print(f"✅ PDF baixado com sucesso: {caminho_arquivo}")
    except Exception as e:
        print(f"❌ Ocorreu um erro ao baixar o PDF: {e}")
        return False
    return True