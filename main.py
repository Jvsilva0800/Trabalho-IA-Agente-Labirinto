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
AZUL = (0, 0, 255)

def desenhar_labirinto(tela, labirinto, fronteira):
    """Desenha o labirinto e destaca a fronteira."""
    for r, linha in enumerate(labirinto):
        for c, valor in enumerate(linha):
            x = c * LARGURA_CELULA
            y = r * ALTURA_CELULA
            if valor == 0:
                pygame.draw.rect(tela, CINZA, (x, y, LARGURA_CELULA, ALTURA_CELULA))
            elif valor == 1:
                pygame.draw.rect(tela, BRANCO, (x, y, LARGURA_CELULA, ALTURA_CELULA))

    # Desenhar os nós da fronteira
    for r, c in fronteira:
        x = c * LARGURA_CELULA
        y = r * ALTURA_CELULA
        pygame.draw.rect(tela, AZUL, (x, y, LARGURA_CELULA, ALTURA_CELULA))

def main():
    my_maze = Maze()
    my_agent = Agent(my_maze)

    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Labirinto")
    clock = pygame.time.Clock()

    start = (4, 11)  # Estado inicial
    goal = (10, 0)   # Estado objetivo
    #bfs_generator = my_agent.bfs(start, goal)
    #dfs_generator = my_agent.dfs(start, goal)
    a_star_generator = my_agent.a_star(start, goal)

    #Loop principal
    # fronteira = []
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     # Atualizar a fronteira a cada iteração da busca
    #     try:
    #         fronteira = next(bfs_generator)  # Obter próxima fronteira
    #     except StopIteration:
    #         pass  # Busca concluída

    #     # Desenhar o labirinto e a fronteira
    #     tela.fill((0, 0, 0))  # Limpar a tela
    #     desenhar_labirinto(tela, my_maze.grid, fronteira)

    #     pygame.display.flip()
    #     clock.tick(8)  # Limitar a 10 FPS para visualizar a expansão

    #   ###################################################################
    
    

    # fronteira = []
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     # Atualizar a fronteira a cada iteração da busca
    #     try:
    #         fronteira = next(dfs_generator)  # Obter próxima fronteira
    #     except StopIteration:
    #         pass  # Busca concluída

    #     # Desenhar o labirinto e a fronteira
    #     tela.fill((0, 0, 0))  # Limpar a tela
    #     desenhar_labirinto(tela, my_maze.grid, fronteira)

    #     pygame.display.flip()
    #     clock.tick(8)  # Limitar a 10 FPS para visualizar a expansão
    #   ########################################################################


    fronteira = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizar a fronteira a cada iteração da busca
        try:
            fronteira = next(a_star_generator)  # Obter próxima fronteira
        except StopIteration:
            pass  # Busca concluída

        # Desenhar o labirinto e a fronteira
        tela.fill((0, 0, 0))  # Limpar a tela
        desenhar_labirinto(tela, my_maze.grid, fronteira)

        pygame.display.flip()
        clock.tick(8)  # Limitar a 10 FPS para visualizar a expansão
    #   ########################################################################

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
    # solution = my_agent.a_star(start, goal)
    # if solution:
    #     print("Solução encontrada:")
    #     for state, action in solution:
    #         print(f"Estado: {state}, Ação: {action}")
    #     print("Número de passos:", len(solution) - 1)
    # else:
    #     print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()
