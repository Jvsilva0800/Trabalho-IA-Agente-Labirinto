
# Resolução de Labirintos com Algoritmos de Busca

A resolução de labirintos é um problema clássico em computação e inteligência artificial (IA), amplamente utilizado para ilustrar conceitos fundamentais de algoritmos de busca e grafos. Este problema possui aplicações práticas em diversas áreas, como:
- **Robótica**: Navegação autônoma.
- **Jogos**: Pathfinding em mapas complexos.
- **Redes**: Otimização de caminhos em grafos e redes.

Este projeto tem como objetivo implementar três algoritmos de busca bem estabelecidos: 
1. **Busca em Largura (BFS)**: Explora os nós camada por camada, garantindo a solução mais curta em grafos não ponderados.
2. **Busca em Profundidade (DFS)**: Adota uma abordagem de exploração profunda, mas pode não ser ótima em termos de custo.
3. **A* (A-Estrela)**: Combina custo acumulado e heurística para priorizar a expansão de nós mais promissores, sendo amplamente utilizado em aplicações práticas devido à sua eficiência.

## Visualização Interativa

A interface gráfica foi desenvolvida utilizando a biblioteca **pygame**, permitindo:
- **Seleção do algoritmo de busca** pelo usuário.
- **Visualização em tempo real** da expansão da fronteira durante a busca.
- **Exibição do caminho encontrado**, destacando as etapas de execução.

Essa funcionalidade torna o projeto não apenas uma ferramenta prática, mas também uma abordagem didática para o ensino e aprendizado de algoritmos de busca.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Biblioteca Gráfica**: pygame
- **Estruturas de Dados**: Filas, pilhas e fila de prioridade (heapq)

