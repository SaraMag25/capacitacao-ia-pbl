import os, dotenv, sys
from google import genai

def main():
    api_key = carregar_configuracao()
    cliente = genai.Client(api_key=api_key)
    mensagem_aluno = capturar_entrada()
    prompt = f"Resuma a dúvida principal deste aluno de forma direta: {mensagem_aluno}"
    resposta = cliente.models.generate_content(model="gemini-3.5-flash", contents=prompt)
    print(resposta.text)




def carregar_configuracao():
    dotenv.load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        sys.exit(1)
    print(f"Chave carregada: {api_key[:4]}****")
    return api_key
    

if __name__ == "__main__":
    main()
