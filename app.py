# Importação das bibliotecas necessárias
import spacy
import gradio as gr

# Carrega o modelo spaCy para a língua portuguesa
nlp = spacy.load("pt_core_news_sm")

# Dicionário para tradução das classes gramaticais para português
traducao_pos = {
    "ADJ": "Adjetivo",
    "ADP": "Preposição",
    "ADV": "Advérbio",
    "AUX": "Verbo auxiliar",
    "CCONJ": "Conjunção coordenativa",
    "DET": "Determinante",
    "INTJ": "Interjeição",
    "NOUN": "Substantivo",
    "NUM": "Número",
    "PART": "Partícula",
    "PRON": "Pronome",
    "PROPN": "Nome próprio",
    "PUNCT": "Pontuação",
    "SCONJ": "Conjunção subordinativa",
    "SYM": "Símbolo",
    "VERB": "Verbo",
    "X": "Outros"
}

# Função que realiza a análise léxica da frase
def analisar_frase(frase):
    doc = nlp(frase)
    resultado = "Token\t→ Classe gramatical\n"
    resultado += "-" * 30 + "\n"
    # Itera sobre cada token (palavra) na frase
    for token in doc:
        classe = traducao_pos.get(token.pos_, token.pos_)  # Traduz a classe, se possível
        resultado += f"{token.text}\t→ {classe}\n"
    return resultado

# Criação da interface gráfica usando Gradio
interface = gr.Interface(
    fn=analisar_frase,          # Função a ser chamada
    inputs="text",              # Tipo de entrada: texto
    outputs="text",             # Tipo de saída: texto
    title="Análise Léxica com spaCy (Português)",
    description="Digite uma frase em português para ver a análise léxica (tokens + classe gramatical)."
)

# Lançar a interface no navegador
interface.launch(share=True)
