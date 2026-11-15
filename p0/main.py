import os, dotenv, sys
from google import genai

def main():
    api_key = carregar_configuracao()
    cliente = genai.Client(api_key=api_key)
    mensagem_aluno = capturar_entrada()
    texto_resumo = consultar_llm(cliente, mensagem_aluno)
    apresentar_resultado(texto_resumo)

def carregar_configuracao():
    dotenv.load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        sys.exit(1)
    print(f"Chave carregada: {api_key[:4]}****")
    return api_key

def capturar_entrada():
    print("Agora cole sua mensagem ou escreva e aperte Ctrl+D ao final")
    mensagem_aluno = sys.stdin.read()
    return mensagem_aluno


def consultar_llm(cliente, mensagem_aluno):
    prompt = f"Resuma a dúvida principal deste aluno de forma direta: {mensagem_aluno}"
    resposta = cliente.models.generate_content(model="gemini-3.5-flash", contents=prompt)
    return resposta.text

def apresentar_resultado(texto):
    print("RESUMO DA DÚVIDA")
    print(texto)


if __name__ == "__main__":
    main()
