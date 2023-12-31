from Grafos.Graph import *
from Pesquisas.Informada import *
from Pesquisas.NaoInformada import *
from sistema import *

def main():

    g = Graph()
    g.add_edge("Valdosende", "Balança", 21.7)
    g.add_edge("Valdosende", "Souto", 22.9)
    g.add_edge("Valdosende", "Ribeira", 20.7)
    g.add_edge("Souto", "Gondoriz", 10.9)
    g.add_edge("Ribeira", "Gondoriz", 10.6)
    g.add_edge("Balança", "Gondoriz", 8.9)
    g.add_edge("Souto", "Ribeira", 2.7)
    g.add_edge("Ribeira", "Balança", 1.9)
    g.add_edge("Balança", "Health Planet", 3.7)
    g.add_edge("Balança", "Chorense e Monte", 2.7)
    g.add_edge("Health Planet", "Gondoriz", 5.6)
    g.add_edge("Health Planet", "Chamoim e Vilar", 4.9)
    g.add_edge("Health Planet", "Chorense e Monte", 2)
    g.add_edge("Chorense e Monte", "Chamoim e Vilar", 6.5)
    g.add_edge("Chorense e Monte", "Covide", 11.7)
    g.add_edge("Chorense e Monte", "Rio Caldo", 20.4)
    g.add_edge("Chorense e Monte", "Valdosende", 19.3)
    g.add_edge("Valdosende", "Rio Caldo", 6.7)
    g.add_edge("Rio Caldo", "Covide", 9.3)
    g.add_edge("Rio Caldo", "Vilar da Veiga", 4.3)
    g.add_edge("Covide", "Vilar da Veiga", 13.5)
    g.add_edge("Covide", "Campo do Gerês", 4.5)
    g.add_edge("Covide", "Carvalheira", 7.1)
    g.add_edge("Covide", "Chamoim e Vilar", 5.9)
    g.add_edge("Carvalheira", "Campo do Gerês", 4.5)
    g.add_edge("Carvalheira", "Cibões e Brufe", 16.7)
    g.add_edge("Gondoriz", "Carvalheira", 14.6)
    g.add_edge("Gondoriz", "Cibões e Brufe", 3.9)
    g.add_edge("Gondoriz", "Chamoim e Vilar", 8.2)
    g.add_edge("Chamoim e Vilar", "Carvalheira", 7.1)
    g.add_edge("Cibões e Brufe", "Campo do Gerês", 12.7)
    g.add_edge("Vilar da Veiga", "Campo do Gerês", 16.4) 

    g.add_heuristica("Covide", "Health Planet")
    g.add_heuristica("Souto", "Health Planet")
    g.add_heuristica("Ribeira", "Health Planet")
    g.add_heuristica("Balança", "Health Planet")
    g.add_heuristica("Valdosende", "Health Planet")
    g.add_heuristica("Rio Caldo", "Health Planet")
    g.add_heuristica("Chorense e Monte", "Health Planet")
    g.add_heuristica("Vilar da Veiga", "Health Planet")
    g.add_heuristica("Cibões e Brufe", "Health Planet")
    g.add_heuristica("Gondoriz", "Health Planet")    
    g.add_heuristica("Carvalheira", "Health Planet")
    g.add_heuristica("Chamoim e Vilar", "Health Planet")
    g.add_heuristica("Campo do Gerês", "Health Planet")
    g.add_heuristica("Health Planet", "Health Planet")
    
    sistema = Sistema(g)

    sistema.carregar_clientes()
    sistema.carregar_encomendas_pendentes()

    saida = -1
    while saida != 5:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-DFS")
        print("4-BFS")
        print("5-Gulosa")
        print("6-A*")
        print("7-Adicionar Cliente")
        print("8-Ver clientes")
        print("9-Adicionar Encomenda")
        print("10-Ver encomendas pendentes")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            print(g.m_graph)
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
            
        if saida == 2:
            g.desenha()
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
        
        if saida == 3:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(procura_DFS(g, inicio, fim, path=[], visited=set()))
            l = input("Prima enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
        
        if saida == 4:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(procura_BFS(g, inicio, fim))
            l = input("Prima enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
            
        if saida == 5:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(gulosa(g, inicio, fim))
            l = input("Prima enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
        
        if saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(procura_aStar(g, inicio, fim))
            l = input("Prima enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))

        if saida == 7:
            sistema.adicionar_cliente()
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))

        if saida == 8:
            sistema.ver_clientes()
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))

        if saida == 9:
            sistema.criar_encomenda()
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))

        if saida == 10:
            sistema.ver_encomendas_pendentes()
            l = input("Prima Enter para continuar.")
            saida = int(input("Introduza a sua opcao -> "))
        
        if saida == 0:
            print("Encerrado")
        break

if __name__ == "__main__":
    main()

