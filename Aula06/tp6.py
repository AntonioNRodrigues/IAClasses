from Aula06.jogos_iia import *


class TicTacToe(Game):
    """Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def actions(self, state):
        "Legal moves are any square not yet taken."
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move  ## adiciona jogada ao dicionário (board)
        moves = list(state.moves)
        moves.remove(move)  ## eliminando-a da lista de movimentos possíveis
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("Tabuleiro actual:")
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()
        if self.terminal_test(state):
            print("FIM do Jogo")
        else:
            print("Próximo jogador:{}\n".format(state.to_move))

    def compute_utility(self, board, move, player):
        "If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        "Return true if there is a line through move on board for player."
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k


jogo1 = TicTacToe()
print(jogo1.initial)
jogo1.display(jogo1.initial)

jogo1.jogar(random_player, alphabeta_player)
jogo1.jogar(alphabeta_player, alphabeta_player)


def f_aval_1(estado, jogador):
    tabela = {(1, 1): 2, (1, 2): 1, (1, 3): 2,
              (2, 1): 1, (2, 2): 5, (2, 3): 1,
              (3, 1): 2, (3, 2): 1, (3, 3): 2}
    soma = 0
    for p, j in estado.board.items():
        if j == jogador:
            soma += tabela[p]
        else:
            soma -= tabela[p]
    return soma


def f_aval_2(estado, jogador):
    tabela = {(1, 1): 2, (1, 2): 1, (1, 3): 2,
              (2, 1): 1, (2, 2): 5, (2, 3): 1,
              (3, 1): 2, (3, 2): 1, (3, 3): 2}

    if estado.utility == 1:  # final e ganhou 'X'
        valor = 100 if jogador == 'X' else -100
    elif estado.utility == -1:  # final e ganhou 'O'
        valor = 100 if jogador == 'O' else -100
    elif len(estado.moves) == 0:  # final e empate
        valor = 0
    else:
        soma = 0
        for p, j in estado.board.items():
            if j == jogador:
                soma += tabela[p]
            else:
                soma -= tabela[p]
        valor = soma
    return valor

def f_aval_3(estado, jogador):
    tabela = {(1, 1): 2, (1, 2): 1, (1, 3): 2,
              (2, 1): 1, (2, 2): 5, (2, 3): 1,
              (3, 1): 2, (3, 2): 1, (3, 3): 2}

    if estado.utility == 1:  # final e ganhou 'X'
        valor = 100 if jogador == 'X' else -100
    elif estado.utility == -1:  # final e ganhou 'O'
        valor = 100 if jogador == 'O' else -100
    elif len(estado.moves) == 0:  # final e empate
        valor = 0
    else:
        soma = 0
        for p, j in estado.board.items():
            if j == jogador:
                soma += tabela[p]
            else:
                soma -= tabela[p]
        valor = soma
    return valor


def jogador_alfabeta_1(jogo, estado):
    return alphabeta_cutoff_search(estado, jogo, 3, eval_fn=f_aval_1)


jogo1.jogar(random_player, jogador_alfabeta_1)
