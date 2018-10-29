from Aula04.search import *


class EstadoSetas:
    """Um estado do problema da inversao das setas
        Uma lista de 6 setas (e's ou d's), indicando para cada seta se está orientada
        para a esquerda para para a direita
        A ordem da esquerda para a direita corresponde às setas de cima para baixo
    """

    def __init__(self, setas=["e", "e", "e", "d", "d", "d"]):
        self.setas = setas

    def flip(self, seta):
        """ Inversão do sentido de uma seta: de e para d e de d para e"""
        if seta == "e":
            return "d"
        else:
            return "e"

    def inverte(self, n):
        """ Inverte duas setas, na posição n e n+1. A primeira seta está na posição 0
            e para inverter a primeira e a segunda, de cima para baixo, implica n = 0.
            Gera uma nova lista.
        """
        copye = []
        for i in range(len(self.setas)):
            if i == n or i == n + 1:
                copye.append(self.flip(self.setas[i]))
            else:
                copye.append(self.setas[i])
        return EstadoSetas(copye)

    def __str__(self):
        return str(self.setas)

    def __eq__(self, estado):
        """Definir em que circunstância os dois estados são considerados iguais.
        Necessário para os algoritmos de procura em grafo.
        """
        return self.setas == estado.setas

    def __lt__(self, estado):
        return True

    def __hash__(self):
        """Necessário para os algoritmos de procura em grafo."""
        return hash((str(self.setas)))


class ProblemaSetas(Problem):

    def __init__(self, initial=EstadoSetas(["e", "e", "e", "d", "d", "d"])):
        super().__init__(initial)

    def actions(self, estado):
        """ A acção 0 corresponde a inverter as setas de índices 0 e 1 da lista
            A acção 4 coorresponde a inverter as setas de índices 4 e 5, as últimas duas """
        accoes = [0, 1, 2, 3, 4]

        return accoes

    def result(self, estado, acao):
        if acao in self.actions(estado):
            resultante = estado.inverte(acao)
        else:
            raise "Há aqui qualquer coisa mal>> acao não reconhecida"

        return resultante

    def goal_test(self, estado):
        """Um estado é final se um for um dos 2 casos de setas com orientacoes alternadas
        """
        return (estado.setas == ["e", "d", "e", "d", "e", "d"]) or (estado.setas == ["d", "e", "d", "e", "d", "e"])

    def menor_distancia(self, no):
        cust_st1 = 0
        cust_st2 = 0
        final_st1 = ["e", "d", "e", "d", "e", "d"]
        final_st2 = ["d", "e", "d", "e", "d", "e"]
        list = no.state.setas

        for i in range(len(list)):
            if list[i] != final_st1[i]:
                cust_st1 += 1
            if list[i] != final_st2[i]:
                cust_st2 += 1

        return min(cust_st1, cust_st2)


x = EstadoSetas()
print(x)

x = EstadoSetas(["d", "e", "d", "d", "d", "e"])
print(x)

print("x antes:")
print(x)
y = x.inverte(1)
print("x depois")
print(x)
print("y: Como ficam depois da inversão da segunda e terceira setas:")
print(y)

z = y.inverte(1)
print(z)
print(x)
print(x == z)

p = ProblemaSetas()
print(p.initial)

# resultado = depth_first_tree_search(p)
# print(resultado.solution())### Largura (árvore)

resultado = breadth_first_tree_search(p)
print("Largura arvore ::breadth_first_tree_search")
print(resultado.solution())

resultado = breadth_first_graph_search(p)
print("Largura grafo ::breadth_first_graph_search")
print(resultado.solution())

resultado = depth_first_graph_search(p)
print("Profundidade grafo ::depth_first_graph_search")
print(resultado.solution())

resultado = uniform_cost_search(p)
print("Custo Uniforme :: uniform_cost_search")
print(resultado.solution())

resultado = iterative_deepening_search(p)
print("Aprofundamento progressivo:: iterative_deepening_search")
print(resultado.solution())

resultado = uniform_cost_search(p)
print("Custo Uniforme:: uniform_cost_search")
print(resultado.solution())

resultado = astar_search(p, p.menor_distancia)
print("A*:: astar_search")
print(resultado.solution())

print(
    "Para a euristica ser admissivel: para cada estado o v.Heuristicos tem de ser menor ou igual do que a sua distancia ao objectivo. Por ex se tiversmos "
    "[e, e, d, e, d, d] a heuristica deste estado é 4 e o custo é 2 logo 4 não é menor ou igual que 2")
