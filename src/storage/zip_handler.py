import zipfile
import os 

def compactar_arquivo(csv_path: str, nome_zip: str):
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))