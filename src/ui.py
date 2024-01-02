from Entregas.Entregas import Entrega
from Grafos.Graph import *
from Cliente.Cliente import Cliente
from Encomendas.Encomenda import Encomenda
from Estafeta.Estafeta import Estafeta
from Veiculos.Bicicleta import *
from Veiculos.Mota import *
from Veiculos.Carro import *
import os
from pathlib import Path 
import random
import string

class UI:

    def __init__ (self, graph):
        self.graph = graph
        self.m_Encomendas = {}  
        self.m_Estafetas = {}           
        self.m_Clientes = []                   
        self.m_encomendas_pendentes = []       
        self.m_encomendas_entregues = []    

    ###ficheiros###

    diretoria_atual = os.getcwd()

    pastaEncomendas = os.path.join(diretoria_atual, 'Encomendas')
    pastaClientes = os.path.join(diretoria_atual, 'Clientes')
    pastaEntregas = os.path.join(diretoria_atual, 'Entregas')
    pastaEstafetas = os.path.join(diretoria_atual, 'Estafetas')
    pastaVeiculos = os.path.join(diretoria_atual, 'Veiculos')

        
    if not os.path.exists(pastaEncomendas):
        os.makedirs(pastaEncomendas)

    if not os.path.exists(pastaClientes):
        os.makedirs(pastaClientes)

    if not os.path.exists(pastaEntregas):
        os.makedirs(pastaEntregas)

    if not os.path.exists(pastaEstafetas):
        os.makedirs(pastaEstafetas)

    if not os.path.exists(pastaVeiculos):
        os.makedirs(pastaVeiculos)

    encomendas_entregues = os.path.join(pastaEncomendas, 'Encomendas_Entregues.txt')
    encomenda_pendentes = os.path.join(pastaEncomendas, 'Encomendas_Pendentes.txt')
    clientes = os.path.join(pastaClientes, 'Clientes.txt')
    entregas = os.path.join(pastaEntregas, 'Entregas.txt')
    estafetas = os.path.join(pastaEstafetas, 'Estafetas.txt')
    veiculos = os.path.join(pastaVeiculos, 'Veiculos.txt')

    file = open(clientes, 'a+')
    file1 = open(estafetas, 'a+')
    file2 = open(encomendas_entregues, 'a+')
    file3 = open(encomenda_pendentes, 'a+')
    file4 = open(veiculos, 'a+')
    file5 = open(entregas, 'a+')

    ###Encomendas Pendentes###

    def carregar_encomendas_pendentes(self):
        ficheiro = open(self.encomenda_pendentes, 'r')
        for linha in ficheiro:
            if linha.strip():
                data = linha.strip().split(';')
                if len(data) == 6:
                    id_encomenda, id_cliente, peso, volume, prazoEntrega, estado = data
                    encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, prazoEntrega, estado)
                    self.m_encomendas_pendentes.append(encomenda)
                else:
                    print(f"Ignoring line due to incorrect format: {linha}")
        
    def criar_encomenda(self):
        id_cliente = input("Introduza o id do cliente: ")

        while True:
            peso = float(input("Introduza o peso da encomenda: "))

            if 0 < peso <= 100:
                volume = float(input("Introduza o volume da encomenda: "))

                if 0 < volume <= 100:
                    prazoEntrega = int(input("Introduza o prazo de entrega da encomenda em dias: "))
                    emHoras = prazoEntrega * 24

                    if emHoras > 0:
                        id_encomenda = str(self.definir_id_encomenda_pendente())

                        encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, emHoras, "Pendente")

                        if not self.valida_tempo("Health Planet",encomenda):
                            print("Prazo de entrega impossível de ser cumprido")
                            break

                        self.adicionar_encomenda_pendente(encomenda)

                        print("Encomenda adicionada com sucesso")
                        break
                    else:
                        print("Prazo de entrega inválido")
                else:
                    print("Volume inválido")
            else:
                print("Peso inválido")

    def definir_id_encomenda_pendente(self):
        return len(self.m_encomendas_pendentes)

    def ver_encomendas_pendentes(self):
        for encomenda in self.m_encomendas_pendentes:
            print(encomenda)
          
    def adicionar_encomenda_pendente(self, encomenda):
        id_encomenda = encomenda.getId()
        id_cliente = encomenda.getClienteId()
        peso = encomenda.getPeso()
        volume = encomenda.getVolume()
        prazoEntrega = encomenda.getPrazo()
        estado = "Pendente"
    
        if id_encomenda not in self.m_Encomendas:
            self.m_encomendas_pendentes.append(encomenda)

            ficheiro = open(self.encomenda_pendentes, 'a+')

            ficheiro.write(id_encomenda + ";" +id_cliente + ";" + str(peso) + ";" + str(volume) + ";" + str(prazoEntrega) + ";" + estado + '\n')
            
    ###Encomendas Entregues###
            
    def carregar_encomendas_entregues(self):
        ficheiro = open(self.encomendas_entregues, 'r')
        for linha in ficheiro:
            if linha.strip():
                data = linha.strip().split(';')
                if len(data) == 6:
                    id_encomenda, id_cliente, peso, volume, prazoEntrega, estado = data
                    encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, prazoEntrega, estado)
                    self.m_encomendas_entregues.append(encomenda)
                else:
                    print(f"Ignoring line due to incorrect format: {linha}")

    def criar_encomenda_entregue(self, encomenda):
        id_encomenda = encomenda.getId()
        id_cliente = encomenda.getClienteId()
        peso = encomenda.getPeso()
        volume = encomenda.getVolume()
        prazoEntrega = encomenda.getPrazo()
        estado = "Entregue"

        if id_encomenda not in self.m_encomendas_entregues:
            self.m_encomendas_entregues.append(encomenda)

            ficheiro = open(self.encomendas_entregues, 'a+')
            ficheiro.write(id_encomenda + ";" +id_cliente + ";" + str(peso) + ";" + str(volume) + ";" + str(prazoEntrega) + ";" + estado + '\n')

    def ver_encomendas_entregues(self):
        for encomenda in self.m_encomendas_entregues:
            print(encomenda)

    def adicionar_encomenda_entregue(self, encomenda):
        self.criar_encomenda_entregue(encomenda)

    ###Clientes###
        
    def carregar_clientes(self):
        try:
            with open(self.clientes, 'r') as ficheiro:
                for linha in ficheiro:
                    if linha.strip():
                        data = linha.strip().split(';')
                        if len(data) == 3:
                            id_cliente, nome, freguesia = data
                            cliente = Cliente(id_cliente, nome, freguesia)
                            self.m_Clientes.append(cliente)
                        else:
                            print(f"Ignoring line due to incorrect format: {linha}")
        except FileNotFoundError:
            print("File not found or path is incorrect.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def adicionar_cliente(self):
        while True:
            nome = input("Introduza o nome do cliente: ")
            freguesia = input("Introduza a freguesia do cliente: ")
            id_cliente = str(self.definir_id_cliente())

            if self.procura_cliente(id_cliente) == None:
                cliente = Cliente(id_cliente, nome, freguesia)

                if cliente not in self.m_Clientes:

                    self.m_Clientes.append(cliente)

                    ficheiro = open(self.clientes, 'a+')

                    ficheiro.write(id_cliente + ";" + nome + ";" + freguesia + '\n')

                    print("Cliente adicionado com sucesso")

                    break
                else:
                    print("Cliente já existe")

    def definir_id_cliente(self):  
        return len(self.m_Clientes)

    def ver_clientes(self):
        for cliente in self.m_Clientes:
            print(cliente)

    def procura_cliente(self, id_cliente):
        for cliente in self.m_Clientes:
            if cliente.id == id_cliente:
                return cliente
        return None

    ###Estafetas###

    def carregar_estafetas(self):
        try:
            with open(self.estafetas, 'r') as ficheiro:
                for linha in ficheiro:
                    if linha.strip():
                        data = linha.strip().split(';')
                        if len(data) == 8:
                            id_estafeta, nome, id_estafeta2, tipo, matricula, perda, velocidade, peso = data

                            if tipo == "bicicleta":
                                veiculo = Bicicleta(id_estafeta, matricula)

                            elif tipo == "mota":
                                veiculo = Mota(id_estafeta, matricula)

                            elif tipo == "carro":
                                veiculo = Carro(id_estafeta, matricula)

                            estafeta = Estafeta(id_estafeta, nome, veiculo)

                            self.m_Estafetas[estafeta] = []
                        else:
                            print(f"Ignoring line due to incorrect format: {linha}")
                            
        except FileNotFoundError:
            print("File not found or path is incorrect.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def criar_estafeta(self):
        nome = input("Introduza o nome do estafeta: ")
        id_estafeta = str(len(self.m_Estafetas))

        characters = string.ascii_letters + string.digits  # All letters (uppercase and lowercase) and digits
        matricula = ''.join(random.choice(characters) for i in range(6))

        tipo_veiculo = input("Introduza o tipo de veiculo do estafeta: ")

        if tipo_veiculo == "bicicleta":
            veiculo = Bicicleta(id_estafeta, matricula)

        elif tipo_veiculo == "mota":
            veiculo = Mota(id_estafeta, matricula)

        elif tipo_veiculo == "carro":
            veiculo = Carro(id_estafeta, matricula)

        if veiculo is not None:
            if self.procura_estafeta(id_estafeta) is None:
                estafeta = Estafeta(id_estafeta, nome, veiculo)

                if estafeta not in self.m_Estafetas:
                    self.m_Estafetas[estafeta] = []

                    ficheiro = open(self.estafetas, 'a+')
                    ficheiro.write(id_estafeta + ';' + nome + ';' + str(veiculo) + '\n') # modificar a escrita de valores dos veiculos

                    ficheiro2 = open(self.veiculos, 'a+')
                    ficheiro2.write(id_estafeta + ';' +  matricula + ';' +tipo_veiculo + '\n')

                    print("Estafeta adicionado com sucesso")
                else:
                    print("Estafeta já existe")
            else:
                print("Estafeta não pode ser adicionado, pois já existe")
        else:
            print("Tipo de veículo inválido")

    def procura_estafeta(self, id_estafeta):
        for estafeta in self.m_Estafetas:
            if estafeta.id == id_estafeta:
                return estafeta
        return None

    def ver_estafetas(self):
        for estafeta in self.m_Estafetas.keys():
            print(estafeta)

    ###Veiculos###
    
    def valida_tempo(self, start,encomenda):
        g = Graph()
        end = self.procura_cliente(encomenda.getIdCliente()).getFreguesia()

        dfs = g.procura_DFS(start, end, path=[], visited=set())
        bfs = g.procura_BFS(start, end,)
        g.add_heuristica(start,end)
        AStar = g.procura_aStar(start, end)
        gulosa = g.gulosa(start, end)

        custo = min(dfs, bfs, AStar, gulosa)

        tipo_veiculo = self.escolherVeiculo(custo, encomenda.getPeso())

        tempo = self.calculaTempoVeiculo(custo,encomenda.getPeso(), tipo_veiculo)

        return encomenda.getPrazo() >= tempo

    def calculaTempoVeiculo(self, custo, peso, tipo_veiculo):
        velocidades = {
            "bicicleta": {"vel_max": 10, "decresc": 0.6},
            "mota": {"vel_max": 35, "decresc": 0.5},
            "carro": {"vel_max": 50, "decresc": 0.1}
        }

        if tipo_veiculo not in velocidades:
            return None  # Tipo de veículo não reconhecido

        vel_max = velocidades[tipo_veiculo]["vel_max"]
        decresc = velocidades[tipo_veiculo]["decresc"]

        vel_atual = vel_max - (peso * decresc)

        if vel_atual <= 0:
            return None  # Peso excede capacidade do veículo

        tempo = custo / vel_atual
        return tempo

    def escolherVeiculo(self, custo, peso):
        tipo_veiculo = self.get_tipo_veiculos(peso)

        if tipo_veiculo:
            tempo_bicicleta = self.calculaTempoVeiculo(custo, peso, "bicicleta")
            tempo_mota = self.calculaTempoVeiculo(custo, peso, "mota")
            tempo_carro = self.calculaTempoVeiculo(custo, peso, "carro")

            tempos = {
                "bicicleta": tempo_bicicleta,
                "mota": tempo_mota,
                "carro": tempo_carro
            }

            veiculo_rapido = min((tempo, veiculo) for veiculo, tempo in tempos.items() if tempo is not None)
            return veiculo_rapido
        else:
            return None  # Peso excede capacidade de todos os veículos
        
    ###ENTREGAS###
    
    def precoEntrega(self,veiculo,prazo,distancia):

        if (float(prazo) >= 24):
            valorPrazo = 0
        elif (float(prazo) >= 12):
            valorPrazo = 5
        elif (float(prazo) >= 7):
            valorPrazo = 7
        elif (float(prazo) < 1):
            valorPrazo = 10
            
        if (float(distancia) >= 10):
            valordistancia = 8
        elif (float(distancia) >= 5):
            valordistancia = 4
        elif (float(distancia) < 1):
            valordistancia = 0
            
        custoBicicleta = 2
        custoMota = 5
        custoCarro = 10
                    
        if (veiculo == "bicicleta"):
            precoEntrega = custoBicicleta + valordistancia + valorPrazo
        elif (veiculo == "mota"):
            precoEntrega = custoMota + valordistancia + valorPrazo
        elif (veiculo == "bicicleta"):
            precoEntrega = custoCarro + valordistancia + valorPrazo
            
        return precoEntrega






        
