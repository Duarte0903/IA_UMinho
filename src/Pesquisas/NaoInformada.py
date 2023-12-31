# - Procura DFS

def procura_DFS(g, start, end, path=[], visited=set()):
    # - start: Nó de início da busca.
    # - end: Nó de destino da busca.
    # - path=[]: Lista que armazena o caminho percorrido durante a busca.
    # - visited=set(): Conjunto que registra os nós visitados para evitar loops infinitos.
    # Adiciona o nó inicial à lista de caminho e ao conjunto de visitados
    path.append(start)
    visited.add(start)
    # Verifica se o nó atual é o nó de destino
    if start == end:
        # Calcula o custo do caminho percorrido até agora usando a função calcula_custo do objeto g
        custoT = g.calcula_custo(path)
        # Retorna o caminho e seu custo
        return (path, custoT)
    
    # Para cada nó adjacente ao nó atual no grafo
    for (adjacente, g.peso) in g.m_graph[start]:
        # Verifica se o nó adjacente não foi visitado
        if adjacente not in visited:
            # Continua a busca a partir do nó adjacente chamando recursivamente a função procura_DFS
            resultado = procura_DFS(g, adjacente, end, path, visited)
            # Se encontrar o nó de destino a partir de um dos nós adjacentes, retorna o caminho e seu custo
            if resultado is not None:
                return resultado
    
    # Se nenhum nó adjacente não visitado leva ao nó de destino, remove o nó atual do caminho para retroceder na busca
    path.pop()
    # Se nenhum caminho válido for encontrado, retorna None
    return None

# - Procura BFS

def procura_BFS(g, start, end):
    # Define um conjunto de nós visitados para evitar ciclos
    visited = set()
    # Cria uma fila para a busca em largura
    fila = Queue()
    custo = 0

    # Adiciona o nó inicial à fila e marca como visitado
    fila.put(start)
    visited.add(start)

    # Um dicionário para armazenar os pais dos nós visitados para reconstruir o caminho
    parent = dict()
    parent[start] = None

    # Variável para indicar se o caminho foi encontrado
    path_found = False

    # Enquanto a fila não estiver vazia e o caminho não foi encontrado
    while not fila.empty() and path_found == False:
        # Obtém o próximo nó na fila
        nodo_atual = fila.get()
        
        # Verifica se o nó atual é o nó de destino
        if nodo_atual == end:
            path_found = True
        else:
            # Para cada nó adjacente ao nó atual no grafo
            for (adjacente, g.peso) in g.m_graph[nodo_atual]:
                # Verifica se o nó adjacente não foi visitado
                if adjacente not in visited:
                    # Adiciona o nó adjacente à fila, marca-o como visitado e define seu nó pai
                    fila.put(adjacente)
                    parent[adjacente] = nodo_atual
                    visited.add(adjacente)

    # Reconstrói o caminho se encontrado
    path = []
    if path_found:
        path.append(end)
        # Reconstrói o caminho percorrendo os pais dos nós visitados
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
        # Calcula o custo do caminho utilizando a função calcula_custo do objeto g
        custo = g.calcula_custo(path)
    return (path, custo)