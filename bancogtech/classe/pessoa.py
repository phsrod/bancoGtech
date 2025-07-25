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
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def cidade(self):
        return self._cidade
    
    @property
    def estado(self):
        return self._estado
    
    