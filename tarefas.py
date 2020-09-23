class ListaTarefas():
    def __init__(self):
        print("Lista de tarefas: ")
        self.tarefas = []
        self.acoes = {}
    def adicionar(self, *args):
        tarefa = input("Digite uma nova tarefa: ")
        self.tarefas.append(tarefa)
        self.acoes.clear()
        self.acoes.update({'adicionar': tarefa})
        self.listar()
        return self.tarefas
    def remover(self, *args):
        tarefa = int(input("Digite o numero da tarefa que deseja remover :"))
        self.tarefas[tarefa] = ''
        self.acoes.clear()
        self.acoes.update({'remover': self.tarefas[tarefa-1]})
        self.listar()
        return self.tarefas
    def listar(self):
        for i, n in enumerate(self.tarefas):
            print(f"{i+1} - {n}")
    def voltar(self):
        print(self.acoes)
        if 'adicionar' in self.acoes:
            self.listar()
            return self.tarefas.remove(self.acoes['adicionar'])
        if 'remover' in self.acoes:
            self.listar()
            return self.tarefas.append(self.acoes['remover'])
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
