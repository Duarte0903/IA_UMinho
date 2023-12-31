# Classe grafo para representaçao de grafos,
import math

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from Node import Node

class Graph:
    
# - __init__: Inicializa um novo objeto Graph
# - directed: determina se o grafo é direcionado
    def __init__(self, directed=False):
        self.m_nodes = []               # - Lista dos nós do grafo
        self.m_directed = directed      # - Indica se o grafo é direcionado
        self.m_graph = {}               # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -< pesquisa info
        
# - __str__: escrever o grafo como string
# - Return: Uma string representando o grafo
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
# - Encontrar nodo pelo nome

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None
    
# - imprime_aresta: imprimir arestas
# - return: uma string representando todas as arestas do grafo
    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

# - add_edge: adicionar aresta no grafo
# - Cria nodos se não existirem, adiciona as arestas e pesos aos nodos correspondentes no dicionário m_graph
    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []

        self.m_graph[node1].append((node2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
              self.m_graph[node2].append((node1, weight))

# - getNodes: Retorna a lista de nós do grafo
    def getNodes(self):
        return self.m_nodes
    
# - getNeighbours é responsável por retornar uma lista de vizinhos de um determinado nó dentro do grafo
    
    def getNeighbours(self, nodo):
        lista = []  # Inicializa uma lista vazia para armazenar os vizinhos do nó
        
        # Itera sobre os vizinhos (adjacentes) e seus pesos no grafo associado ao nó fornecido
        for (adjacente, peso) in self.m_graph[nodo]:
        
            # Adiciona o vizinho atual à lista de vizinhos com seu respectivo peso
            lista.append((adjacente, peso))  
        
        # Retorna a lista de vizinhos do nó fornecido
        return lista 
    
# - add_heuristica: define heuristica para cada nodo

    def add_heuristica(self, n, estima):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima
    
# - heuristica: define heuristica para cada nodo 1 por defeito

    def heuristica(self):
        nodos = self.m_graph.keys
        for n in nodos:
            self.m_h[n] = 1
        return (True)
    
# - calcula_est: recebe um dicionário de estimativas e retorna a chave (nó) associada à menor estimativa presente no dicionário
    
    def calcula_est(self, estima):
        # Transforma as chaves do dicionário 'estima' em uma lista
        l = list(estima.keys())
        # Inicializa a variável 'min_estima' com o valor da primeira estimativa
        min_estima = estima[l[0]]
        # Inicializa a variável 'node' com a chave correspondente à primeira estimativa
        node = l[0]
        
        # Percorre todas as chaves e valores do dicionário 'estima'
        for k, v in estima.items():
            # Verifica se o valor atual é menor do que o valor mínimo encontrado até agora
            if v < min_estima:
                # Se for menor, atualiza o valor mínimo e o nó correspondente
                min_estima = v
                node = k
                
        # Retorna o nó associado à estimativa mínima encontrada no dicionário
        return node
    
# - Devolve heuristica do nodo

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])

# - responsável por recuperar o custo de uma aresta entre dois nós específicos no grafo

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

# - retorna o custo de um determinado caminho 

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo 

# - desenha: Desenha graficamente o grafo

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()