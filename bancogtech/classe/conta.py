import bancogtech.validations as validations


class Conta():
    def __init__(self, senha, cpf_pessoa, numero_conta=None, saldo=0.0):
        self.numero_conta = numero_conta  # Pode vir do BD
        self.senha = senha
        self.saldo = saldo
        self.cpf_pessoa = cpf_pessoa

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        if not validations.validar_senha(senha):
            raise ValueError("A senha deve conter exatamente 6 dígitos numéricos.")
        self._senha = senha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = saldo

    @property
    def cpf_pessoa(self):
        return self._cpf_pessoa

    @cpf_pessoa.setter
    def cpf_pessoa(self, cpf):
        if not validations.validar_cpf(cpf):
            raise ValueError("CPF inválido.")
        self._cpf_pessoa = cpf

    def __str__(self):
        return (
            f"Número da Conta: {self.numero_conta if self.numero_conta else 'A definir'}\n"
            f"CPF do Titular: {self.cpf_pessoa}\n"
            f"Saldo: R$ {self.saldo:.2f}"
        )
