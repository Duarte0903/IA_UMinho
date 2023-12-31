# - A*

def procura_aStar(g, start, end):
    # open_list é uma lista de nós que foram visitados, mas cujos vizinhos ainda não foram todos inspecionados
    # começa com o nó de início
    # closed_list é uma lista de nós que foram visitados e cujos vizinhos foram inspecionados
    open_list = {start}
    closed_list = set([])

    # g contém as distâncias atuais do nó de início para todos os outros nós
    # o valor padrão (se não for encontrado no mapa) é +infinito
    g = {}  ##  g é apra substiruir pelo peso  ???
    g[start] = 0

    # parents contém um mapa de adjacência de todos os nós
    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        # encontrar um nó com o menor valor de f() - função de avaliação
        n = None
        for v in open_list:
            if n == None or g[v] + g.getH(v) < g[n] + g.getH(n):  # heurística a ser verificada
                n = v
        
        if n == None:
            print('Caminho não existe!')
            return None

        # se o nó atual for o nó de destino
        # então começamos a reconstruir o caminho dele para o nó de início
        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)

            reconst_path.reverse()

            # Retorna o caminho reconstruído e o custo desse caminho
            return (reconst_path, g.calcula_custo(reconst_path))

        # para todos os vizinhos do nó atual
        for (m, weight) in g.getNeighbours(n):  # defina a função getNeighbours que retorna pares de nó-peso
            # se o nó atual não estiver em open_list nem em closed_list
            # adicione-o a open_list e note n como seu pai
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # caso contrário, verifique se é mais rápido primeiro visitar n e depois m
            # e se for, atualize os dados do pai e de g
            # e se o nó estiver em closed_list, mova-o para open_list
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remova n de open_list e adicione-o a closed_list
        # porque todos os seus vizinhos foram inspecionados
        open_list.remove(n)
        closed_list.add(n)

    print('Caminho não existe!')
    return None
    
# - Greedy/Gulosa

def gulosa(g, start, end):
    # open_list é uma lista de nodos visitados, mas com vizinhos
    # que ainda não foram todos visitados, começa com o  start
    open_list = set([start])
    # closed_list é uma lista de nodos visitados
    # e todos os seus vizinhos também já o foram
    closed_list = set([])

    # parents é um dicionário que mantém o antecessor de um nodo
    # começa com start
    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        # encontra nodo com a menor heuristica
        for v in open_list:
            if n == None or g.m_h[v] < g.m_h[n]:
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # se o nodo corrente é o destino
        # reconstruir o caminho a partir desse nodo até ao start
        # seguindo o antecessor
        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)

            reconst_path.reverse()

            return (reconst_path, g.calcula_custo(reconst_path))

        # para todos os vizinhos do nodo corrente
        for (m, weight) in g.getNeighbours(n):
            # Se o nodo corrente não está na open_list nem na closed_list
            # adiciona-lo à open_list e marcar o antecessor
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n

        # remover n da open_list e adiciona-lo à closed_list
        # porque todos os seus vizinhos foram inspecionados
        open_list.remove(n)
        closed_list.add(n)

    print('Caminho não existe!')
    return None
