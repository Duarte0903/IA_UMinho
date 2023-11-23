from Graph import Graph

def main():
    g = Graph()

    g.add_edge("Health Planet", "Souto", 0)
    g.add_edge("Health Planet", "Ribeira", 0)
    g.add_edge("Health Planet", "Balança", 0)
    g.add_edge("Health Planet", "Chorense e Monte", 0)
    g.add_edge("Health Planet", "Valdosende", 0)
    g.add_edge("Souto", "Ribeira", 0)
    g.add_edge("Ribeira", "Balança", 0)
    g.add_edge("Balança", "Moimenta", 0)
    g.add_edge("Balança", "Chorense e Monte", 0)
    
    g.add_edge("Moimenta", "Gondoriz", 0)
    g.add_edge("Moimenta", "Chamoim e Vilar", 0)
    g.add_edge("Moimenta", "Chorense e Monte", 0)
    g.add_edge("Chorense e Monte", "Chamoim e Vilar", 0)
    g.add_edge("Chorense e Monte", "Covide", 0)
    g.add_edge("Chorense e Monte", "Rio Caldo", 0)
    g.add_edge("Chorense e Monte", "Valdosende", 0)
    g.add_edge("Valdosende", "Rio Caldo", 0)
    g.add_edge("Rio Caldo", "Covide", 0)
    
    g.add_edge("Rio Caldo", "Vilar da Veiga", 0)
    g.add_edge("Covide", "Vilar da Veiga", 0)
    g.add_edge("Covide", "Campo do Gerês", 0)
    g.add_edge("Covide", "Carvalheira", 0)
    g.add_edge("Covide", "Chamoim e Vilar", 0)
    g.add_edge("Carvalheira", "Campo do Gerês", 0)
    g.add_edge("Carvalheira", "Cibões e Brufe", 0)
    g.add_edge("Gondoriz", "Carvalheira", 0)
    g.add_edge("Gondoriz", "Cibões e Brufe", 0)
    g.add_edge("Gondoriz", "Chamoim e Vilar", 0)
    g.add_edge("Chamoim e Vilar", "Carvalheira", 0)
    
    

    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            print(g.m_graph)
            l = input("Prima Enter para continuar.")
        elif saida == 2:
            g.desenha()
            l = input("Prima Enter para continuar.")
        elif saida == 3:
            print("Encerrado")
            break

if __name__ == "__main__":
    main()

