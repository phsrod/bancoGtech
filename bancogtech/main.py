import mysql.connector
from bd.db_config import db_config
from mysql.connector import Error


#testes de conexão
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conectado ao banco de dados com sucesso!")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def connect_and_list_databases():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print("Bancos de dados no servidor MySQL:")
            for db in databases:
                print(f"- {db[0]}")
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Erro: {e}")

def list_tables():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                print("Tabelas existentes no banco de dados:")
                for table in tables:
                    print(f"- {table[0]}")
            else:
                print("Não há tabelas no banco de dados.")
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    connect_to_database()
    connect_and_list_databases()
    list_tables()
