import os, dotenv, sys, logging
from google import genai

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def main():
    logging.info("Iniciando o sistema de resumo...")
    api_key, modelo = carregar_configuracao()
    cliente = genai.Client(api_key=api_key)
    mensagem_aluno = capturar_entrada()
    texto_resumo = consultar_llm(cliente, mensagem_aluno, modelo)
    apresentar_resultado(texto_resumo)
    logging.info("Resumo gerado com sucesso.")

def carregar_configuracao():
    dotenv.load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        sys.exit(1)
    modelo = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    logging.info(f"Chave carregada com sucesso: {api_key[:4]}**** usando modelo {modelo}")
    return api_key, modelo

def capturar_entrada():
    print("Agora cole sua mensagem ou escreva e aperte Ctrl+D ao final")
    mensagem_aluno = sys.stdin.read()
    return mensagem_aluno


def consultar_llm(cliente, mensagem_aluno, modelo):
    prompt = f"Resuma a dúvida principal deste aluno de forma direta: {mensagem_aluno}"
    logging.info(f"Enviando texto de {len(mensagem_aluno)} caracteres para o LLM...")
    resposta = cliente.models.generate_content(model=modelo, contents=prompt)
    return resposta.text

def apresentar_resultado(texto):
    print("RESUMO DA DÚVIDA")
    print(texto)


if __name__ == "__main__":
    main()
