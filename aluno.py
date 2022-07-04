import sqlite3
conexao = sqlite3.connect('sqlm2s2.dados')
sql = '''CREATE TABLE aluno (
	id INTEGER NOT NULL,
	nome TEXT,
	professor TEXT,
	materia TEXT,
	CONSTRAINT aluno_PK PRIMARY KEY (id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()
