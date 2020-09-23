class ListaTarefas():

    def __init__(self):
        print("Lista de tarefas: ")
        self.tarefas = []
        self.acoes_feitas = []
        self.acoes_desfeitas = []
    def adicionar(self):
        tarefa = input("Digite uma nova tarefa: ")
        self.acoes_feitas.append(('adicionar', tarefa))
        self.tarefas.append(tarefa)
        self.listar()
        return self.tarefas

    def remover(self):
        tarefa = int(input("Digite o numero da tarefa que deseja remover :"))
        self.acoes_feitas.append(('remover', self.tarefas[tarefa-1], tarefa-1))
        self.tarefas.pop(tarefa - 1)
        self.listar()
        return self.tarefas

    def listar(self):
        for i, n in enumerate(self.tarefas):
            print(f"{i+1} - {n}")

    def voltar(self):
        if 'adicionar' in self.acoes_feitas[-1][0]:
            self.tarefas.remove(self.acoes_feitas[-1][1])
            self.listar()
            self.acoes_desfeitas.append(self.acoes_feitas[-1])
            return self.acoes_feitas.pop(-1)
        if 'remover' in self.acoes_feitas[-1][0]:
            self.tarefas.insert(-1, self.acoes_feitas[-1][1])
            self.listar()
            self.acoes_desfeitas.append(self.acoes_feitas[-1])
            return self.acoes_feitas.pop(-1)

    def refazer(self):
        print(self.acoes_desfeitas)
        if 'remover' in self.acoes_desfeitas[-1][0]:
            self.tarefas.remove(self.acoes_desfeitas[-1][1])
            self.listar()
            self.acoes_feitas.append(self.acoes_desfeitas[-1])
            return self.acoes_desfeitas.pop(-1)
        if 'adicionar' in self.acoes_desfeitas[-1][0]:
            self.tarefas.insert(-1, self.acoes_desfeitas[-1][1])
            self.listar()
            self.acoes_feitas.append(self.acoes_desfeitas[-1])
            return self.acoes_desfeitas.pop(-1)


lista1 = ListaTarefas()

while True:
    menu = input('''
Digite a ação desejada:
1 - Adicionar
2 - Remover
3 - Listar
4 - Voltar
5 - Refazer
''')
    if int(menu) == 1:
        lista1.adicionar()
    elif int(menu) == 2:
        lista1.remover()
    elif int(menu) == 3:
        lista1.listar()
    elif int(menu) == 4:
        lista1.voltar()
    elif int(menu) == 5:
        lista1.refazer()
    else:
        print("Opção inválida")
