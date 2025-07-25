def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    # Elimina CPFs com todos os dígitos iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = ((soma * 10) % 11) % 10
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = ((soma * 10) % 11) % 10
    
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

def validar_nome(nome: str) -> bool:
    if nome is None or nome.strip() == "":
        return False
    if not all(palavra.isalpha() for palavra in nome.split()):
        return False
    if len(nome) <= 1:
        return False
    return True

def validar_telefone(telefone: str) -> bool:
    return telefone.isdigit() and len(telefone) == 11

def validar_endereco(endereco: str) -> bool:
    return bool(endereco and endereco.strip())

def validar_cidade(cidade: str) -> bool:
    return bool(cidade and cidade.strip())

def validar_estado(estado: str) -> bool:
    ufs = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    }
    if not estado:
        return False
    return estado.strip().upper() in ufs

def validar_senha(senha: str) -> bool:
    if senha is None or not senha.isdigit() or len(senha) != 6:
        return False
    return True



