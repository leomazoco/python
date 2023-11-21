import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user=' ', #USUÁRIO DO BANCO DE DADOS
    password=' ', #SENHA DO BANCO DE DADOS,
    database=' ', #SCHEMA CRIADO NO BANCO DE DADOS
)

cursor = conexao.cursor()

print('Operações Disponíveis')
print(' ')
print('1 - Criar Venda')
print('2 - Selecionar todas as Venda')
print('3 - Selecionar Venda')
print('4 - Atualizar Venda')
print('5 - Deletar Venda')
print(' ')
operacao = input ('Digite a operação que deseja realizar: ')

#INSERIR REGISTRO
if operacao == '1':
    try:
        nome_produto = input ('Digite o produto que deseja inserir: ')
        valor = input ('Digite o valor do produto: ')
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'  # CASO O COMANDO SEJA DE ALTERAÇÃO NO BANCO, NECESSÁRIO CONEXAO.COMMIT()
        cursor.execute(comando)
        conexao.commit()  # edita o banco de dados
        print(f'O produto {nome_produto} foi inserido no Banco de Dados')
    except ValueError:
        print('Não foi possível alterar o Banco de Dados')

    cursor.close()
    conexao.close()

elif operacao == '2':
    try:
        comando = f'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall() #LE OS REGISTROS NO BANCO DE DADOS
        print(resultado)

        cursor.close()
        conexao.close()
    except ValueError:
        print('Não há registros no Banco de Dados')

        cursor.close()
        conexao.close()

elif operacao == '3':
    selecao = input ('Selecionar pelo ID ou NOME (1 - ID, 2 - NOME): ')
    if selecao == '1':
        try:
            id_produto = input('Digite o ID do produto que deseja exibir: ')
            comando = f'SELECT idvendas, nome_produto, valor FROM vendas WHERE idvendas = {id_produto}'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)

            cursor.close()
            conexao.close()
        except ValueError:
            print(f'Não existe produto com o ID {id_produto}')
            cursor.close()
            conexao.close()
    else:
        try:
            nome_busca_produto = input('Digite o NOME do produto que deseja exibir: ')
            comando = f'SELECT idvendas, nome_produto, valor FROM vendas WHERE nome_produto = "{nome_busca_produto}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)

            cursor.close()
            conexao.close()
        except ValueError:
            print(f'Não existe o produto {nome_busca_produto} no Banco de Dados')

            cursor.close()
            conexao.close()

elif operacao == '4':
    selecao = input('Atualizar produto pelo ID ou NOME (1 - ID, 2 - NOME): ')
    if selecao == '1':
        id_busca = input('Digite o ID do produto que deseja editar: ')
        try:
            comando = f'SELECT idvendas, nome_produto, valor FROM vendas WHERE idvendas = "{id_busca}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
            editar_venda = input('Deseja realmente editar esse registro? (1 - Editar, 2 - Cancelar): ')
            if editar_venda == '1':
                edicao_venda = input('Qual valor deseja editar? (1 - Nome do Produto, 2 - Valor): ')
                if edicao_venda == '1':
                    novo_nome = input('Digite o novo nome do produto: ')
                    try:
                        comando_edicao = f'UPDATE vendas SET nome_produto = "{novo_nome}" WHERE idvendas = "{id_busca}"'
                        cursor.execute(comando_edicao)
                        conexao.commit()
                        print('A venda foi alterado com sucesso')
                    except ValueError:
                        print(f'Ocoreu um erro ao alterar o nome do produto na venda de ID {id_busca}')
                else:
                    novo_valor = input('Digite o novo valor do produto: ')
                    try:
                        comando_edicao = f'UPDATE vendas SET valor = "{novo_valor}" WHERE idvendas = "{id_busca}"'
                        cursor.execute(comando_edicao)
                        conexao.commit()
                        print('A venda foi alterado com sucesso')
                    except ValueError:
                        print(f'Não foi encontrada uma venda com o ID {id_busca}')

                        cursor.close()
                        conexao.close()
        except ValueError:
            print(f'Não existe o produto {id_busca} no Banco de Dados')

            cursor.close()
            conexao.close()

    elif selecao == '2':
        nome_busca = input('Digite o nome do produto que deseja editar: ')
        try:
            comando = f'SELECT idvendas, nome_produto, valor FROM vendas WHERE nome_produto = "{nome_busca}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
            editar_venda = input('Deseja realmente editar esse registro? (1 - Editar, 2 - Cancelar): ')
            if editar_venda == '1':
                edicao_venda = input('Qual valor deseja editar? (1 - Nome do Produto, 2 - Valor): ')
                if edicao_venda == '1':
                    novo_nome = input('Digite o novo nome do produto: ')
                    try:
                        comando_edicao = f'UPDATE vendas SET nome_produto = "{novo_nome}" WHERE nome_produto = "{nome_busca}"'
                        cursor.execute(comando_edicao)
                        conexao.commit()
                        print('A venda foi alterado com sucesso')

                        cursor.close()
                        conexao.close()
                    except ValueError:
                        print(f'Ocoreu um erro ao alterar o nome do produto')

                        cursor.close()
                        conexao.close()
                else:
                    novo_valor = input('Digite o novo valor do produto: ')
                    try:
                        comando_edicao = f'UPDATE vendas SET valor = "{novo_valor}" WHERE nome_produto = "{nome_busca}"'
                        cursor.execute(comando_edicao)
                        conexao.commit()
                        print('A venda foi alterado com sucesso')

                        cursor.close()
                        conexao.close()
                    except ValueError:
                        print(f'Não foi encontrada uma venda com o nome {nome_busca}')

                        cursor.close()
                        conexao.close()
        except ValueError:
            print(f'Não existe o produto com o nome {nome_busca} no Banco de Dados')

            cursor.close()
            conexao.close()


elif operacao == '5':
    delete_op = input('Deseja deletar a venda pelo ID ou NOME do produto? (1 - ID, 2 - NOME: ')
    if delete_op == '1':
        delete_venda = input ('Digite o ID da venda que deseja excluir: ')
        try:
            comando_delete = f'DELETE FROM vendas WHERE idvendas = {delete_venda}'
            cursor.execute(comando_delete)
            conexao.commit()

            cursor.close()
            conexao.close()

            print('Venda exlcuída com sucesso!')

        except ValueError:
            print(f'Erro ao excluir a venda ID {delete_venda}')

            cursor.close()
            conexao.close()

    elif delete_op == '2':
        delete_produto = input('Digite o nome do produto que deseja excluir a venda: ')
        try:
            comando_delete = f'DELETE FROM vendas WHERE nome_produto = "{delete_produto}"'
            cursor.execute(comando_delete)
            conexao.commit()

            cursor.close()
            conexao.close()

            print('Venda exlcuída com sucesso!')

        except ValueError:
            print(f'Ocoreu um erro ao deletar o produto {delete_produto}')







