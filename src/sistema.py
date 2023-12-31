from Grafos.Graph import *
from Cliente.Cliente import Cliente
from Encomendas.Encomenda import Encomenda
from Estafeta.Estafeta import Estafeta
import os
from pathlib import Path 
from Pesquisas.NaoInformada import *
from Pesquisas.Informada import *

class Sistema:

    def __init__ (self,grafo):
        self.m_Grafo = grafo
        self.m_Encomendas = {} #dicionaio que associa um cliente a uma lista encomenda
        self.m_Clientes = [] #lista de clientes
        self.m_Estafetas = []
        self.m_encomendas_pendentes = []

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
        inicio = "Health Planet"
        fim = self.procura_cliente(encomenda.getClienteId()).getFreguesia()
        
        (path, custo) = gulosa(self.m_Grafo, inicio, fim)

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

    def adicionar_estafeta(self, estafeta):
        self.m_Estafetas.append(estafeta)

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
