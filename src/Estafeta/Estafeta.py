class Estafeta:
    def __init__ (self, id, nome, veiculo):
        self.id = id
        self.nome = nome
        self.veiculo = veiculo
        self.disponivel = True

    def setId(self, id):
        self.id = id

    def getId (self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome
    
    def setVeiculo(self, veiculo):
        self.veiculo = veiculo

    def getVeiculo (self):
        return self.veiculo
    
    def setDisponivel(self, disponivel):
        self.disponivel = disponivel
    
    def getDisponivel(self):
        return self.disponivel
    
    def __str__(self):
        return "Id: " + str(self.id) + "; "+ "Nome: " + self.nome + "; " +"Veiculo:" + str(self.veiculo) + "; " + "Disponibilidade: " + str(self.disponivel)



