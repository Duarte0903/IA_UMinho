from Grafos.Graph import *
from ui import *

def menu_clientes(ui):
    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_encomendas_entregues
    ui.carregar_estafetas()
    saida = -1
    while saida != 0:
        print("1-Adicionar Cliente")
        print("2-Ver clientes")
        print("3-Avaliar Entrega")
        print("0-Sair")

        saida = int(input("Escolha uma opção -> "))
        if saida == 1:
            ui.adicionar_cliente()
            l = input("Prima Enter para continuar.")
        elif saida == 2:
            ui.ver_clientes()
            l = input("Prima Enter para continuar.")
        elif saida == 3:
            ui.ver_clientes()
            l = input("Prima Enter para continuar.")
        elif saida == 0:
            print("Encerrado")
            break
        
def menu_algoritmos(g):
    saida = -1
    while saida != 0:
        print("1-DFS")
        print("2-BFS")
        print("3-Gulosa")
        print("4-A*")
        print("0-Sair")
        
        saida = int(input("Escolha uma opção -> "))
        if saida == 1:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("Prima enter para continuar.")
        
        elif saida == 2:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_BFS(inicio, fim))
            l = input("Prima enter para continuar.")
            
        elif saida == 3:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            g.add_heuristica_general(fim)
            print(g.gulosa(inicio, fim))
            l = input("Prima enter para continuar.")
        
        elif saida == 4:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            g.add_heuristica_general(fim)
            print(g.procura_aStar(inicio, fim))
            l = input("Prima enter para continuar.")
        
        elif saida == 0:
            print("Encerrado")
            break
        
def menu_grafos(g):
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            print(g.m_graph)
            l = input("Prima Enter para continuar.")
            
        elif saida == 2:
            n1 = input("Insira o nodo -> ")
            g.desenha(n1)
            l = input("Prima Enter para continuar.")
        elif saida == 0:
            print("Encerrado")
            break
        
def menu_estafetas(ui):
    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_encomendas_entregues
    ui.carregar_estafetas()
    saida = -1
    while saida != 0:
        print("1-Criar estafeta")
        print("2-Ver estafetas")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            ui.criar_estafeta()
            l = input("Prima Enter para continuar.")

        elif saida == 2:
            ui.ver_estafetas()
            l = input("Prima Enter para continuar.")
            
        elif saida == 0:
            print("Encerrado")
            break
        
def menu_encomendas(ui):
    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_encomendas_entregues
    ui.carregar_estafetas()
    saida = -1
    while saida != 0:
        print("1-Adicionar Encomenda")
        print("2-Ver encomendas pendentes")
        print("3-Ver encomendas entregues")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            ui.criar_encomenda()
            l = input("Prima Enter para continuar.")

        elif saida == 2:
            ui.ver_encomendas_pendentes()
            l = input("Prima Enter para continuar.")
        
        elif saida == 3:
            ui.ver_encomendas_entregues()
            l = input("Prima Enter para continuar.")
            
        elif saida == 0:
            print("Encerrado")
            break
        
def menu_entregas(ui):
    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_encomendas_entregues
    ui.carregar_estafetas()
    saida = -1
    while saida != 0:
        print("1-Efetuar Entrega")
        print("2-Ver entregas")
        print("0-Sair")

        saida = int(input("Introduza a sua opcao -> "))
        if saida == 1:
            l = input("Prima Enter para continuar.")

        elif saida == 2:
            l = input("Prima Enter para continuar.")
            
        elif saida == 0:
            print("Encerrado")
            break

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
    
    ui = UI(g)

    ui.carregar_clientes()
    ui.carregar_encomendas_pendentes()
    ui.carregar_encomendas_entregues
    ui.carregar_estafetas()

    saida = -1
    while saida != 0:
        print("1-Menu Clientes")
        print("2-Menu Algoritmos")
        print("3-Menu Grafos")
        print("4-Menu Estafetas")
        print("5-Menu Encomendas")
        print("6-Menu Entregas")
        print("0-Sair")

        saida = int(input("Escolha uma opção -> "))
        if saida == 1:
            menu_clientes(ui)
        elif saida == 2:
            menu_algoritmos(g)
        elif saida == 3:
            menu_grafos(g)
        elif saida == 4:
            menu_estafetas(ui)
        elif saida == 5:
            menu_encomendas(ui)
        elif saida == 5:
            menu_entregas(ui)
        elif saida == 0:
            print("Encerrado")
            break

if __name__ == "__main__":
    main()