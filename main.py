import pygame
import sys
from agent import Agent
from maze import Maze

# Configurações da tela
LARGURA_CELULA = 40  # Tamanho de cada célula (pixels)
ALTURA_CELULA = 40
LARGURA_TELA = 640
ALTURA_TELA = 640

# Cores
BRANCO = (255, 255, 255)
CINZA = (190,190,190)
VERMELHO = (255, 0, 0)

def main():

    my_maze = Maze()
    my_agent = Agent(my_maze)

    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Labirinto")
    clock = pygame.time.Clock()

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenhar o labirinto
        for r, linha in enumerate(my_maze.grid):
            for c, valor in enumerate(linha):
                x = c * LARGURA_CELULA
                y = r * ALTURA_CELULA
                if valor == 0:
                    pygame.draw.rect(tela, CINZA, (x, y, LARGURA_CELULA, ALTURA_CELULA))
                elif valor == 1:
                    pygame.draw.rect(tela, BRANCO, (x, y, LARGURA_CELULA, ALTURA_CELULA))

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(30)  # Limitar a 30 FPS


    start = (4, 11)  # Estado inicial
    goal = (10, 0)   # Estado objetivo

    # print("Busca em Largura (BFS):")
    # solution = my_agent.bfs(start, goal)
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

    # print("Busca com Heurística Euclidiana (A*):")
    # solution = agent.a_star(start, goal)
    # if solution:
    #     print("Solução encontrada:")
    #     for state, action in solution:
    #         print(f"Estado: {state}, Ação: {action}")
    #     print("Número de passos:", len(solution) - 1)
    # else:
    #     print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()
