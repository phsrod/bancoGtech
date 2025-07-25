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



from classe.pessoa import Pessoa
from classe.banco import Banco

def cadastrar_nova_conta():
    banco = Banco()

    print("=== Cadastro de nova conta ===")
    nome = input("Nome: ")
    cpf = input("CPF (apenas números): ")
    telefone = input("Telefone (11 dígitos): ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla, ex: SP): ")
    senha = input("Senha (6 dígitos numéricos): ")

    try:
        pessoa = Pessoa(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, cidade=cidade, estado=estado)
        numero_conta = banco.criar_conta(pessoa, senha)
        if numero_conta:
            print(f"Conta criada com sucesso! Número: {numero_conta}")
        else:
            print("Falha ao criar conta.")
    except Exception as e:
        print(f"Erro no cadastro: {e}")
    finally:
        banco.fechar_conexao()

if __name__ == "__main__":
    cadastrar_nova_conta()
