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

    start = (4, 11)  # Estado inicial
    goal = (10, 0)   # Estado objetivo

    # Solicitar escolha do algoritmo ao usuário
    print("Escolha o algoritmo de busca:")
    print("1 - BFS (Busca em Largura)")
    print("2 - DFS (Busca em Profundidade)")
    print("3 - A* (Busca com Heurística)")
    escolha = input("Digite o número do algoritmo desejado: ")

    if escolha == "1":
        generator = my_agent.bfs(start, goal)
        algoritmo = "BFS"
    elif escolha == "2":
        generator = my_agent.dfs(start, goal)
        algoritmo = "DFS"
    elif escolha == "3":
        generator = my_agent.a_star(start, goal)
        algoritmo = "A*"
    else:
        print("Opção inválida. Encerrando o programa.")
        return

    print(f"Executando {algoritmo}...")

    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Labirinto")
    clock = pygame.time.Clock()
    
    fronteira = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizar a fronteira a cada iteração da busca
        try:
            fronteira = next(generator)  # Obter próxima fronteira
        except StopIteration:
            pass  # Busca concluída

        # Desenhar o labirinto e a fronteira
        tela.fill((0, 0, 0))  # Limpar a tela
        desenhar_labirinto(tela, my_maze.grid, fronteira)

        pygame.display.flip()
        clock.tick(8)  # Limitar a 8 FPS para visualizar a expansão
    


if __name__ == "__main__":
    main()
