import os
from colorama import Fore, Style

def welcome_message():
    welcome = """
__        __  _____   ____
\\ \\      / / | ____| | __ )
 \\ \\ /\\ / /  |  _|   |  _ \\
  \\ V  V /   | |___  | |_) |
   \\_/\\_/    |_____| |____/  By Lucifer 121 Ϟ
                    t.me/the121ofc Ϟ
    """
    print(f"{Fore.GREEN}{welcome}{Style.RESET_ALL}")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')  

    welcome_message()

    print("Digite o nome do seu arquivo em .txt:")
    nome_arquivo = input()

    print("Digite o login:")
    palavra_chave = input()

    with open(nome_arquivo, 'r') as arquivo_teste:
        quantidade_linhas = sum(1 for _ in arquivo_teste if palavra_chave in _)

    arquivo_saida = f"[{quantidade_linhas}]_{palavra_chave}.txt"

    try:
        with open(nome_arquivo, 'r') as arquivo_entrada, open(arquivo_saida, 'w') as arquivo_saida:
            linhas_encontradas = 0

            for linha in arquivo_entrada:
                if palavra_chave in linha:
                    linha_completa = linha.strip() + " by: CronosBot t.me/the121ofc \n"
                    arquivo_saida.write(linha_completa)
                    linhas_encontradas += 1

            print(f"\nForam encontrado {linhas_encontradas} logins.")

    except FileNotFoundError:
        print(f"{Fore.RED}Erro: ERROR.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erro inesperado: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
