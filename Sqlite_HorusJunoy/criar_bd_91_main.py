from criar_bd_91_database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Ricardo',11111111111,'ricardojunoy@gmail.com')
	banco.inserir_cliente('Renato',22222222222,'renatojunoy@gmail.com')
	banco.inserir_cliente('Roberto',33333333333,'robertojunoy@gmail.com')
	banco.remover_cliente('11111111111')
	banco.buscar_cliente_cpf('11111111111')
	banco.buscar_cliente_cpf('22222222222')
	banco.buscar_cliente_email('renatojunoy@gmail.com')
	banco.buscar_cliente_email('robertojunoy@gmail.com')
	banco.desconecta()