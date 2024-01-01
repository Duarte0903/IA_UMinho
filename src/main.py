from Grafos.Graph import *
from ui import *

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
    
    ui = UI(g)

    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_estafetas()

    saida = -1
    while saida != 0:
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
        print("11-Criar estafeta")
        print("12-Ver estafetas")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            print(g.m_graph)
            l = input("Prima Enter para continuar.")
            
        elif saida == 2:
            g.desenha()
            l = input("Prima Enter para continuar.")
        
        elif saida == 3:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("Prima enter para continuar.")
        
        elif saida == 4:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_BFS(inicio, fim))
            l = input("Prima enter para continuar.")
            
        elif saida == 5:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.gulosa(inicio, fim))
            l = input("Prima enter para continuar.")
        
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_aStar(inicio, fim))
            l = input("Prima enter para continuar.")

        elif saida == 7:
            ui.adicionar_cliente()
            l = input("Prima Enter para continuar.")

        elif saida == 8:
            ui.ver_clientes()
            l = input("Prima Enter para continuar.")

        elif saida == 9:
            ui.criar_encomenda()
            l = input("Prima Enter para continuar.")

        elif saida == 10:
            ui.ver_encomendas_pendentes()
            l = input("Prima Enter para continuar.")

        elif saida == 11:
            ui.criar_estafeta()
            l = input("Prima Enter para continuar.")

        elif saida == 12:
            ui.ver_estafetas()
            l = input("Prima Enter para continuar.")
            
        #print("1 - Ver Clientes registados no Sistema")
        #print("2 - Ver Estafetas registados no Sistema")
        #print("3 - Ver Veiculos registados no Sistema")
        #print("4 - Adicionar Estafeta")
        #print("5 - Adicionar Veículo")
        #print("6 - Ver Encomendas do Sistema")
        #print("7 - Ver Entregas Concluídas do Sistema")
        #print("8 - Lançar Entregas Pendentes")
        #print("9 - Ranking dos Estafetas Classificação")
        #print("10 - Ranking dos Estafetas Ecológicos")
        
        #print("1 - Criar Encomenda")
        #print("2 - Lista de Encomendas")
       # print("3 - Lista de Entregas")
        
        elif saida == 0:
            print("Encerrado")
            break

if __name__ == "__main__":
    main()

