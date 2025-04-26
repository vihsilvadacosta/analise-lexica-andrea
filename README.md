# Analisador Léxico em Português com spaCy e Gradio

## Descrição
Este projeto realiza uma análise léxica de frases em português utilizando o modelo de linguagem `spaCy` e disponibiliza uma interface amigável com `Gradio`.  
O sistema identifica e traduz as classes gramaticais de cada palavra digitada.

## Principais Funcionalidades
- Tokenização de frases.
- Identificação das classes gramaticais (substantivos, verbos, adjetivos, etc.).
- Interface web simples para uso fácil (via Gradio).
- Tradução das siglas de POS para português.

## Instruções de Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/vihsilvadacosta/analise-lexica-andrea.git
   cd seu_repositorio
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Baixe o modelo de português do spaCy:
   ```bash
   python -m spacy download pt_core_news_sm
   ```

6. Execute o projeto:
   ```bash
   python app.py
   ```

## Autores
- Vitória Silva da Costa
- Suelen Araujo
