# Conversor de PDF para CSV e Compactação em ZIP

## Descrição
Este script em Python extrai tabelas de um arquivo PDF e as converte para um arquivo CSV. Além disso, o script compacta o arquivo CSV gerado em um arquivo ZIP chamado `Teste_Samuel.zip`. Opcionalmente, o script permite a renomeação de colunas específicas no CSV gerado.

## Tecnologias Utilizadas
- Python
- Tabula para extração de tabelas de PDFs
- Pandas para manipulação de dados
- Módulos nativos ```os``` e ```zipfile``` para manipulação de arquivos

## Funcionalidades

### 1. Conversão de PDF para CSV (`convert_pdf_to_csv`)
- Verifica se o arquivo PDF existe.
- Extrai todas as tabelas do PDF e converte para um único arquivo ```.csv```
- Salva os dados extraídos em um arquivo CSV.
- Compacta o CSV gerado em um arquivo ZIP chamado ```Teste_Samuel.zip```.

### 2. Renomeação de Colunas (`rename_csv_columns`)
- Lê o arquivo CSV gerado.
- Substitui os nomes de colunas com base em um dicionário de mapeamento.
- Salva o arquivo CSV atualizado com os novos nomes de colunas.

## Como Executar
1. Instale as dependências necessárias:
   ```sh
   pip install tabula-py pandas
   ```
