CREATE TABLE IF NOT EXISTS prefeitos (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cidade_id INT UNSIGNED,
    UNIQUE KEY (cidade_id)
    FOREIGN KEY (cidade_id) REFERENCES cidades (id)
);