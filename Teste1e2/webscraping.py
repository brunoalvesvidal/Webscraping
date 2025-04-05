import requests
from bs4 import BeautifulSoup
import os
import shutil

url  = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

os.makedirs("pdfs_anexo", exist_ok= True)

response = requests.get(url)

# trasnformando html em formato legivel para o python
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
# encontrando os links
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if ("Anexo_I" in href or "Anexo_II" in href) and href.endswith('.pdf'):
            pdf_links.append(href)

    if pdf_links:
        for pdf in pdf_links:
            print("PDF encontrado:", pdf)
    else:
        print("Nenhum PDF encontrado.")

# extraindo o nome e baixando os pdfs
    for pdf_url in pdf_links:
        pdf_name = pdf_url.split("/")[-1]
        pdf_path = os.path.join("pdfs_anexo", pdf_name)

        print(f"Baixando: {pdf_url} -> {pdf_path}")
        pdf_response = requests.get(pdf_url)

        if pdf_response.status_code == 200:
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"Download concluido: {pdf_name}")
        else:
            print(f"Erro ao baixar {pdf_url}")

# compactando os arquivos
    zip_name = "pdfs_compactados"
    folder_path = "pdfs_anexo"

    shutil.make_archive(zip_name, 'zip', folder_path)
    print(f"Arquivo'{zip_name}.zip' criado com sucesso!")
    
else:
    print("Erro ao acessar a página:", response.status_code)

      


