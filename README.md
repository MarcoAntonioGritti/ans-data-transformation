
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
├── tests/
│   ├── test_main.py           # Testes para o fluxo principal
│   ├── test_baixar_pdf.py     # Testes para o método de download de PDF
│   ├── test_excluir_arquivo_zip.py
│   ├── test_verificar_arquivo_pdf.py
│   ├── test_extrair_dados_pdf.py
│   ├── test_substituir_abreviacoes.py
│   ├── test_salvar_csv.py
│   ├── test_compactar_arquivo.py
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

## 🧪 Como Executar os Testes

O projeto utiliza o framework `pytest` e `pytest-mock` para testes unitários e integração. Siga os passos abaixo para rodar os testes:

1. **Instale o pytest e pytest-mock** (caso ainda não esteja instalado):
   ```bash
   poetry add pytest pytest-mock
   ```

2. **Execute todos os testes**:
   ```bash
   pytest tests/
   ```

3. **Execute um teste específico**:
   ```bash
   pytest tests/unit/test_cleaner
   ```

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