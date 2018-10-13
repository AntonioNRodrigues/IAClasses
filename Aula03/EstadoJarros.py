from Aula03.search import *


class EstadoJarros:
    """Um estado do problema dos 2 jarros é um par de jarros, em que cada jarro
    é representado por um par (capacidade,quantidade).
    """

    def __init__(self, jarros=((3, 0), (5, 0))):
        self.jarros = jarros

    def jarro_cheio(self, num):
        """Método para verificar se um dado jarro está cheio.
        O número do jarro é 1 ou 2.
        """
        capacidade, quantidade = self.jarros[num - 1]
        return capacidade == quantidade

    def jarro_vazio(self, num):
        """Método para verificar se um dado jarro está vazio.
        O número do jarro é 1 ou 2.
        """
        _, quantidade = self.jarros[num - 1]
        return quantidade == 0

    def __str__(self):
        return str(self.jarros)

    def __eq__(self, estado):
        """Definir em que circunstância os dois estados são considerados iguais.
        Necessário para os algoritmos de procura em grafo.
        """
        return self.jarros == estado.jarros

    def __hash__(self):
        """Necessário para os algoritmos de procura em grafo."""
        return hash((self.jarros[0], self.jarros[1]))


class ProblemaJarros(Problem):

    def __init__(self, inicial=EstadoJarros(), vamos_medir=4):
        super().__init__(inicial)
        self.vamos_medir = vamos_medir

    def actions(self, estado):
        accoes = list()
        if not estado.jarro_cheio(1):
            accoes.append("encher jarro 1")
        if not estado.jarro_cheio(2):
            accoes.append("encher jarro 2")
        if not estado.jarro_vazio(1):
            accoes.append("esvaziar jarro 1")
        if not estado.jarro_vazio(2):
            accoes.append("esvaziar jarro 2")
        if not estado.jarro_vazio(1) and not estado.jarro_cheio(2):
            accoes.append("verter de 1 para 2")
        if not estado.jarro_vazio(2) and not estado.jarro_cheio(1):
            accoes.append("verter de 2 para 1")
        return accoes

    def result(self, estado, acao):
        cap1, quant1 = estado.jarros[0]
        cap2, quant2 = estado.jarros[1]

        if acao == "encher jarro 1":
            resultante = EstadoJarros(((cap1, cap1), (cap2, quant2)))
        elif acao == "encher jarro 2":
            resultante = EstadoJarros(((cap1, quant1), (cap2, cap2)))
        elif acao == "esvaziar jarro 1":
            resultante = EstadoJarros(((cap1, 0), (cap2, quant2)))
        elif acao == "esvaziar jarro 2":
            resultante = EstadoJarros(((cap1, quant1), (cap2, 0)))
        elif acao == "verter de 1 para 2":
            em2 = min(cap2, quant1 + quant2)
            resultante = EstadoJarros(((cap1, quant1 + quant2 - em2), (cap2, em2)))
        elif acao == "verter de 2 para 1":
            em1 = min(cap1, quant1 + quant2)
            resultante = EstadoJarros(((cap1, em1), (cap2, quant1 + quant2 - em1)))
        else:
            raise "Há aqui qualquer coisa mal>> acao não reconhecida"

        return resultante

    def goal_test(self, estado):
        """Um estado é final se um dos seus jarros tiver uma quantidade igual
        àquela que se pretende medir
        """
        return estado.jarros[0][1] == self.vamos_medir or \
               estado.jarros[1][1] == self.vamos_medir

    def path_cost(self, c, state1, action, state2):
        return c + state1.jarros[0][1] - state2.jarros[0][1]


prob_jarros = ProblemaJarros()
print(prob_jarros.initial)
print(prob_jarros.vamos_medir)
medida1 = depth_first_graph_search(prob_jarros)
print(medida1.solution())
print(medida1.path())
print(medida1.path_cost())

jarros2 = ((7, 0), (5, 0))
estadoJarros = EstadoJarros(jarros2)
prob_jarros2 = ProblemaJarros(estadoJarros, 3)
print(prob_jarros2.initial)
print(prob_jarros2.vamos_medir)
medida2 = depth_first_graph_search(prob_jarros2)
print(medida2.solution())
print(medida2.path())

jarros3 = ((7, 0), (8, 0))
estadoJarros3 = EstadoJarros(jarros3)
prob_jarros3 = ProblemaJarros(estadoJarros3, 4)
print(prob_jarros3.initial)
print(prob_jarros3.vamos_medir)
medida3 = depth_first_graph_search(prob_jarros3)

print(medida3.solution())
print(medida3.depth)
print(medida3.path())