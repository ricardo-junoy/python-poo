import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados da aplicação"""

	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None

	def conecta(self):
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		try:
			self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		# Cria as tabelas do banco
		try:
			cursor = self.conexao.cursor()
			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				nome TEXT NOT NULL,
				cpf VARCHAR(11) UNIQUE NOT NULL,
				email TEXT NOT NULL
			);
			""")

		except AttributeError:
			print('Faça a conexão do banco antes de criar as tabelas')


	def inserir_cliente(self, nome, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()
			try:
				cursor.execute("""
					INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
					""", (nome, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpf %s já existe!' % cpf)

			self.conexao.commit()	
		except AttributeError:
			print('Faça a conexão do banco antes de inserir um cliente')


	def buscar_cliente_cpf(self, cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()
			#obter os dados
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[2] == cpf:
					print('Cliente %s encontrado pelo cpf.' % linha[1])
					break
		except AttributeError:
			print('Faça a conexão no banco antes de buscar clientes')	

	def remover_cliente(self, cpf):
		"""Deleta um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()
			try:
				cursor.execute("""
					DELETE FROM clientes WHERE cpf=? """, (cpf,))
			except sqlite3.IntegrityError:
				print('O cpf %s não existe' % cpf)	
		except AttributeError:
			print('Faça a conexão do banco antes de remover um cliente')

	def buscar_cliente_email(self,email):
		"""Busca um cliente pelo email"""
		cursor = self.conexao.cursor()
		try:
			cursor.execute("""SELECT * FROM clientes WHERE email=?""",(email,))

			for linha in cursor.fetchall():
				if linha[3] == email:
					print('Cliente %s encontrado pelo nome' % linha[1])
					return True
				else:
					return False

		except AttributeError:
			print('Faça a conexão no banco antes de buscar clientes')		