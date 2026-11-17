# Resumidor de Dúvidas de Alunos (Projeto P0)

## O Problema
Monitores e professores frequentemente recebem mensagens longas, confusas e com desabafos de alunos relatando erros de código, o que atrasa a identificação do problema técnico real (ex: mensagens enormes para dizer que ocorreu um `IndexError`).

## Público-Alvo
Professores, monitores e tutores de disciplinas de programação e exatas.

## Justificativa para utilizar um LLM
Um LLM é ideal para este problema devido à sua capacidade de Processamento de Linguagem Natural (PLN) para interpretar textos não estruturados, filtrar emoções/ruídos e sintetizar a intenção técnica (o erro ou dúvida central) de forma clara e direta.

## Funcionamento da Solução
A aplicação funciona via interface de linha de comando (CLI). O usuário executa o script, cola a mensagem do aluno e, ao finalizar a entrada, o sistema se comunica com a API do Google Gemini para retornar um resumo objetivo da dúvida técnica.

## Limites do Projeto e Limitações Conhecidas
- O programa roda apenas no terminal, sem interface gráfica.
- Depende de conexão ativa com a internet para chamar a API do Google.
- O modelo pode ocasionalmente alucinar se a mensagem não tiver nenhum contexto técnico, tentando forçar um resumo onde não há dúvida.

## Instalação e Preparação do Ambiente
```bash
# 1. Clone o repositório
git clone <link-do-seu-repositorio>

# 2. Crie um ambiente virtual e ative-o
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto (use o `.env.example` como base) e adicione suas chaves:

```env
GEMINI_API_KEY="sua_chave_de_api"
GEMINI_MODEL="gemini-1.5-flash"
```

## Execução e Exemplos

Para rodar a aplicação:

```bash
python main.py
```

**Exemplo de Entrada:**

> "Professor, pelo amor de Deus, me ajuda. Estou desde ontem tentando rodar o 'for' na minha lista de notas que tem 5 itens indo de 0 a 5, mas sempre dá IndexError na linha 15. Será que é vírus?"

**Exemplo de Saída:**

> INFO - Resumo gerado com sucesso.
> RESUMO DA DÚVIDA
> O aluno quer saber por que está recebendo um erro `IndexError` na linha 15 ao tentar iterar sobre uma lista de 5 itens usando um laço `for` de 0 a 5.

## Execução dos Testes

O projeto conta com testes automatizados utilizando `mock` para simular a chamada ao LLM sem consumir internet ou cota de API:

```bash
python test_main.py
```

## Link para o Vídeo

https://youtu.be/U4cJ-Znz2Uw
