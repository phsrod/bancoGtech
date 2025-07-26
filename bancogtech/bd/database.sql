-- CRIAÇÃO DO BD

CREATE DATABASE IF NOT EXISTS `bd`;
USE `bd`;

-- CRIAÇÃO DAS TABELAS

CREATE TABLE IF NOT EXISTS `pessoa` (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) UNIQUE NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    estado VARCHAR(2) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `conta` (
    numero_conta INT AUTO_INCREMENT PRIMARY KEY,
    senha CHAR(6) NOT NULL,
    saldo DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    cpf_pessoa VARCHAR(11) UNIQUE NOT NULL,
    FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf)
        ON DELETE NO ACTION
        ON UPDATE CASCADE 
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `transacao` (
    id_transacao INT AUTO_INCREMENT PRIMARY KEY,
    tipo_transacao ENUM('deposito', 'saque', 'pix', 'transferencia_enviada', 'transferencia_recebida') NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    conta_origem_id INT, 
    conta_destino_id INT,
    FOREIGN KEY (conta_origem_id) REFERENCES conta(numero_conta)
        ON DELETE NO ACTION
        ON UPDATE CASCADE,
    FOREIGN KEY (conta_destino_id) REFERENCES conta(numero_conta)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
) ENGINE=InnoDB;