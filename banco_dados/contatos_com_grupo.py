'''Incluir Casa e trabalho'''
# pylint: disable=E0611, C0103

from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    SELECT
        grupos.descricao AS grupo,
        contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome    
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True) #recurso do mysql
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')
            