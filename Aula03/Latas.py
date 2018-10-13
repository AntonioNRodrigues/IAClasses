from Aula03.search import *


def add_new_empty_lata():
    pass


class EstadoLatas:
    def __init__(self, latas=([], [45, 80, 30, 15])):
        self.latas = latas

    def __str__(self):
        return str(self.latas)

    def __eq__(self, estado):
        """Definir em que circunstância os dois estados são considerados iguais.
        Necessário para os algoritmos de procura em grafo.
        """
        return self.latas == estado.latas

    def __hash__(self):
        """Necessário para os algoritmos de procura em grafo."""
        return hash((self.latas[0], self.latas[1]))


class ProblemJarros(Problem):

    def __init__(self, initList, goal, finalList):
        self.initList = initLista
        self.goal = goal
        self.finalList = finalList

    def actions(self, state):
        accoes = list()
        for i in finalList:
            if finalList[i] == 0:
                accoes.append("new jarro")
            if finalList[i] != 0:
                if finalList[i] < self.goal:
                    accoes.append("add capcity to jarro")
        return accoes

    def result(self, state, action):
        if action == "new jarro":
            result = latas[0].append([])
        if action == "add capcity to jarro":
            result = latas[0].append(state)
        return result


initLista = [45, 80, 30, 15]
finalList = []
latas = ProblemJarros(initLista, 100, finalList)
print(latas.initList)
print(latas.goal)
print(latas.finalList)
print(latas.actions(45))
