from Aula03.search import *


class ProblemaTeoricas_1(Problem):
    grafo = {'I': ['A', 'B'],
             'A': ['C', 'D', 'I'],
             'B': ['D', 'F', 'I'],
             'C': [],
             'D': ['C', 'F'],
             'F': []}

    def actions(self, estado):
        sucessores = self.grafo[estado]
        accoes = map(lambda x: "ir de {} para {}".format(estado, x), sucessores)
        return list(accoes)

    def result(self, estado, accao):
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]


# call problem
problema_1 = ProblemaTeoricas_1('I', 'F')
print(problema_1.actions('I'))

# loop all keys
for key in problema_1.grafo:
    print(problema_1.actions(key))

result = breadth_first_search(problema_1)
print(result)
print(result.path())
print(result.solution())
print("-----------------------------------------------")


class ProblemaTeoricas_1_with_costs(Problem):
    grafo = {'I': {'A': 2, 'B': 5},
             'A': {'C': 2, 'D': 4, 'I': 2},
             'B': {'D': 1, 'F': 5, 'I': 5},
             'C': {},
             'D': {'C': 3, 'F': 2},
             'F': {}}

    def actions(self, state):
        sucessores = self.grafo[state]
        accoes = map(lambda x: "ir de {} para {}".format(state, x), sucessores)
        return list(accoes)

    def result(self, estado, accao):
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]

    def path_cost(self, c, state1, action, state2):
        return c + self.grafo[state1][state2]


# call problem
problema_2 = ProblemaTeoricas_1_with_costs('I', 'F')
print(problema_2.actions('I'))

# loop all keys
for key in problema_2.grafo:
    print(problema_2.actions(key))

result = breadth_first_search(problema_2)
print(result)
print(result.path())
print(result.solution())
print(result.path_cost)
print("-----------------------------------------------")

r_ucs = uniform_cost_search(problema_2)
print(r_ucs.state)
print(r_ucs.parent)
print(r_ucs.action)
print(r_ucs.path_cost)
print(r_ucs.depth)
print(r_ucs.solution())
