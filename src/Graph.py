# Classe grafo para representaçao de grafos,
import math
from queue import Queue

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
        
# - __str__: escrever o grafo como string
# - Return: Uma string representando o grafo
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
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

# - get_arc_cost: devolver o custo de uma aresta
    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

# - desenha: Desenha graficamente o grafo
# - Funcionamento: Usa a biblioteca NetworkX para criar e desenhar o grafo com base nos nós e arestas armazenados no dicionário m_graph
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