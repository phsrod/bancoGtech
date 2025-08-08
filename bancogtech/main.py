# import mysql.connector
# from bd.db_config import db_config
# from mysql.connector import Error


# #testes de conexão
# def connect_to_database():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         if conn.is_connected():
#             print("Conectado ao banco de dados com sucesso!")
#             return conn
#     except Error as e:
#         print(f"Erro ao conectar ao banco de dados: {e}")
#         return None

# if __name__ == "__main__":
#     connect_to_database()


# if __name__ == "__main__":

import funcoes
from classe.banco import Banco

def main():
    banco = Banco()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Criar nova conta")
        print("2. Autenticar conta")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            funcoes.cadastrar_nova_conta()
        elif opcao == "2":
            numero_conta = funcoes.autenticar_conta()
            if numero_conta:
                conta_logada = numero_conta
                print(f"Conta {conta_logada} autenticada com sucesso!")
                # Aqui você poderia abrir um menu para transações bancárias
            else:
                print("Falha na autenticação.")
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


