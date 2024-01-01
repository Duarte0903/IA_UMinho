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
        self.m_Encomendas = {}                  #dicionaio que associa um cliente a uma lista encomendas
        self.m_Clientes = []                    #lista de clientes
        self.m_Estafetas = {}                   #dicionario que associa um estafeta a uma lista de encomendas
        self.m_encomendas_pendentes = []        #lista de encomendas pendentes

    ###ficheiros###

    diretorio_atual = os.getcwd()

    nome_pasta_Encomendas = 'Encomendas'
    nome_pasta_Clientes = 'Clientes'
    nome_pasta_Entregas = 'Entregas'
    nome_pasta_Estafetas = 'Estafetas'
    nome_pasta_Veiculos = 'Veiculos'

    pasta_anterior_Encomendas = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Encomendas)))
    pasta_anterior_Clientes = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Clientes)))
    pasta_anterior_Entregas = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Entregas)))
    pasta_anterior_Estafetas = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Estafetas)))
    pasta_anterior_Veiculos = Path(os.path.abspath(os.path.join(diretorio_atual, os.pardir, nome_pasta_Veiculos)))

    if not pasta_anterior_Encomendas.exists():
        pasta_anterior_Encomendas.mkdir()

    if not pasta_anterior_Clientes.exists():
        pasta_anterior_Clientes.mkdir()

    if not pasta_anterior_Entregas.exists():
        pasta_anterior_Entregas.mkdir()

    if not pasta_anterior_Estafetas.exists():
        pasta_anterior_Estafetas.mkdir()

    if not pasta_anterior_Veiculos.exists():
        pasta_anterior_Veiculos.mkdir()

    # Crie um caminho para o novo arquivo na pasta anterior
    caminho_arquivo_Encomendas = os.path.join(pasta_anterior_Encomendas, 'Encomendas.txt')
    caminho_arquivo_Encomendas_Pendentes = os.path.join(pasta_anterior_Encomendas, 'Encomendas_Pendentes.txt')
    caminho_arquivo_Clientes = os.path.join(pasta_anterior_Clientes, 'Clientes.txt')
    caminho_arquivo_Entregas = os.path.join(pasta_anterior_Entregas, 'Entregas.txt')
    caminho_arquivo_Estafetas = os.path.join(pasta_anterior_Estafetas, 'Estafetas.txt')
    caminho_arquivo_Veiculos = os.path.join(pasta_anterior_Veiculos, 'Veiculos.txt')

    file = open(caminho_arquivo_Clientes, 'a+')
    file1 = open(caminho_arquivo_Estafetas, 'a+')
    file2 = open(caminho_arquivo_Encomendas, 'a+')
    file3 = open(caminho_arquivo_Encomendas_Pendentes, 'a+')
    file4 = open(caminho_arquivo_Veiculos, 'a+')
    file5 = open(caminho_arquivo_Entregas, 'a+')

    ###Encomendas Pendentes###

    def carregar_encomendas_pendentes(self):
        ficheiro = open(self.caminho_arquivo_Encomendas_Pendentes, 'r')
        for linha in ficheiro:
            if linha.strip():
                data = linha.strip().split(';')
                if len(data) == 6:
                    id_encomenda, id_cliente, peso, volume, prazoEntrega, estado = data
                    encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, prazoEntrega, estado)
                    self.m_encomendas_pendentes.append(encomenda)
                else:
                    print(f"Ignoring line due to incorrect format: {linha}")
            else:
                print("Skipping empty line.")
        
    def criar_encomenda(self):
        id_cliente = input("Introduza o id do cliente: ")

        while True:
            peso = float(input("Introduza o peso da encomenda: "))

            if 0 < peso <= 100:
                volume = float(input("Introduza o volume da encomenda: "))

                if 0 < volume <= 100:
                    prazoEntrega = int(input("Introduza o prazo de entrega da encomenda em dias: "))

                    if prazoEntrega > 1:
                        id_encomenda = str(self.definir_id_encomenda_pendente())

                        encomenda = Encomenda(id_encomenda, id_cliente, peso, volume, prazoEntrega, "Pendente")

                        if not self.valida_tempo(encomenda):
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

            ficheiro = open(self.caminho_arquivo_Encomendas_Pendentes, 'a+')

            ficheiro.write(id_encomenda + ';' + id_cliente + ';' + str(peso) + ';' + str(volume) + ';' + str(prazoEntrega) + ';' + estado + '\n')

    ###Processamento de Encomendas###

    def valida_tempo(self, encomenda):
        g = Graph()
        inicio = "Health Planet"
        fim = self.procura_cliente(encomenda.getClienteId()).getFreguesia()
        
        (path, custo) = g.gulosa(self.m_Grafo, inicio, fim)

        tipo_veiculo = self.get_tipo_veiculos(encomenda.getPeso())

        velocidade = self.calcula_velocidade(encomenda.getPeso(), tipo_veiculo)

        return encomenda.getPrazo() >= custo / velocidade

    ###Clientes###
        
    def carregar_clientes(self):
        try:
            with open(self.caminho_arquivo_Clientes, 'r') as ficheiro:
                for linha in ficheiro:
                    if linha.strip():
                        data = linha.strip().split(';')
                        if len(data) == 3:
                            id_cliente, nome, freguesia = data
                            cliente = Cliente(id_cliente, nome, freguesia)
                            self.m_Clientes.append(cliente)
                        else:
                            print(f"Ignoring line due to incorrect format: {linha}")
                    else:
                        print("Skipping empty line.")
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

                    ficheiro = open(self.caminho_arquivo_Clientes, 'a+')

                    ficheiro.write(id_cliente + ';' + nome + ';' + freguesia + '\n')

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
            with open(self.caminho_arquivo_Estafetas, 'r') as ficheiro:
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
                    else:
                        print("Skipping empty line.")
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

                    ficheiro = open(self.caminho_arquivo_Estafetas, 'a+')
                    ficheiro.write(id_estafeta + ';' + nome + ';' + str(veiculo) + '\n') # modificar a escrita de valores dos veiculos

                    ficheiro2 = open(self.caminho_arquivo_Veiculos, 'a+')
                    ficheiro2.write(id_estafeta + ';' + matricula + ';' + tipo_veiculo + '\n')

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
    
    def get_tipo_veiculos(self, peso):
        if peso <= 5:
            return "Bicicleta"
        elif peso <= 20:
            return "Mota"
        elif peso <= 100:
            return "Carro"
        else:
            return None
        
    def calcula_velocidade(self, peso, tipo):
        if tipo == "Bicicleta":
            velocidade = 10
            i = peso
            while i > 0:
                velocidade -= 0.6
                i = i-1
            return velocidade
        elif tipo == "Mota":
            velocidade = 35
            i = peso
            while i > 0:
                velocidade -= 0.5
                i = i-1
            return velocidade
        else:
            velocidade = 50
            i = peso
            while i > 0:
                velocidade -= 0.1
                i = i-1
            return velocidade
        
