# Classe grafo para representaçao de grafos,
import math
from queue import Queue

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
        lista = []  
        
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))  
        
        return lista 
    
    def add_heuristica(self, node1, node2):
        coord1 = self.get_coord_by_name(node1)
        coord2 = self.get_coord_by_name(node2)
        
        if coord1 is not None and coord2 is not None:
            distancia_km = geodesic(coord1, coord2).kilometers
            distancia_int = round(distancia_km,3)
            self.m_h[node1] = distancia_int
            return distancia_int
        else:
            print("Coordenadas não encontradas para calcular a heurística.")


    def get_coord_by_name(self, name):
        coordenadas = {
            "Health Planet": (41.71807978492159, -8.30917203803056),
            "Balança": (41.704898431813334, -8.321451365436666),
            "Covide": (41.73746645742784, -8.213419535956106),
            "Souto": (41.69798855136702, -8.34528975491547),
            "Ribeira": (41.697042171877975, -8.32928045699718),
            "Valdosende": (41.65456719741683, -8.222147650257954),
            "Rio Caldo": (41.6782800365772, -8.184467528752261),
            "Chorense e Monte": (41.70991309207952, -8.304550695299849),
            "Vilar da Veiga": (41.703049799112755, -8.16645961862092),
            "Chamoim e Vilar": (41.734604350198396, -8.27073986996217),
            "Gondoriz": (41.73414387416662, -8.302094615042998),
            "Carvalheira": (41.746663597981545, -8.236168994389564),
            "Campo do Gerês": (41.758671476196184, -8.199980773826091),
            "Cibões e Brufe": (41.7438212353067, -8.280861241830227)
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

    def desenha(self,n1):
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        
        for nodo in lista_v:
            n = nodo.getName()
            heuristica = self.add_heuristica(n,n1)  
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

    def procura_DFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path,round(custoT,1),visited)
        
        for (adjacente,peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente,end,path,visited)
                if resultado is not None:
                    return resultado
        
        path.pop()
        return None

    def procura_BFS(self, start, end):
        visited = set()
        fila = Queue()
        custo = 0
        fila.put(start)
        visited.add(start)

        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente,peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()

            # função que calcula o custo do caminho
            custo = self.calcula_custo(path)
        return (path,round(custo,1),visited)  

    def procura_aStar(self, start, end):
        open_list = {start}
        closed_list = set([])

        g = {}  

        g[start] = 0

        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if (n == None) or (g[v] + self.getH(v) < g[n] + self.getH(n)):  
                    n = v
            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, round(self.calcula_custo(reconst_path),1),closed_list)

            for (m, weight) in self.getNeighbours(n): 
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
        
    def gulosa(self, start, end):
        open_list = set([start])
        closed_list = set([])

        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, round(self.calcula_custo(reconst_path),1),closed_list)
            
            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
    def add_heuristica_general(self, n1):
        lista_v = self.m_nodes
        
        for nodo in lista_v:
            n = nodo.getName()
            self.add_heuristica(n,n1)  