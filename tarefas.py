import sqlite3
conexao = sqlite3.connect('sqlm2s2.dados')
sql = '''CREATE TABLE tarefas (
	id INTEGER NOT NULL,
	nome TEXT,
	"data" TEXT,
	materia_id INTEGER NOT NULL,
	status_conclusão TEXT,
	CONSTRAINT tarefas_PK PRIMARY KEY (id),
	CONSTRAINT tarefas_FK FOREIGN KEY (materia_id) REFERENCES aluno(id)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()