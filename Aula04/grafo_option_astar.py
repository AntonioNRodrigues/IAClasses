from Aula04.search import *


class ProblemaGrafoOptAast(Problem):
    grafo = {'I': {'A': 1, 'B': 1},
             'A': {'C': 1},
             'B': {'C': 2},
             'C': {'F': 3},
             'F': {}}

    def __init__(self, initial='I', final='F'):
        super().__init__(initial, final)

    def actions(self, estado):
        sucessores = self.grafo[estado].keys()  # métodos keys() devolve a lista das chaves do dicionário
        accoes = list(map(lambda x: "ir de {} para {}".format(estado, x), sucessores))
        return accoes

    def result(self, estado, accao):
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]

    def path_cost(self, c, state1, action, state2):
        return c + self.grafo[state1][state2]

    def h1(self, no):
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        h = {'I': 2, 'A': 4, 'B': 1, 'C': 1, 'F': 0}
        return h[no.state]


p = ProblemaGrafoOptAast()
result = uniform_cost_search(p)
print("Custo Uniforme:: uniform_cost_search")
print(result.solution())
print(result.path_cost)

p = ProblemaGrafoOptAast()
res_astar = astar_search(p, p.h1)
print("A *:: astar_search")
print(res_astar.solution())
print(res_astar.path_cost)


class ProblemaGrafoOptAastV2(ProblemaGrafoOptAast):
    def h1(self, no):
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        h = {'I': 2, 'A': 2, 'B': 1, 'C': 1, 'F': 0}
        return h[no.state]


p = ProblemaGrafoOptAastV2()
result = uniform_cost_search(p)
print("Custo Uniforme:: uniform_cost_search")
print(result.solution())
print(result.path_cost)

p = ProblemaGrafoOptAastV2()
res_astar = astar_search(p, p.h1)
print("A *:: astar_search")
print(res_astar.solution())
print(res_astar.path_cost)



