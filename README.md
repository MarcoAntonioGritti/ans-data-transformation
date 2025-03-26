# Projeto de Transformação de Dados - ANS

Este projeto foi desenvolvido para realizar a extração, transformação e armazenamento de dados contidos em arquivos PDF disponibilizados pela ANS (Agência Nacional de Saúde Suplementar). O objetivo é processar os dados de forma automatizada, gerando um arquivo compactado (ZIP) contendo os dados extraídos no formato CSV.

---

## 📋 Funcionalidades

1. **Download de PDF**: Faz o download do arquivo PDF a partir de uma URL.
2. **Validação de PDF**: Verifica se o arquivo baixado é um PDF válido.
3. **Extração de Dados**: Extrai os dados estruturados do PDF.
4. **Transformação de Dados**: Substitui abreviações e realiza ajustes nos dados extraídos.
5. **Armazenamento em CSV**: Salva os dados transformados em um arquivo CSV.
6. **Compactação**: Compacta o arquivo CSV em um arquivo ZIP.
7. **Limpeza**: Remove arquivos temporários após o processamento.

---

## 🛠️ Estrutura do Projeto

```
ans-data-transformation-test/
│
├── src/
│   ├── main.py                # Arquivo principal para execução do processo
│   ├── pdf_extraction/        # Módulo para download e extração de dados do PDF
│   ├── data_processing/       # Módulo para validação, transformação e limpeza de dados
│   ├── storage/               # Módulo para salvar e compactar arquivos
│
└── README.md                  # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python 3.13+** instalado.
- Gerenciador de pacotes `poetry`.
- Ambiente virtual configurado (recomendado).

### Passos para Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/ans-data-transformation-test.git
   cd ans-data-transformation-test
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   poetry install #Ira instalar as depenências
   source venv/bin/activate  # Linux/Mac
   ./.venv/Scripts/activate  # Windows
   ```
3. **Execute o script principal**:
   ```bash
   poetry run python -m src.main
   ```
---


---

## 📂 Detalhes dos Módulos

### `src/main.py`

Este é o arquivo principal que orquestra todo o fluxo de processamento. Ele realiza as seguintes etapas:
1. Baixa o PDF a partir de uma URL.
2. Valida o arquivo PDF.
3. Extrai os dados do PDF.
4. Realiza transformações nos dados.
5. Salva os dados em um arquivo CSV.
6. Compacta o CSV em um arquivo ZIP.
7. Remove arquivos temporários.

### Módulos Secundários

- **`pdf_extraction`**: Contém funções para download e extração de dados do PDF.
- **`data_processing`**: Contém funções para validação, transformação e limpeza de dados.
- **`storage`**: Contém funções para salvar dados em CSV e compactar arquivos.

---

## 📜 Exemplo de Uso

No arquivo `main.py`, você pode alterar a URL do PDF e o nome do arquivo ZIP gerado:

```python
if __name__ == "__main__":
    url_pdf = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    asyncio.run(processar_pdf_para_zip(url_pdf, "Teste_Marco_Antonio.zip"))
```

---

## 📖 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## 📞 Contato

- **Autor**: Marco Antônio
- **Email**: marco_gritti15@hotmail.com
- **LinkedIn**: (https://www.linkedin.com/in/marco-antonio-gritti-pazza-091938232/)
