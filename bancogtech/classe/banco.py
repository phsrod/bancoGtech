import mysql.connector
from bd.db_config import db_config
from mysql.connector import Error
from classe.pessoa import Pessoa
import validations as validations

class Banco():
    def __init__(self):
        try: 
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor(dictionary=True)
            print("Conectado ao banco de dados com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None
            self.cursor = None

    
    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def executar_query(self, query, params=None):
        """
        Executa uma query SQL com parâmetros opcionais.
        Retorna os resultados no caso de SELECT.
        """
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
        except Error as e:
            print(f"Erro ao executar query: {e}")
            self.conn.rollback()
            return None
    
    def criar_conta(self, pessoa: Pessoa, senha: str):
        """
        Cria um cliente e uma conta associada no banco de dados.
        Retorna o número da nova conta ou None em caso de erro.
        """
        try:
            # Valida a senha (usando sua função no validations.py)
            if not validations.validar_senha(senha):
                raise ValueError("Senha inválida. Deve conter exatamente 6 dígitos numéricos.")

            # Verifica se cliente já existe pelo CPF
            consulta = "SELECT cpf FROM pessoa WHERE cpf = %s"
            resultado = self.executar_query(consulta, (pessoa.cpf,))
            if resultado:
                print("Cliente já cadastrado, não será criado novo registro em pessoa.")
            else:
                # Insere cliente na tabela pessoa
                sql_insert_pessoa = """
                    INSERT INTO pessoa (cpf, nome, telefone, endereco, cidade, estado)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                self.executar_query(sql_insert_pessoa, (
                    pessoa.cpf, pessoa.nome, pessoa.telefone,
                    pessoa.endereco, pessoa.cidade, pessoa.estado
                ))

            # Insere a conta associada (saldo começa em 0.00)
            sql_insert_conta = """
                INSERT INTO conta (senha, cpf_pessoa)
                VALUES (%s, %s)
            """
            self.executar_query(sql_insert_conta, (senha, pessoa.cpf))

            # Recupera o número da conta criada (ultimo id inserido)
            self.cursor.execute("SELECT LAST_INSERT_ID() AS numero_conta")
            numero_conta = self.cursor.fetchone()["numero_conta"]

            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            return numero_conta

        except Exception as e:
            print(f"Erro ao criar conta: {e}")
            self.conn.rollback()
            return None

    def autenticar_conta(self, numero_conta: int, senha: str) -> bool:
        try:
            consulta = "SELECT numero_conta FROM conta WHERE numero_conta = %s AND senha = %s"
            resultado = self.executar_query(consulta, (numero_conta, senha))
            return bool(resultado)  # True se encontrou, False se não
        except Exception as e:
            print(f"Erro na autenticação: {e}")
            return False