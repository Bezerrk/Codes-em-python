import json
tarefas = []
loop = True
escolha = int(1)


#carrega tarefas
def carregar_tarefas():
    global tarefas
    try: 
        with open('tarefas.json','r') as arquivo:
            tarefas = json.load(arquivo)
    except:
        print("nenhum arquivo de tarefas encontrado.")

#metodo adiciona tarefa
def adiciona_tarefa():
    titulo = str(input("Insira o titulo da tarefa: "))
    desc = str(input("Insira a descricao: "))
    feita = bool(False)
    tarefa = {
        'titulo':titulo,
        'subtitulo':desc,
        'concluida':feita
    }
    tarefas.append(tarefa)

#metodo lista tarefas
def lista_tarefas():
    if len(tarefas) != 0:
        for i,tarefa in enumerate(tarefas):
            print(i,".",tarefa,"\n")
    if len(tarefas) == 0:
        print ("Não há items na lista de tarefas, tente inserir alguns")

#metodo deleta tarefas
def deleta_tarefa():
    lista_tarefas()
    if len(tarefas) != 0:
        deleta = int(input("Escolha uma opcao para deletar: "))
        confirma = int(input("tem certeza que deseja deletar essa tarefa?\n1.sim\n2.nao\nescolha: "))
        if confirma == 1:
            tarefas.remove(tarefas[deleta])

#metodo marca como feito
def marcar_como_feito():
    lista_tarefas()
    if len(tarefas) != 0:
        selecao = int(input("Escolha uma para marcar como feito: "))
        tarefas[selecao]['concluida'] = True
        print("marcada como concluida!")

#salva as tarefas
def salvar():
    with open('tarefas.json','w') as arquivos:
        json.dump(tarefas,arquivos)
    print("Tarefas salvas com sucesso!")    

#loop principal do menu
carregar_tarefas()
while loop == True:
    escolha = int(input("Escolha uma das opçoes:\n1.inserir tarefa\n2.imprimir tarefas\n3.remover tarefa\n4.marcar como concluida\n0.sair\nEscolha: "))
    if escolha == 1:
        adiciona_tarefa()
    if escolha == 2:
        lista_tarefas()
    if escolha == 3:
        deleta_tarefa()
    if escolha == 4:
        marcar_como_feito()
    if escolha == 0:
        salvar()
        loop = False
        print("Obrigado por usar!")
        break
