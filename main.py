listagem = [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,10,12,11]
contagem = int(len(listagem)*len(listagem))
cont = int(0)
troca = float(0.0)
antes = int(0)
depois = int(1)

while cont <= contagem:
    #incremeta o valor das variaveis a verificar
    cont +=1
    if cont != 0:
        antes += 1
        depois += 1

    #garante que as variaveis não excedam a quantidade de itens
    if antes == int(len(listagem)-1):
        antes = int(0)
        depois = int(1)

    #verifica numeros iguais e remove o valor   
    if listagem [antes] == listagem[depois]:
        listagem.remove(listagem[antes])

    #verifica item por item ordenando-os
    elif listagem [antes] > listagem[depois]:
        troca = listagem[antes]
        listagem [antes] = listagem[depois]
        listagem[depois] = troca

print (listagem)
