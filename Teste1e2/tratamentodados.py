import pdfplumber
import pandas as pd 
import zipfile


pdf_path = "pdfs_anexo/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Extraindo os dados do pdf
tabelas = []

with pdfplumber.open(pdf_path) as pdf:
    for pagina in pdf.pages:
        tabela = pagina.extract_table()
        if tabela:
            tabelas.append(tabela)

todas_linhas = []


for tabela in tabelas:
    for linha in tabela:
        todas_linhas.append(linha)


colunas = todas_linhas[0]
dados = todas_linhas[1:]

# DataFrame com o resultado
df = pd.DataFrame(dados, columns=colunas)
print(df.head())

csv_path = "Teste_Bruno.csv"
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

print(f"arquivo salvo em: {csv_path}")

# Zipando o arquivo

zip_filename = "Teste_Bruno.zip"


with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_path)

print (f"Arquivo zipado com sucesso: {zip_filename}")

df = pd.read_csv("Teste_Bruno.csv")

df["OD"] = df["OD"].replace("OD", "Odontologia")
df["AMB"] = df["AMB"].replace("AMB", "Ambulatorial")

csv_atualizado = "Teste_Bruno_atualizado.csv"
df.to_csv(csv_atualizado, index=False)
print(f"Arquivo atualizado e salvo como: {csv_atualizado}")

zip_name = "Teste_Bruno_atualizado.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    zipf.write(csv_atualizado)
print(f"Arquivo zipado: {zip_name}")

