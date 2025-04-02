# Web Scraper de PDFs ANS (Python)

## Descrição
Este script em Python realiza Web Scraping no site da *Agência Nacional de Saúde Suplementar* para localizar e baixar os documentos em PDF "Anexo I" e "Anexo II". Após o download, os arquivos são compactados em um arquivo ZIP no diretório especificado pelo usuário.

## Tecnologias Utilizadas
* Python
* BeautifulSoup
* Módulos nativos `os` e `zipfile` para manipulação de arquivos

## Estrutura do Script

### **1. Configuração Inicial**
* Define a URL da página da ANS contendo os PDFs.
* Mapeia os arquivos de interesse ("Anexo I" e "Anexo II") para seus respectivos nomes de download.

### **2. Função `baixar_arquivo(url, caminho_arquivo)`**
* Realiza o download de um arquivo PDF a partir da URL informada.
* Salva o arquivo localmente no diretório especificado.

### **3. Função `encontrar_e_baixar_pdfs(pasta_destino)`**
* Acessa a página da ANS e analisa seu conteúdo HTML.
* Busca os links que correspondem aos arquivos "Anexo I" e "Anexo II".
* Faz o download dos arquivos encontrados para o diretório indicado.

### **4. Função `compactar_arquivos(pasta_destino)`**
* Verifica se os arquivos foram baixados com sucesso.
* Compacta os PDFs em um arquivo `anexos.zip` dentro do diretório destino.

## Como Executar
1. Instale as dependências necessárias:
   ```sh
   pip install requests beautifulsoup4
    ```
