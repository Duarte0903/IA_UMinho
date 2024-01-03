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

    pastaEncomendas = os.path.join(diretoria_atual, 'EncomendasData')
    pastaClientes = os.path.join(diretoria_atual, 'ClientesData')
    pastaEntregas = os.path.join(diretoria_atual, 'EntregasData')
    pastaEstafetas = os.path.join(diretoria_atual, 'EstafetasData')
    pastaVeiculos = os.path.join(diretoria_atual, 'VeiculosData')

        
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

    encomenda_pendentes = os.path.join(pastaEncomendas, 'Encomendas_Pendentes.txt')
    clientes = os.path.join(pastaClientes, 'Clientes.txt')
    entregas = os.path.join(pastaEntregas, 'Entregas.txt')
    estafetas = os.path.join(pastaEstafetas, 'Estafetas.txt')
    veiculos = os.path.join(pastaVeiculos, 'Veiculos.txt')

    file = open(clientes, 'a+')
    file1 = open(estafetas, 'a+')
    file3 = open(encomenda_pendentes, 'a+')
    file4 = open(veiculos, 'a+')
    file5 = open(entregas, 'a+')

    ###Encomendas Pendentes###

    def reload_encomendas_pendentes(self):
        ficheiro = open(self.encomenda_pendentes, "w")
        for encomenda in self.m_encomendas_pendentes:
            id_encomenda = encomenda.getId()
            id_cliente = encomenda.getIdCliente()
            peso = encomenda.getPeso()
            volume = encomenda.getVolume()
            prazoEntrega = encomenda.getPrazo()
            estado = "Pendente"
    
            ficheiro.write(str(id_encomenda) + ";" +str(id_cliente) + ";" + str(peso) + ";" + str(volume) + ";" + str(prazoEntrega) + ";" + estado + '\n')

    def carregar_encomendas_pendentes(self):
        ficheiro = open(self.encomenda_pendentes, 'r')
        for linha in ficheiro:
            if linha.strip():
                data = linha.strip().split(';')
                if len(data) == 6:
                    id_encomenda, id_cliente, peso, volume, prazoEntrega, estado = data
                    encomenda = Encomenda(int(id_encomenda), int(id_cliente), float(peso), float(volume), int(prazoEntrega), estado)
                    self.m_encomendas_pendentes.append(encomenda)
                else:
                    print(f"Ignoring line due to incorrect format: {linha}")
        
    def criar_encomenda(self):
        id_cliente = int(input("Introduza o id do cliente: "))
        
        while True:
            peso = float(input("Introduza o peso da encomenda: "))

            if 0 < peso <= 100:
                volume = float(input("Introduza o volume da encomenda: "))

                if 0 < volume <= 100:
                    prazoEntrega = int(input("Introduza o prazo de entrega da encomenda em horas: "))

                    if prazoEntrega > 0:
                        id_encomenda = int(self.definir_id_encomenda_pendente())

                        encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, prazoEntrega, "Pendente")

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
        if len(self.m_encomendas_pendentes) == 0: return print ("Não existem encomendas pendentes!")
        for encomenda in self.m_encomendas_pendentes:
            print(encomenda)
          
    def adicionar_encomenda_pendente(self, encomenda):
        id_encomenda = encomenda.getId()
        id_cliente = encomenda.getIdCliente()
        peso = encomenda.getPeso()
        volume = encomenda.getVolume()
        prazoEntrega = encomenda.getPrazo()
        estado = "Pendente"
    
        if id_encomenda not in self.m_Encomendas:
            self.m_encomendas_pendentes.append(encomenda)

            ficheiro = open(self.encomenda_pendentes, 'a+')

            ficheiro.write(str(id_encomenda) + ";" +str(id_cliente) + ";" + str(peso) + ";" + str(volume) + ";" + str(prazoEntrega) + ";" + estado + '\n')
            
    ###Encomendas Entregues###
            
    def reload_entregas(self):
        ficheiro = open(self.entregas, 'w')
        for entrega in self.m_encomendas_entregues:
            id_entrega = entrega.getId()
            id_cliente = entrega.getIdCliente()
            id_estafeta = entrega.getIdEstafeta()
            id_encomenda = entrega.getIdEncomenda()
            avaliacao = entrega.getAvaliacao()
            preco = entrega.getPreco()
            matr = entrega.getMatrVeiculo()
            caminho = entrega.getCaminho()
            dist = entrega.getDistancia()
            tempo = entrega.getTempoPrevisto()

            ficheiro.write(f"{id_entrega};{id_cliente};{id_estafeta};{id_encomenda};{avaliacao};{preco};{matr};{caminho};{dist};{tempo}\n")

    def carregar_encomendas_entregues(self):
        ficheiro = open(self.entregas, 'r')
        for linha in ficheiro:
            if linha.strip():
                data = linha.strip().split(';')
                if len(data) == 10:
                    id_entrega, id_cliente, id_estafeta, id_encomenda, avaliacao, preco, matricula, caminho, distancia, tempo = data
                    encomenda = Entrega(int(id_entrega), int(id_cliente), int(id_estafeta), int(id_encomenda), avaliacao, float(preco), matricula, caminho, float(distancia), float(tempo))
                    self.m_encomendas_entregues.append(encomenda)
                else:
                    print(f"Ignoring line due to incorrect format: {linha}")

    def criar_encomenda_entregue(self, entrega):
        id_entrega = entrega.getId()
        id_cliente = entrega.getIdCliente()
        id_estafeta = entrega.getIdEstafeta()
        id_encomenda = entrega.getIdEncomenda()
        avaliacao = entrega.getAvaliacao()
        preco = entrega.getPreco()
        matr = entrega.getMatrVeiculo()
        caminho = entrega.getCaminho()
        dist = entrega.getDistancia()
        tempo = entrega.getTempoPrevisto()

        list_estafetas = list(self.m_Estafetas.keys())
        for estafeta in list_estafetas:
            if estafeta.getId() == id_estafeta:
                estafeta.setDisponivel(False)

        if id_encomenda not in self.m_encomendas_entregues:
            self.m_encomendas_entregues.append(entrega)

            ficheiro = open(self.entregas, 'a+')
            ficheiro.write(f"{id_entrega};{id_cliente};{id_estafeta};{id_encomenda};{avaliacao};{preco};{matr};{caminho};{dist};{tempo}\n")

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
                            cliente = Cliente(int(id_cliente), nome, freguesia)
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
            
            for node in self.graph.getNodes():
                teste = node.getName()
                if teste == freguesia:
                    break;
                else: teste = "None"
            
            if teste == "None": return print("Freguesia não existente!")
            

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
        if len(self.m_Clientes) == 0: print("Não existem clientes!")
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
                                veiculo = Bicicleta(int(id_estafeta), matricula)

                            elif tipo == "mota":
                                veiculo = Mota(int(id_estafeta), matricula)

                            elif tipo == "carro":
                                veiculo = Carro(int(id_estafeta), matricula)

                            estafeta = Estafeta(int(id_estafeta), nome, veiculo)

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

        tipo_veiculo = input("Introduza o tipo de veiculo do estafeta: ").lower()

        if tipo_veiculo == "bicicleta":
            veiculo = Bicicleta(id_estafeta, matricula)

        elif tipo_veiculo == "mota":
            veiculo = Mota(id_estafeta, matricula)

        elif tipo_veiculo == "carro":
            veiculo = Carro(id_estafeta, matricula)
            
        else: return print("Veículo inválido!")

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
        end = self.procura_cliente(encomenda.getIdCliente()).getFreguesia()

        dfs = self.graph.procura_DFS(start, end, path=[], visited=set())
        bfs = self.graph.procura_BFS(start, end,)
        self.graph.add_heuristica_general(end)
        AStar = self.graph.procura_aStar(start, end)
        gulosa = self.graph.gulosa(start, end)

        custo = min(dfs[1], bfs[1], AStar[1], gulosa[1])

        tempo = self.escolherVeiculo(custo, encomenda.getPeso(), encomenda.getPrazo())

        #tempo = self.calculaTempoVeiculo(custo,encomenda.getPeso(), tipo_veiculo)

        return encomenda.getPrazo() >= tempo

    def calculaTempoVeiculo(self, custo, peso, tipo_veiculo, prazo):
        velocidades = {
            "bicicleta": {"vel_max": 10, "decresc": 0.6},
            "mota": {"vel_max": 35, "decresc": 0.5},
            "carro": {"vel_max": 50, "decresc": 0.1}
        }

        if tipo_veiculo not in velocidades:
            return None  # Tipo de veículo não reconhecido

        key_list = list(velocidades.keys())
        indice = key_list.index(tipo_veiculo)
        vel_max = velocidades[tipo_veiculo]["vel_max"]
        decresc = velocidades[tipo_veiculo]["decresc"]

        vel_atual = vel_max - (peso * decresc)

        if vel_atual <= 0:
            return None  # Peso excede capacidade do veículo

        tempo = custo / vel_atual

        if tempo >= prazo:
            indice = indice + 1
            tempo = self.calculaTempoVeiculo(custo, peso, key_list[indice], prazo)

        return (tempo, key_list[indice])

    def escolherVeiculo(self, custo, peso, prazo):
        tipo_veiculo = self.get_tipo_veiculos(peso)

        if tipo_veiculo:
            (tempo, tipo) = self.calculaTempoVeiculo(custo, peso, tipo_veiculo, prazo)

            return tempo
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
        elif (float(prazo) >= 1):
            valorPrazo = 10
            
        if (float(distancia) >= 10):
            valordistancia = 8
        elif (float(distancia) >= 5):
            valordistancia = 4
        elif (float(distancia) > 1):
            valordistancia = 0
            
        custoBicicleta = 2
        custoMota = 5
        custoCarro = 10
                    
        if (veiculo == "bicicleta"):
            precoEntrega = custoBicicleta + valordistancia + valorPrazo
        elif (veiculo == "mota"):
            precoEntrega = custoMota + valordistancia + valorPrazo
        elif (veiculo == "carro"):
            precoEntrega = custoCarro + valordistancia + valorPrazo
            
        return precoEntrega
    
    def procura_encomenda(self, id_encomenda):
        for encomenda in self.m_encomendas_pendentes:
            if encomenda.getId() == id_encomenda:
                return encomenda
        return None
    
    def get_tipo_veiculos(self, peso):
        if peso <= 5:
            return "bicicleta"
        elif peso <= 20:
            return "mota"
        elif peso <= 100:
            return "carro"
        else:
            return None
        
    def estafeta_disponivel(self, tipo):
        estafetas_list = list(self.m_Estafetas.keys())
        for estafeta in estafetas_list:
            if estafeta.getVeiculo().getTipo() == tipo:
                if estafeta.getDisponivel():
                    return estafeta
        return None

    def criar_entrega(self):
        id = int(input("Introduza o ID da encomenda a entregar: "))
        encomenda = self.procura_encomenda(id)
        if not encomenda:
            print("Encomenda não existe")
            return
        
        custo = self.graph.procura_aStar("Health Planet", self.procura_cliente(encomenda.getIdCliente()).getFreguesia())
        
        id_entrega = len(self.m_encomendas_entregues)
        id_cliente = encomenda.getIdCliente()
        (tempo, tipo) = self.calculaTempoVeiculo(custo[1], encomenda.getPeso(), self.get_tipo_veiculos(encomenda.getPeso()), encomenda.getPrazo())
        estafeta = self.estafeta_disponivel(tipo)
        if estafeta == None:
            print("Não existe nenhum estafeta disponível")
            return
        id_encomenda = id
        avaliacao = None
        preco = self.precoEntrega(estafeta.getVeiculo().getTipo(), encomenda.getPrazo(), custo[1])
        matr = estafeta.getVeiculo().getMatricula()
        caminho = custo[0]
        dist = custo[1]

        entrega = Entrega(id_entrega, id_cliente, estafeta.getId(), id_encomenda, avaliacao, preco, matr, caminho, dist, tempo)

        self.criar_encomenda_entregue(entrega)

        self.m_encomendas_pendentes.remove(encomenda)

        self.reload_encomendas_pendentes()
        
        print("Entrega efetuada com sucesso!")

    ###AVALIACOES###
        
    def avaliar_entrega(self):
        id_cliente = int(input("Qual o seu ID de cliente? "))              
        i=0
        for entrega in self.m_encomendas_entregues:
            if entrega.getIdCliente() == id_cliente:
                print(entrega)
                i = i + 1
        if i == 0: return print("Este cliente não existe ou não tem entregas!")
        id = int(input("Que entrega deseja avaliar? "))
        entrega_pedida = None
        for entrega in self.m_encomendas_entregues:
            if entrega.getId() == id:
                entrega_pedida = entrega
        if entrega_pedida == None:
            print("Entrega não existe")

        avaliacao = input("Como avalia a entrega?")

        if float(avaliacao) > 5 or float(avaliacao) < 0:
            print("Avaliação introduzida é inválida(0-5)")

        entrega_pedida.setAvaliacao(avaliacao)

        list_estafetas = list(self.m_Estafetas.keys())
        for estafeta in list_estafetas:
            if estafeta.getId() == entrega.getIdEstafeta():
                estafeta.setDisponivel(True)

        self.reload_entregas()

    def avaliacao_media(self):
        soma = 0
        counter = 0
        id = int(input("ID de estafeta: "))
        for entrega in self.m_encomendas_entregues:
            if entrega.getAvaliacao() != "None":
                if entrega.getIdEstafeta() == id:
                    soma = soma + int(entrega.getAvaliacao())
                    counter = counter + 1
        if counter == 0:
            print("O estafeta não tem entregas")
            return
        print(f'Avaliação média: {soma / counter}')







        
