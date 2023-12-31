# Classe grafo para representaçao de grafos,
import math

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from geopy.distance import geodesic

from Grafos.Node import *

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
    
    def add_heuristica(self, node1, node2):
        coord1 = self.get_coord_by_name(node1)
        coord2 = self.get_coord_by_name(node2)
        
        if coord1 is not None and coord2 is not None:
            distancia_km = geodesic(coord1, coord2).kilometers
            distancia_int = round(distancia_km)
            self.m_h[node1] = distancia_int
        else:
            print("Coordenadas não encontradas para calcular a heurística.")


    def get_coord_by_name(self, name):
        coordenadas = {
            "Health Planet": (41.719444, -8.298333),
            "Balança": (41.7025, -8.311389),
            "Covide": (41.738611, -8.213889 ),
            "Souto": (41.693333, -8.343056),
            "Ribeira": (41.696389, -8.330833),
            "Valdosende": (41.667778, -8.233056),
            "Rio Caldo": (41.677222, -8.197222),
            "Chorense e Monte": (41.7, -8.271667),
            "Vilar da Veiga": (41.745556, -8.169722),
            "Chamoim e Vilar": (41.723611, -8.2625),
            "Gondoriz": (41.735278, -8.301944),
            "Carvalheira": (41.746389, -8.234444),
            "Campo do Gerês": (41.759167, -8.195),
            "Cibões e Brufe": (41.754167, -8.26)
        }
        
        return coordenadas.get(name)
    
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
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        
        for nodo in lista_v:
            n = nodo.getName()
            heuristica = self.getH(n)  
            g.add_node(n, heuristic=heuristica, label=n) 
            
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        
        node_labels = {}
        for node, position in pos.items():
            x, y = position
            node_labels[node] = (x, y + 0.05)
            
        nx.draw_networkx_nodes(g, pos, node_size=500)
        nx.draw_networkx_edges(g, pos)
        
        node_labels_combined = {node: f"{node}\nHeurística: {g.nodes[node]['heuristic']}" for node in g.nodes()}
        nx.draw_networkx_labels(g, node_labels, labels=node_labels_combined, font_color='black', font_weight='bold')
        
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
        
        plt.axis('off')
        plt.show()