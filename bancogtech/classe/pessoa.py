import validations as validations


class Pessoa():
    def __init__(self, nome, cpf, telefone, endereco, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if not validations.validar_nome(nome):
            raise ValueError("Nome inválido: deve conter apenas letras e espaços, não pode ser vazio e ter mais de um caractere.")
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if cpf is None:
            raise ValueError("CPF não pode ser None.")
        # Remove caracteres não numéricos
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        
        if not validations.validar_cpf(cpf_limpo):
            raise ValueError("CPF inválido.")
        
        self._cpf = cpf_limpo
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        if not validations.validar_telefone(telefone):
            raise ValueError("Telefone deve ser um número de 11 dígitos.")
        self._telefone = telefone
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        if not validations.validar_endereco(endereco):
            raise ValueError("O endereço não pode ser vazio.")
        self._endereco = endereco
    
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, cidade):
        if not validations.validar_cidade(cidade):
            raise ValueError("A cidade não pode ser vazia.")
        self._cidade = cidade
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        if not validations.validar_estado(estado):
            raise ValueError("Estado inválido. Por favor, insira um estado válido.")
        self._estado = estado.strip().upper()
    
    def __str__(self):
        return (
            f"Nome: {self._nome}\n"
            f"CPF: {self._cpf}\n"
            f"Telefone: {self._telefone}\n"
            f"Endereço: {self._endereco}\n"
            f"Cidade: {self._cidade} - {self._estado}"
        )

    