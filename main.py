from funcao import *

vazamento={}
resposta=""

while resposta !="6":
    print("-"*30,"\n\n[1]-Adcionar Vazamento\n[2]-Exibir Vazamento\n[3]-Buscar Vazamento\n[4]-Excluir Vazamento\n[5]-Alterar Validade\n[6]-Sair\n")
    print("-"*30)
    resposta=input("R:")

    if resposta=="1":
        #Adcionar Vazamento
        adcionar_vazamento(vazamento)

    elif resposta=="2":
        #Exibir Vazamento
        exibir_vazamento(vazamento)

    elif resposta=="3":
        #Buscar Vazamento
        buscar_vazemento(vazamento)

    elif resposta=="4":
        #Excluir Vazamento
        excluir_vazamento(vazamento)

    elif resposta=="5":
        #Alterar validade
        alterar_validade(vazamento)

    elif resposta=="6":
        print("Saindo...")
