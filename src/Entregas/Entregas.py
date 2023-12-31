from Cliente import Cliente as cliente
from Encomenda import Encomenda as encomenda

class Entrega:

    def __init__( self, id, cliente, estafeta, classificacao, preco, veiculo, caminho, distancia, tempoPrevisto, encomenda, algoritmo):
        self.id = id
        self.cliente = cliente
        self.estafeta = estafeta
        self.classificacao = classificacao
        self.preco = preco
        self.veiculo = veiculo
        self.caminho = caminho
        self.distancia = distancia
        self.tempoPrevisto = tempoPrevisto
        self.encomenda = encomenda
        self.algoritmo = algoritmo

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setCliente(self, cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
    def setEstafeta(self, estafeta):
        self.estafeta = estafeta
        
    def getEstafeta(self):
        return self.estafeta
    
    def setClassificacao(self, classificacao):
        self.classificacao = classificacao
        
    def getClassificacao(self):
        return self.classificacao
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setVeiculo(self, veiculo):
        self.veiculo = veiculo
    
    def getVeiculo(self):
        return self.veiculo
    
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
    
    def setEncomenda(self, encomenda):
        self.encomenda = encomenda
        
    def getEncomenda(self):
        return self.encomenda
    
    def setAlgoritmo(self, algoritmo):
        self.algoritmo = algoritmo

    def getAlgoritmo(self):
        return self.algoritmo
    
    def __eq__(self, other):
        if(isinstance(other,Entrega)):
            return self.id == other.id and self.cliente == other.cliente and self.estafeta == other.estafeta and self.classificacao == other.classificacao and self.preco == other.preco and self.veiculo == other.veiculo and self.caminho == other.caminho and self.tempoPrevisto == other.tempoPrevisto and self.encomenda == other.encomenda and self.algoritmo == other.algoritmo
        return False




