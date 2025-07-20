# 1. Criando catálogo telefonico
catalogo_telefonico = {}    #Cria catalogo

# 2. Função incluir: cria função para incluir um contato no catálogo
# e essa função deve receber o nome e o numero do telefone do catalogo
def incluir_contato(catalogo, nome, telefone):
    '''
    Inclui um novo contato no catalogo telefonico
    Args:
        catalogo (dict): O dicionario que representa o catalogo telefonico
        nome (str): O nome do contato a ser incluido
        telefone (str): O numero de telefone do contato
    '''
    catalogo[nome] = telefone
    print(f"Contato '{nome}' com telefone '{telefone}' incluído com sucesso.")


# 3. Função excluir: Cria função para excluir um contato
# Essa função recebe o nome do contato e devolve uma mensagem informando se foi exluido ou não
def excluir_contato(catalogo, nome):
    if nome in catalogo:
        del catalogo[nome]
        return f"Contato '{nome}' excluído com sucesso."
    else:
        return f"Erro: contato '{nome}' não consta no catalogo."


# 4. Função pesquisar: Cria uma função para pesquisar um contato
def pesquisar_contato(catalogo, nome):
    if nome in catalogo:
        return f"O telefone de '{nome}' é: {catalogo[nome]}."
    else:
        return f"Contato '{nome}' não encontrado no catalogo."


# 5. Imprime o catalogo telefonico após chamar as funções implementadas.
def imprimir_catalogo(catalogo):
    if not catalogo:
        print("O catalogo está vazio.")
    else:
        for nome, telefone in catalogo.items():
            print(f"Nome: {nome} telefone: {telefone}")
    print("------------------------------------------\n")

# --- Demostração do uso das funções ---

print("--- Inicializando o Catalogo ---")
imprimir_catalogo(catalogo_telefonico)

#incluir contatos
incluir_contato(catalogo_telefonico, "Luiz", "99991111882")
incluir_contato(catalogo_telefonico, "Gustavo", "99991111882")

#Pesquisando contatos
print(pesquisar_contato(catalogo_telefonico, "Luiz"))
print(pesquisar_contato(catalogo_telefonico, "Gustavo"))

#Excluir contatos
print(excluir_contato(catalogo_telefonico, "Luiz"))
print(excluir_contato(catalogo_telefonico, "Gustavo"))

#Incluir mais um para ver o catalogo novamente
incluir_contato(catalogo_telefonico, "Sara", "99991111882")
incluir_contato(catalogo_telefonico, "Mariana", "99991111882")
imprimir_catalogo(catalogo_telefonico)

print(" --- Fim da Demostração ---")




















