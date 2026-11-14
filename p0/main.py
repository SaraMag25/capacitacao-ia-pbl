import os, dotenv, sys

def main():
    dotenv.load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        sys.exit(1)
    print(f"Chave carregada: {api_key[:4]}****")
    pass
    

if __name__ == "__main__":
    main()
