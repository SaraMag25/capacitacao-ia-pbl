# Resumidor de Dúvidas e Mensagens de Alunos (P0)

CLI em Python que utiliza um LLM para transformar mensagens longas e informais de estudantes em um resumo estruturado com **dúvida central**, **urgência** e **ação esperada**.

## 1. Sobre o Projeto

### Definição do Problema

> Um professor, tutor ou monitor precisa transformar mensagens longas e informais de alunos em resumos estruturados (Dúvida central, Urgência e Ação esperada), porque atualmente enfrenta a dificuldade de as mensagens virem misturadas com desabafos e contexto irrelevante, o que inviabiliza o uso de regras fixas (Regex).

* **Problema:** Alto volume de mensagens longas e desestruturadas dificulta a triagem rápida de dúvidas acadêmicas.
* **Público-Alvo:** Professores, tutores e monitores.
* **Por que usar LLM:** Regras fixas ou `regex` não lidam bem com linguagem informal e desabafos; o LLM interpreta o contexto e extrai o ponto central com precisão.

## 2. Requisitos

* Python 3.10+
* Chave de API do Google Gemini (obtenha em [Google AI Studio](https://aistudio.google.com/apikey)), definida como `GEMINI_API_KEY` no arquivo `.env`
* Dependências principais: `google-genai` (SDK do Gemini) e `python-dotenv`. Versões exatas fixadas em `requirements.txt`

## 3. Instalação e Execução

```bash
# 1. Clonar e acessar a pasta
git clone https://github.com/SaraMag25/capacitacao-ia-pbl.git
cd capacitacao-ia-pbl/p0

# 2. Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências e configurar o .env
pip install -r requirements.txt
cp .env.example .env

# 4. Executar
python main.py
```
