class ListaTarefas():
    def __init__(self):
        print("Lista de tarefas: ")
        self.tarefas = []
        self.acoes = {}
    def adicionar(self, *args):
        tarefa = input("Digite uma nova tarefa: ")
        self.tarefas.append(tarefa)
        self.acoes.update({'adicionar': tarefa})
        self.listar()
        return self.tarefas
    def remover(self, *args):
        tarefa = int(input("Digite o numero da tarefa que deseja remover :"))
        self.tarefas.pop(tarefa)
        self.acoes.update({'remover': tarefa})
        return self.tarefas
    def listar(self):
        for i, n in enumerate(self.tarefas):
            print(f"{i+1} - {n}")
    def voltar(self):
        if self.acoes['adicionar']:
            return self.adicionar(self.acoes.values())
        if self.acoes['remover']:
            return self.remover(self.acoes.values())

lista1 = ListaTarefas()

while True:
    menu = int(input('''
Digite a ação desejada:
1 - Adicionar
2 - Remover
3 - Listar
4 - Voltar
5 - Refazer
'''))
    if menu == 1:
        lista1.adicionar()
    elif menu == 2:
        lista1.remover()
    elif menu == 3:
        lista1.listar()
    elif menu == 4:
        lista1.voltar()
    elif menu == 5:
        lista1.refazer()
    else:
        print("Opção inválida")
