import networkx as nx
import matplotlib.pyplot as plt

# Plotagem da matriz inicial


def plotaMatriz(matriz):
    # Obter rótulos para as colunas da matriz (para diferenciar dos números das disciplinas)
    rotulos_colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                       'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']

    # Cria um objeto de grafo
    G = nx.Graph()

    # Adiciona as arestas ao grafo com os pesos correspondentes
    num_linhas, num_colunas = matriz.shape
    for i in range(num_linhas):
        for j in range(num_colunas):
            peso = matriz[i][j]
            if peso > 0:
                vertice_linha = i
                vertice_coluna = rotulos_colunas[j]
                G.add_edge(vertice_linha, vertice_coluna, weight=peso)

    # Define o layout do grafo
    pos = nx.spring_layout(G)

    # Obtém os pesos das arestas
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Plota o grafo
    nx.draw_networkx(G, pos, with_labels=True,
                     node_color='lightblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Exibe o gráfico
    plt.axis('off')
    plt.show()

# Plotagem do grafo de restrição, similar à uma coloração de arestas, onde disciplinas adjacentes e com demais restrições não podem ter mesmo dia e horário


def plotaGrafoRestricao(grafo):
    num_horarios = max([max(linha) for linha in grafo]) + 1
    # Função de coloração para melhor visualização do grafo

    def coloracao(grafo, num_horarios):
        num_disciplinas = len(grafo)
        cores = [-1] * num_disciplinas
        cores_disponiveis = [True] * num_horarios
        cores[0] = 0
        # Itera sobre os vértices pintando-os conforme disponibilidade
        for u in range(1, num_disciplinas):
            for i in grafo[u]:
                if cores[i] != -1:
                    cores_disponiveis[cores[i]] = False

            cor_disponivel = next(cor for cor in range(
                num_horarios) if cores_disponiveis[cor])
            cores[u] = cor_disponivel

            for i in range(num_horarios):
                cores_disponiveis[i] = True

        return cores

    # Atribuição das cores aos vértices
    cores_atribuidas = coloracao(grafo, num_horarios)

    # Mapeamento dos rótulos dos vértices para cores
    cores_dict = {i: cor for i, cor in enumerate(cores_atribuidas)}

    # Criação do grafo
    G = nx.DiGraph()

    # Adicionando vértices e arestas no grafo
    for i, adjacencias in enumerate(grafo):
        G.add_edges_from([(i, adj) for adj in adjacencias])

    # Define o layout do grafo
    pos = nx.spring_layout(G)

    # Plotagem
    nx.draw_networkx(G, pos, node_color=[cores_dict[node]
                     for node in G.nodes()], node_size=500)

    # Exibe o gráfico
    plt.show()

# Plotagem final, com disciplinas ligando aos seus horários, representa um grafo bipartido


def plotaAtribuicoes(atribuicoes):
    # Cria um grafo
    G = nx.DiGraph()

    # Adiciona as chaves como nós de um conjunto
    chaves = set(atribuicoes.keys())
    G.add_nodes_from(chaves, bipartite=0)

    # Adiciona os valores como nós do outro conjunto
    valores = set(valor for lista in atribuicoes.values() for valor in lista)
    G.add_nodes_from(valores, bipartite=1)

    # Adiciona as arestas do dicionário
    for chave, lista_valores in atribuicoes.items():
        G.add_edges_from([(chave, valor) for valor in lista_valores])

    # Define o layout como bipartido
    pos_chaves = nx.bipartite_layout(G, chaves)

    # Plota o grafo
    nx.draw_networkx_nodes(G, pos_chaves, nodelist=chaves,
                           node_color='lightblue', node_size=500)
    nx.draw_networkx_nodes(G, pos_chaves, nodelist=valores,
                           node_color='lightgreen', node_size=500)
    nx.draw_networkx_edges(G, pos_chaves, width=1.0, alpha=0.5, arrowsize=10)
    nx.draw_networkx_labels(G, pos_chaves, font_size=10,
                            font_family='sans-serif')
    plt.axis('off')
    plt.show()
