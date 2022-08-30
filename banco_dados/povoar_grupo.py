'''Incluir Casa e trabalho'''
# pylint: disable=E0611, C0103

from mysql.connector import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('Casa',),
    ('Trabalho',),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} regristro(s)!')
        