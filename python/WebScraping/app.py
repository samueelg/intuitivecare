import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"  # Substitua pela URL real

ARQUIVOS = {
    "Anexo I": "Anexo I.pdf",
    "Anexo II": "Anexo II.pdf",
}


def baixar_arquivo(url, caminho_arquivo):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        with open(caminho_arquivo, "wb") as f:
            for chunk in resposta.iter_content(1024):
                f.write(chunk)
        print(f"Arquivo salvo: {caminho_arquivo}")
    else:
        print(f"Erro ao baixar {url}")


def encontrar_e_baixar_pdfs(pasta_destino):
    resposta = requests.get(URL)
    if resposta.status_code != 200:
        print("Erro ao acessar a página")
        return

    soup = BeautifulSoup(resposta.text, "html.parser")

    os.makedirs(pasta_destino, exist_ok=True)

    for link in soup.find_all("a", string=ARQUIVOS.keys()):
        nome_anexo = link.text.strip()
        href = link.get("href")
        if href:
            url_arquivo = urljoin(URL, href)
            caminho_arquivo = os.path.join(pasta_destino, ARQUIVOS[nome_anexo])
            baixar_arquivo(url_arquivo, caminho_arquivo)


def compactar_arquivos(pasta_destino):
    zip_file = os.path.join(pasta_destino, "anexos.zip")
    with zipfile.ZipFile(zip_file, "w") as zipf:
        for arquivo in ARQUIVOS.values():
            caminho_arquivo = os.path.join(pasta_destino, arquivo)
            if os.path.exists(caminho_arquivo):
                zipf.write(caminho_arquivo, arquivo)
                print(f"Adicionado ao ZIP: {arquivo}")

    print(f"Arquivo ZIP criado: {zip_file}")


if __name__ == "__main__":
    pasta_destino = input("Digite o diretório onde deseja salvar os arquivos: ").strip()

    if not os.path.isdir(pasta_destino):
        print("Diretório inválido. Criando o diretório...")
        os.makedirs(pasta_destino, exist_ok=True)

    encontrar_e_baixar_pdfs(pasta_destino)
    compactar_arquivos(pasta_destino)
