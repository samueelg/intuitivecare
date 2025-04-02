# Web Scraper de PDFs

## Descrição

Esta pasta contem o exercicio em Java que realiza Web Scraping no site da Agência Nacional de Saúde Suplementar (ANS) para buscar documentos em PDF relacionados à atualização do rol de procedimentos. Ele baixa os arquivos "Anexo I" e "Anexo II", armazena-os em um diretório especificado pelo usuário e compacta os PDFs em um arquivo ZIP.

## Tecnologias Utilizadas
* Java 8+
* Biblioteca JSoup para extração dos links
* Classes nativas do Java para download de arquivos e compressão

## Estrutura do projeto

### 1. Main.java

Esta classe principal:
* Solicita ao usuário o diretório onde os arquivos serão salvos.
* Chama ```PdfDownloader``` para obter os links dos PDFs desejados.
* Usa ```FileDownloader``` para baixar os arquivos.
* Compacta os PDFs baixados com ```ZipCompressor```.

### 2. PdfDownloader.java

Responsável por:
* Acessar a URL da página.

* Encontrar e armazenar os links dos PDFs "Anexo I" e "Anexo II".

* Retornar uma lista com os links encontrados.

### 3. FileDownloader.java
* Baixa os arquivos PDF dos links fornecidos por ```PdfDownloader```.

* Salva os PDFs no diretório definido pelo usuário.

### 4. ZipCompressor.java

* Recebe a lista de arquivos baixados e os compacta em um arquivo ```Anexos.zip```.

* Utiliza ```ZipOutputStream``` para criar o arquivo ZIP.
