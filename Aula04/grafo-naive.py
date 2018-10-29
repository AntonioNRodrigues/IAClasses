from Aula04.search import *


class ProblemaGrafoNaive(Problem):
    grafo = {'I': ['A', 'B'],
             'A': ['C', 'D', 'I'],
             'B': ['D', 'F', 'I'],
             'C': [],
             'D': ['C', 'F'],
             'F': []}

    def __init__(self, initial='I', final='F'):
        super().__init__(initial, final)

    def actions(self, estado):
        sucessores = self.grafo[estado]
        accoes = map(lambda x: "ir de {} para {}".format(estado, x), sucessores)
        return list(accoes)

    def result(self, estado, accao):
        """Assume-se que uma acção é da forma 'ir de X para Y'
           Quebramos a frase da acção numa lista de palavras e a última corresponde à acção
        """
        return accao.split()[-1]


p = ProblemaGrafoNaive()
print(p.initial)
print(p.grafo)

# result = depth_first_tree_search(p)
# print("Profundidade Arvore ")
# print(result.solution())

result = depth_first_graph_search(p)
print("Profundidade Grafo")
print(result.solution())

result = breadth_first_tree_search(p)
print("Largura Arvore ")
print(result.solution())

result = breadth_first_graph_search(p)
print("Largura Grafo ")
print(result.solution())

result = iterative_deepening_search(p)
print("Aprofundamento Progressivo ")
print(result.solution())

p = ProblemaGrafoNaive('C')
result = depth_first_graph_search(p)
print("Profundidade Grafo")

if result != None:
    print(result.solution())
else:
    print("Sem solução!")
