from Aula04.search import *


class ProblemaGrafoNaiveCustos(Problem):
    grafo = {'I': {'A': 2, 'B': 5},
             'A': {'C': 2, 'D': 4, 'I': 2},
             'B': {'D': 1, 'F': 5, 'I': 5},
             'C': {},
             'D': {'C': 3, 'F': 2},
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
        h = {'I': 7, 'A': 2, 'B': 3, 'C': 1, 'D': 5, 'F': 0}
        return h[no.state]


p = ProblemaGrafoNaiveCustos()
print(p.grafo)
result = breadth_first_tree_search(p)
print("Profundidade Grafo")
print(result.solution())
print(result.path_cost)

resultado = uniform_cost_search(p)
print("Custo Uniforme")
print(resultado.solution())
print(resultado.path_cost)

resultado = iterative_deepening_search(p)
print("Aprofundamento Progressivo ")
print(resultado.solution())
print(resultado.path_cost)

# precisamos desta instrução para ir buscar o grafo e percorrer depois estado a estado
p = ProblemaGrafoNaiveCustos()
for estado in p.grafo.keys():
    q = ProblemaGrafoNaiveCustos(estado)
    print("Custo Uniforme")
    resultado = uniform_cost_search(q)
    if resultado == None:
        print("sem solução a partir de", estado)
    else:
        print("Menor distância de ", estado, "ao objectivo", q.goal, "=", resultado.path_cost)

print("Heuristicas")
print("h1 de", 'A', " =", p.h1(Node('A')))
print("h1 de", 'I', " =", p.h1(Node('I')))

print("Heuristicas")
for estado in p.grafo.keys():
    print("h1 de", estado, " =", p.h1(Node(estado)))

prob = ProblemaGrafoNaiveCustos()
print("Melhor Primeiro")
res_gbfs = greedy_best_first_graph_search(prob, prob.h1)
print(res_gbfs.solution())
print(res_gbfs.path_cost)


# redefine the heuristic so we can aplly the a*(this algoritm must have an heuristic admissivel and consistent)

class ProblemaGrafoNaiveCustosV2(ProblemaGrafoNaiveCustos):
    def h1(self, no):
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        h = {'I': 7, 'A': 2, 'B': 3, 'C': 1, 'D': 2, 'F': 0}
        return h[no.state]


p = ProblemaGrafoNaiveCustosV2()
print("Heuristicas Redefined")
for estado in p.grafo.keys():
    print("h1 de", estado, " =", p.h1(Node(estado)))

res_astar = astar_search(p, p.h1)
print("A*")
print(res_astar.solution())
print(res_astar.path_cost)

