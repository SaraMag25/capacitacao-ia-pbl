# Relatório de Execução - Projeto P0

## Evolução por Nível
- **Básico:** Criação do script monolítico (`main.py`) capaz de ler o arquivo `.env`, capturar texto com `sys.stdin.read()`, enviar a requisição para a API do Google Gemini e exibir a resposta.
- **Intermediário:** Refatoração do código. O bloco monolítico foi dividido em funções modulares com responsabilidades únicas (`carregar_configuracao`, `capturar_entrada`, `consultar_llm`, `apresentar_resultado`), governadas por uma função `main()`.
- **Avançado:** Implementação de configurações dinâmicas de modelo via `.env`, substituição de prints internos por `logging`, criação de um teste de software com dublê (`Mock`) em `test_main.py` e documentação técnica completa.

## Decisões Principais
1. **Uso do SDK `google-generativeai` vs. Requisições HTTP Diretas (`requests`)**
   - *Alternativa considerada:* Fazer chamadas POST diretas para a API REST do Google.
   - *Justificativa:* O uso do SDK oficial simplifica o código, lida automaticamente com a formatação JSON e facilita atualizações futuras na API, tornando a função `consultar_llm` mais limpa e legível.
2. **Uso de `unittest.mock` para testes**
   - *Alternativa considerada:* Fazer testes reais passando a chave da API.
   - *Justificativa:* Testes reais gastam internet, lentificam a esteira de testes e consomem a cota gratuita do serviço. O `MagicMock` isolou a lógica da função perfeitamente.

## Testes e Resultados
| Teste | Entrada ou situação | Resultado esperado | Resultado obtido |
| :--- | :--- | :--- | :--- |
| **Falta de API Key** | `.env` sem a variável `GEMINI_API_KEY` | Programa encerra (sys.exit) antes de chamar a IA | Sucesso (Programa encerrado) |
| **Resumo Padrão** | Texto prolixo sobre erro de `IndexError` | Resumo técnico extraindo o erro "IndexError no laço for" | Sucesso (Resumo extraído) |
| **Teste Local (Mock)** | Executar `test_main.py` (cliente simulado) | Resposta fictícia processada sem chamar internet | Sucesso (Teste passou: OK) |

## Falhas e Limitações
- **O que aconteceu:** Durante o Nível Intermediário, ao extrair o texto de resposta na refatoração, o programa quebrou informando que uma string não tinha o atributo `.text`.
- **Como foi identificado:** Pela mensagem de erro e traceback do interpretador Python apontando para a função `main()`.
- **Como foi tratado:** Ajustou-se a função `consultar_llm` para retornar diretamente `resposta.text`, e a função de apresentação passou a receber o texto puro, corrigindo a tipagem e isolando a responsabilidade de formatação.

## Uso de IA no desenvolvimento
- **Ferramenta utilizada:** Google Gemini.
- **Tarefa delegada:** Tutoramento e revisão de código em Pair Programming.
- **Resultado aproveitado:** Estratégia de refatoração para modularização (Intermediário) e arquitetura de injeção de dependência fictícia para o `MagicMock` (Avançado).
- **Correções realizadas:** O modelo apontou falhas sutis de escopo de variável (parâmetros vazios vs. preenchidos) durante a separação de funções, que foram corrigidas antes de rodar o código.
- **Forma de verificação:** Execução empírica no terminal local após cada sugestão do LLM.

## Reflexão Final
- **Principal aprendizado:** Entendimento claro sobre separação de responsabilidades (Clean Code) em Python e como variáveis transitam entre funções.
- **Competência mais desenvolvida:** C01 (entregar código compreensível e organizado) e C04 (permitir instalação reprodutível).
- **Aspecto a ser aprimorado:** Lidar melhor com tratamento de exceções (blocos `try/except`) para cenários onde a API do Google caia ou a internet falhe no meio da requisição.
