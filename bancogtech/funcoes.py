from classe.pessoa import Pessoa
from classe.banco import Banco
import validations
import os

banco = Banco()
def cadastrar_nova_conta():
    
    while True:
        os.system("cls")
        print("=== Cadastro de nova conta ===")

        while True:
            os.system("cls")
            cpf = input("CPF (apenas números): ")
            if not validations.validar_cpf(cpf):
                print("CPF inválido. Tente novamente.")
                continue
            # Verifica se CPF já existe no banco
            if validations.existe_cpf(cpf):
                print("CPF já cadastrado. Não é possível criar nova conta com este CPF.")
                continue
            break

        while True:
            os.system("cls")
            nome = input("Nome: ")
            if not validations.validar_nome(nome):
                print("Nome inválido. Tente novamente.")
                continue
            break
        
        while True:
            os.system("cls")
            telefone = input("Telefone (11 dígitos): ")
            if not validations.validar_telefone(telefone):
                print("Telefone inválido. Tente novamente.")
                continue
            break
        
        while True:
            os.system("cls")
            endereco = input("Endereço: ")
            if not validations.validar_endereco(endereco):
                print("Endereço não pode ser vazio. Tente novamente.")
                continue
            break

        while True:
            os.system("cls")
            cidade = input("Cidade: ")
            if not validations.validar_cidade(cidade):
                print("Cidade não pode ser vazia. Tente novamente.")
                continue
            break

        while True:
            os.system("cls")
            estado = input("Estado (sigla, ex: SP): ")
            if not validations.validar_estado(estado):
                print("Estado inválido. Tente novamente.")
                continue
            break

        while True:
            os.system("cls")
            senha = input("Senha (6 dígitos numéricos): ")
            if not validations.validar_senha(senha):
                print("Senha inválida. Deve conter exatamente 6 dígitos numéricos.")
                continue
            break
        
        os.system("cls")
        print("\nConfirme os dados informados:")
        print(f"CPF: {cpf}")
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
        print(f"Endereço: {endereco}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
        print(f"Senha: {senha}")

        confirmar = input("Confirma os dados? (S/N): ").strip().upper()

        if confirmar == 'S':
            try:
                pessoa = Pessoa(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, cidade=cidade, estado=estado)
                numero_conta = banco.criar_conta(pessoa, senha)
                os.system("cls")
                if numero_conta:
                    print(f"Conta criada com sucesso! Número: {numero_conta}")
                    break
                else:
                    print("Falha ao criar conta.")
            except Exception as e:
                os.system("cls")
                print(f"Erro no cadastro: {e}")
            finally:
                banco.fechar_conexao()
        else:
            confirmar2 = input("Deseja continuar o cadastro? (S/N): ").strip().upper()
            if confirmar2 == 'S':
                os.system("cls")
                print("Reiniciando cadastro...")
            else:
                print("Cadastro cancelado.")
                banco.fechar_conexao()
                break

def autenticar_conta():
    # banco = Banco()

    while True:
        os.system("cls")
        print("=== Autenticação ===")

        while True:
            os.system("cls")
            numero_str = input("Número da conta: ").strip()
            if not numero_str:
                print("Número da conta não pode ser vazio.")
                continue
            if not numero_str.isdigit():
                print("Número da conta deve conter apenas dígitos.")
                continue
            numero = int(numero_str)
            break

        while True:
            os.system("cls")
            senha = input("Senha: ").strip()
            if not senha:
                print("Senha não pode ser vazia.")
                continue
            break

        os.system("cls")
        print("\nConfirme os dados informados:")
        print(f"Conta: {numero}")
        print(f"Nome: {senha}")

        confirmar = input("Confirma os dados? (S/N): ").strip().upper()

        if confirmar == 'S':
            try:
                os.system("cls")
                if banco.autenticar_conta(numero, senha):
                    print("Autenticação bem-sucedida!\nCarregando...\n")
                    return True
                else:
                    print("Número da conta ou senha incorretos.")
                    return False
            except Exception as e:
                print(f"Ocorreu um erro durante a autenticação: {e}")
                return False
        else:
            confirmar2 = input("Deseja continuar a autenticação? (S/N): ").strip().upper()
            os.system("cls")
            if confirmar2 == 'S':
                print("Reiniciando autenticação...")
            else:
                print("Autenticação cancelada.")
                break