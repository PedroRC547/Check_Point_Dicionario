#Adcionar Vazamento
def adcionar_vazamento(vazamento):
    print("---Adicionar Vazamento---")
    resposta="S"
    while resposta=="S":
        tag = input("\nTAG do dicionario: ").upper()
        vazamento[tag]=[input("\nEmail: "), input("Senha: "), int(input("Validade: "))]
        resposta = input("\nDeseja adicionar mais um vazamento [s/n]: ").upper()
        print("-"*30)

#Exibir Vazamento
def exibir_vazamento(vazamento):
    print("\n---Exibir Vazamento---")
    for tag, dados in vazamento.items():
        print("-"*30)
        print("\nTAG.....: ", tag)
        print("Email.....: ", dados[0])
        print("Senha.....: ", dados[1])
        print("Validade..: ", dados[2])
        print("-"*30)

#Buscar Vazamento
def buscar_vazemento(vazamento):
    print("\n---Buscar Vazamento---")
    busca = input("\nTAG: ").upper()
    lista = vazamento.get(busca)
    if lista !=None:
        print("\nEmail...: ", lista[0])
        print("Senha.....: ", lista[1])
        print("Validade..: ", lista[2])
        print("-"*30)
    else:
        print("Vazamento não encontrado")
        print("-"*30)

#Alterar validade
def alterar_validade(vazamento):
    print("\n---Alterar Validade---")
    busca = input("\nTAG: ")
    nova_validade=int(input("Nova validade: "))
    lista = vazamento.get(busca)
    if lista !=None:
        lista[2]=nova_validade
        print("\nEmail...: ", lista[0])
        print("Senha.....: ", lista[1])
        print("Validade..: ", lista[2])
        print("-"*30)
    else:
        print("Vazamento não encontrado")
        print("-"*30)

#Excluir Vazamento
def excluir_vazamento(vazamento):
    print("\n---Excluir Vazamento---")
    deletar = input("\nVazamento que deseja deletar [TAG]: ")
    if vazamento.get(deletar) !=None:
        del vazamento[deletar]
    print("-"*30, "\nElemento Excluido  com sucesso!\n")
    print("-"*30)
