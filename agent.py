from collections import deque
from node import Node

class Agent:
    def __init__(self, maze):
        self.maze = maze

    def bfs(self, start, goal):
        """Implementa a Busca em Largura."""
        # Inicializa a fronteira com o nó inicial
        start_node = Node(state=start, parent=None, action=None, path_cost=0)
        frontier = deque([start_node])  # Fila FIFO para os nós
        explored = set()  # Conjunto de estados explorados

        while frontier:
            # Remove o nó da fronteira
            current_node = frontier.popleft()

            # Verifica se o nó atual contém o estado objetivo
            if current_node.state == goal:
                return self.reconstruct_path(current_node)

            # Adiciona o estado atual aos explorados
            explored.add(current_node.state)

            # Expande o nó atual
            for action, (dx, dy) in zip(["UP", "LEFT", "RIGHT", "DOWN"], [(-1, 0), (0, -1), (0, 1), (1, 0)]):
                next_state = (current_node.state[0] + dx, current_node.state[1] + dy)
                if (
                    self.maze.is_valid_position(*next_state) and
                    next_state not in explored and
                    not any(node.state == next_state for node in frontier)
                ):
                    # Cria o nó filho e adiciona à fronteira
                    child_node = Node(
                        state=next_state,
                        parent=current_node,
                        action=action,
                        path_cost=current_node.path_cost + 1
                    )
                    frontier.append(child_node)
             # Mostra o conteúdo da fronteira
            self.show_frontier(frontier)

        return None  # Se não houver solução
    
    def dfs(self, start, goal):
        """Implementa a Busca em Profundidade."""
        start_node = Node(state=start, parent=None, action=None, path_cost=0)
        frontier = [start_node]  # Pilha para os nós
        explored = set()  # Conjunto de estados explorados

        while frontier:
            # Remove o nó do topo da pilha
            current_node = frontier.pop()

            # Verifica se o nó atual contém o estado objetivo
            if current_node.state == goal:
                return self.reconstruct_path(current_node)

            # Adiciona o estado atual aos explorados
            explored.add(current_node.state)

            # Expande o nó atual (adiciona todos os sucessores na ordem correta)
            for action, (dx, dy) in zip(
                ["UP", "LEFT", "RIGHT", "DOWN"],  # Ordem fixa
                [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Movimentos correspondentes
            ):
                next_state = (current_node.state[0] + dx, current_node.state[1] + dy)

                if (
                    self.maze.is_valid_position(*next_state) and
                    next_state not in explored and
                    not any(node.state == next_state for node in frontier)
                ):
                    # Cria um novo nó e adiciona ao topo da pilha
                    child_node = Node(
                        state=next_state,
                        parent=current_node,
                        action=action,
                        path_cost=current_node.path_cost + 1
                    )
                    frontier.append(child_node)  # Adiciona ao topo da pilha
            # Mostra o conteúdo da fronteira
            self.show_frontier(frontier)

        return None  # Se não encontrar solução
    
    def show_frontier(self, frontier):
        """Exibe o conteúdo atual da fronteira."""
        print("Fronteira atual:")
        for node in frontier:
            print(f"  Estado: {node.state}, Ação: {node.action}, Custo: {node.path_cost}")
        print("-" * 30)

    def reconstruct_path(self, node):
        """Reconstrói o caminho da solução a partir do nó objetivo."""
        path = []
        while node:
            path.append((node.state, node.action))
            node = node.parent
        path.reverse()  # Reverte o caminho para começar no estado inicial
        return path
