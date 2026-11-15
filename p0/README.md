# Resumidor de Dúvidas de Alunos (Projeto P0)

Este projeto é uma aplicação de linha de comando que utiliza a API do Google Gemini para extrair e resumir a dúvida principal em mensagens de alunos.

## Tecnologias Utilizadas
- **Python 3.10+**
- `google-generativeai`: Comunicação com o modelo de linguagem (LLM).
- `python-dotenv`: Gerenciamento seguro de variáveis de ambiente.

## Como preparar o ambiente (Ambiente Limpo)
Para garantir a reprodutibilidade, siga os passos abaixo para executar em um ambiente virtual limpo:

1. Clone este repositório.
2. Crie um ambiente virtual: 
   `python -m venv venv`
3. Ative o ambiente virtual:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Instale as dependências do projeto: 
   `pip install -r requirements.txt`

## Configuração
Crie um arquivo chamado `.env` na raiz do projeto e adicione as suas configurações:
```env
GEMINI_API_KEY="sua_chave_de_api_aqui"
GEMINI_MODEL="gemini-1.5-flash"
```

## Como Executar

Rode a aplicação principal no terminal:

```bash
python main.py
```

Cole a mensagem do aluno, pressione `Enter` e depois `Ctrl+D` para gerar o resumo.

## Testes Locais

Para executar o teste automatizado (mock) que valida a lógica interna sem consumir cota da API, execute:

```bash
python test_main.py
```
