from Cliente.Cliente import *
from Encomendas.Encomenda import *

class Entrega:

    def __init__(self, id, idcliente, idestafeta, idencomenda, avaliacao, preco, matrVeiculo, caminho, distancia, tempoPrevisto):
        self.id = id
        self.idcliente = idcliente
        self.idestafeta = idestafeta
        self.idencomenda = idencomenda
        self.avaliacao = avaliacao
        self.preco = preco
        self.matrVeiculo = matrVeiculo
        self.caminho = caminho
        self.distancia = distancia
        self.tempoPrevisto = tempoPrevisto

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setIdCliente(self, idcliente):
        self.idcliente = idcliente
    
    def getIdCliente(self):
        return self.idcliente
    
    def setIdEstafeta(self, idestafeta):
        self.idestafeta = idestafeta
        
    def getIdEstafeta(self):
        return self.idestafeta
    
    def setIdEncomenda(self, idencomenda):
        self.idencomenda = idencomenda
        
    def getIdEncomenda(self):
        return self.idencomenda
    
    def setAvaliacao(self, avaliacao):
        self.avaliacao = avaliacao
        
    def getAvaliacao(self):
        return self.avaliacao
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setMatrVeiculo(self, matrVeiculo):
        self.matrVeiculo = matrVeiculo
    
    def getMatrVeiculo(self):
        return self.matrVeiculo
    
    def setCaminho(self, caminho):
        self.caminho = caminho

    def getCaminho(self):
        return self.caminho
    
    def setDistancia(self, distancia):
        self.distancia = distancia

    def getDistancia(self):
        return self.distancia
    
    def setTempoPrevisto(self, tempoPrevisto):
        self.tempoPrevisto = tempoPrevisto

    def getTempoPrevisto(self):
        return self.tempoPrevisto
    
    def __str__(self):
        return "Id: " + str(self.getId()) + "; " + "Cliente: " + str(self.getIdCliente()) + "; " + "Estafeta: " + str(self.getIdEstafeta()) + "; " + "Encomenda: " + str(self.getIdEncomenda()) + "; " + "Avaliação: " + str(self.getAvaliacao()) + "; " + "Custo: " + str(self.getPreco()) + "; " + "Matrícula: " + str(self.getMatrVeiculo()) +"; " +"Caminho: " + str(self.getCaminho()) + "; " + "Distância: " + str(self.getDistancia()) + "; " + "Tempo de Entrega: " + str(self.getTempoPrevisto()) + "; "
    
    def __eq__(self, other):
        if(isinstance(other,Entrega)):
            return self.id == other.id and self.cliente == other.cliente and self.estafeta == other.estafeta and self.classificacao == other.classificacao and self.preco == other.preco and self.veiculo == other.veiculo and self.caminho == other.caminho and self.tempoPrevisto == other.tempoPrevisto and self.encomenda == other.encomenda 
        return False




