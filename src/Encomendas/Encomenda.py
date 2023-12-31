class Encomenda:


    def __init__(self, cliente , encomenda, peso, volume, prazoEntrega, estado):
        self.cliente = cliente
        self.encomenda = encomenda
        self.peso = peso
        self.volume = volume
        self.prazoEntrega = prazoEntrega
        self.estado = estado

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente
    
    def setEncomenda(self, encomenda):
        self.encomenda = encomenda

    def getEncomenda(self):
        return self.encomenda

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setVolume(self, volume):
        self.volume = volume

    def getVolume(self):
        return self.volume

    def setPrazo(self, prazo):
        self.prazoEntrega = prazo

    def getPrazo(self):
        return self.prazoEntrega
    
    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def __str__(self):
        return "Cliente: " + str(self.getCliente()) + "; " + "Encomenda: " + str(self.getEncomenda()) + "; " + "Peso: " + str(self.getPeso()) + "; " + "Volume: " + str(self.getVolume()) + "; " + "Prazo de Entrega: " + str(self.getPrazo()) + "; " + "Estado: " + str(self.getEstado())

    def __eq__(self, other):
        if(isinstance(other,Encomenda)):
            return self.getCliente == other.getCliente and self.getEncomenda == other.getEncomenda and self.getPeso == other.getPeso and self.getVolume == other.getVolume and self.getPrazo == other.getPrazo and self.getEstado == other.getEstado
        return False



