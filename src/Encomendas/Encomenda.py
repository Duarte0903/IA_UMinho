class Encomenda:

    def __init__(self, id_encomenda, id_cliente , peso, volume, prazoEntrega, estado):
        self.id_encomenda = id_encomenda        
        self.id_cliente = id_cliente
        self.peso = peso
        self.volume = volume
        self.prazoEntrega = prazoEntrega # prazo de entrega em dias 
        self.estado = estado

    def setId(self, id_encomenda):
        self.id_encomenda = id_encomenda

    def getId(self):
        return self.id_encomenda
    
    def getIdCliente(self):
        return self.id_cliente
    
    def setIdCliente(self, id_cliente):
        self.id_cliente = id_cliente

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setVolume(self, volume):
        self.volume = volume

    def getVolume(self):
        return self.volume

    def setPrazo(self, prazoEntrega):
        self.prazoEntrega = prazoEntrega

    def getPrazo(self):
        return self.prazoEntrega
    
    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def __str__(self):
        return "Id: " + str(self.getId()) + "; " + "Cliente: " + str(self.getIdCliente()) + "; " + "Peso: " + str(self.getPeso()) + "; " + "Volume: " + str(self.getVolume()) + "; " + "Prazo: " + str(self.getPrazo()) + "; " + "Estado: " + str(self.getEstado())

    def __eq__(self, other):
        if(isinstance(other,Encomenda)):
            return self.getId == other.getId and self.getIdCliente == other.getIdCliente and self.getPeso == other.getPeso and self.getVolume == other.getVolume and self.getPrazo == other.getPrazo and self.getEstado == other.getEstado
        return False



