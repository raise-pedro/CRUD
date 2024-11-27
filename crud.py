menu = '''
========== SISTEMA DE CADASTRO ==========
1. Adicionar Novo Estudante
2. Listar Estudantes
3. Buscar um Estudante
4. Editar Informações de um Estudante
5. Deletar Cadastro de um Estudante
6. Sair
=========================================
Selecione uma opção: '''

def adicionar_estudante(dicionario):
  nome = input('Digite o nome do estudante: ').capitalize()
  if buscar_estudante(nome, dicionario):
    print('Estudante já cadastrado.')
  else:
    idade = int(input('Digite a idade do estudante: '))
    cidade = input('Digite a cidade do estudante: ').capitalize()
    novo_cadastro = {'Idade': idade, 'Cidade': cidade}
    dicionario[nome] = novo_cadastro
    print(f'Estudante {nome} cadastrado com sucesso!')

def listar_estudantes(dicionario):
  if not dicionario:
    print('Nenhum estudante cadastrado.')
  else:
    print('========= Lista de Estudantes =========')
    for nome in sorted(dicionario):
        print(nome,'-', dicionario[nome])


def buscar_estudante(nome, dicionario):
  return nome in dicionario

def mostrar_busca_estudante(dicionario):
  nome = input('Digite o nome do estudante: ').capitalize()
  if buscar_estudante(nome, dicionario):
    print(f'Estudante {nome} encontrado(a)!')
    opcao = input('Deseja editar? (S/N)\n')
    if opcao == 's' or opcao == 'sim':
      editar_cadastro(dicionario=dicionario)
  else:
    print(f'Estudante {nome} não foi encontrado(a).')
    opcao = input('Deseja cadastrar? (S/N)\n').lower()
    if opcao == 's' or opcao == 'sim':
      adicionar_estudante(dicionario=dicionario)

def deletar_estudante(dicionario):
  nome = input('Informe o nome do estudante a ser deletado: ').capitalize()
  if buscar_estudante(nome, dicionario):
    print(nome,'-', dicionario[nome])
    opcao = input('Tem certeza que deseja deletar as informações desse estudante? (S/N)\n')
    if opcao == 's' or opcao == 'sim':
      del dicionario[nome]
      print('Estudante deletado com sucesso.')
  else:
    print(f'Estudante {nome} não econtrado.')

def editar_cadastro(dicionario):
  nome = input('Digite o nome do estudante a ser editado: ').capitalize()
  if buscar_estudante(nome, dicionario):
    del dicionario[nome]
    adicionar_estudante(dicionario=dicionario)
  else:
    print('Estudante não cadastrado.')
    opcao = input('Deseja cadastrar? (S/N)\n').lower()
    if opcao == 's' or opcao == 'sim':
      adicionar_estudante(dicionario=dicionario)

def gerenciar_cadastro():
  estudantes = {}
  while True:
    opcao = input(menu).lower()
    if opcao == '1' or opcao == 'adicionar':
      adicionar_estudante(estudantes)
    elif opcao == '2' or opcao == 'listar':
      listar_estudantes(estudantes)
    elif opcao == '3' or opcao == 'buscar':
      mostrar_busca_estudante(estudantes)
    elif opcao == '4' or opcao == 'editar':
      editar_cadastro(estudantes)
    elif opcao == '5' or opcao == 'deletar':
      deletar_estudante(estudantes)
    elif opcao == '6' or opcao == 'sair':
      print('Saindo do programa...')
      break
    else:
      print('Opção inválida!')

gerenciar_cadastro()
