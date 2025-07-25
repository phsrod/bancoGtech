import funcoes


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
        if nome is None or nome.strip() == "":
            raise ValueError("O nome não pode ser vazio.")
        if not all(palavra.isalpha() for palavra in nome.split()):
            raise ValueError("O nome deve conter apenas letras e espaços entre as palavras.")
        if len(nome) <= 1:
            raise ValueError("O nome deve ter mais de um caractere.")
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
        
        if not funcoes.validar_cpf(cpf_limpo):
            raise ValueError("CPF inválido.")
        
        self._cpf = cpf_limpo
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        if telefone.isdigit() and len(telefone) == 11:
            self._telefone = telefone
        else:
            raise ValueError("Telefone deve ser um número de 11 dígitos.")
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        if endereco.strip():
            self._endereco = endereco
        else:
            raise ValueError("O endereço não pode ser vazio.")
    
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, cidade):
        if cidade.strip():
            self._cidade = cidade
        else:
            raise ValueError("A cidade não pode ser vazia.")
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        ufs = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        }
        if estado.strip().upper() in ufs:
            self._estado = estado.strip().upper()
        else:
            raise ValueError("Estado inválido. Por favor, insira um estado válido.")
    
    def __str__(self):
        return (
            f"Nome: {self._nome}\n"
            f"CPF: {self._cpf}\n"
            f"Telefone: {self._telefone}\n"
            f"Endereço: {self._endereco}\n"
            f"Cidade: {self._cidade} - {self._estado}"
        )

    