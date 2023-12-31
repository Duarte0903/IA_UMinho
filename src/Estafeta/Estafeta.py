class Estafeta:
    def __init__ (self, nome, entregas):
        self.nome = nome
        self.entregas = entregas 

    def setNome(self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome
    
    def setEntregas(self, entregas):
        self.entregas = entregas

    def getEntregas(self):
        return self.entregas
    
    def __str__(self):
        return "Nome: " + str(self.getNome())




