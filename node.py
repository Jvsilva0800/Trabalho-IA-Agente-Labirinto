class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        
        # Estrutura de um nó para armazenar:
        # - state: Estado atual (ex.: posição no labirinto como (linha, coluna)).
        # - parent: Referência ao nó pai.
        # - action: Ação tomada para chegar a este nó (ex.: "UP", "LEFT").
        # - path_cost: Custo acumulado desde o estado inicial.
        
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return (f"Node(state={self.state}, action={self.action}, "
                f"path_cost={self.path_cost})")

    # Método de comparação (menor que)
    def __lt__(self, other):
        return self.path_cost < other.path_cost