# Teste Técnico – Estágio em Desenvolvimento

Este projeto é parte de um teste técnico para processo seletivo de estágio. Ele contempla tarefas relacionadas a extração, transformação e análise de dados, além da criação de API e interface de busca.

---

## ✅ Tarefas realizadas

### 🧩 1. Extração de arquivos PDF

- Os anexos em PDF foram localizados na página oficial da ANS:
  https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
- Utilizei Python com as bibliotecas `requests`, `BeautifulSoup` e `shutil` para baixar os arquivos.
- Os PDFs encontrados foram salvos em uma pasta local e compactados em um único arquivo `.zip`.

---

### 🔄 2. Transformação de Dados

#### 2.1 Extração dos dados do Anexo I
- Utilizei `pdfplumber` para extrair todas as páginas do PDF do Anexo I.

#### 2.2 Conversão para CSV
- Os dados extraídos foram transformados em um `DataFrame` com `pandas` e exportados como `.csv`.

#### 2.3 Compactação
- O CSV foi compactado como `Teste_Bruno.zip`.

#### 2.4 Substituição de abreviações
- As colunas "OD" e "AMB" foram substituídas por suas descrições completas com base na legenda do rodapé.
