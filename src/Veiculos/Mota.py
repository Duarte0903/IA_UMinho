class Mota:
    def __init__(self, id_estafeta, matricula):
        self.tipo = "mota"
        self.idDono = id_estafeta
        self.matricula = matricula
        self.perdaVelocidade = 0.5
        self.velocMedia = 35
        self.limitePeso = 20

    def getTipo(self):
        return self.tipo

    def setIdDono(self, idDono):
        self.idDono = idDono

    def getIdDono(self):
        return self.idDono

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setPerdaVelocidade(self, perdaVelocidade):
        self.perdaVelocidade = perdaVelocidade

    def getPerdaVelocidade(self):
        return self.perdaVelocidade

    def getVelocMedia(self):
        return self.velocMedia

    def getLimite_peso(self):
        return self.limite_peso
    
    def __str__(self):
        return str(self.idDono) + ";" + self.tipo + "; " +self.matricula + "; " + str(self.perdaVelocidade) + "; "+ str(self.velocMedia) + "; " +  str(self.limitePeso)
    
    def __eq__(self, other):
        if(isinstance(other,Mota)):
            return self.getIdDono == other.getIdDono and self.getMatricula == other.getMatricula and self.getPerdaVelocidade == other.getPerdaVelocidade and self.getVelocMedia == other.getVelocMedia and self.getLimite_peso == other.getLimite_peso
        return False