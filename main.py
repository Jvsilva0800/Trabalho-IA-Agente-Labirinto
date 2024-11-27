from maze import Maze
from agent import Agent

def main():
    maze = Maze()
    agent = Agent(maze)

    start = (4, 11)  # Estado inicial
    goal = (10, 0)   # Estado objetivo

    # print("Busca em Largura (BFS):")
    # solution = agent.bfs(start, goal)
    # if solution:
    #     print("Solução encontrada:")
    #     for state, action in solution:
    #         print(f"Estado: {state}, Ação: {action}")
    #     print("Número de passos:", len(solution) - 1)
    # else:
    #     print("Nenhuma solução encontrada.")
    # 
    #   ###################################################################

    # print("Busca em Profundidade (DFS):")
    # solution = agent.dfs(start, goal)
    # if solution:
    #     print("Solução encontrada:")
    #     for state, action in solution:
    #         print(f"Estado: {state}, Ação: {action}")
    #     print("Número de passos:", len(solution) - 1)
    # else:
    #     print("Nenhuma solução encontrada.")
    #
    #   ###################################################################

    print("Busca com Heurística Euclidiana (A*):")
    solution = agent.a_star(start, goal)
    if solution:
        print("Solução encontrada:")
        for state, action in solution:
            print(f"Estado: {state}, Ação: {action}")
        print("Número de passos:", len(solution) - 1)
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()
