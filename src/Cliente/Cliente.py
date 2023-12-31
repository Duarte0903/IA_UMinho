
class Cliente:

    def __init__(self, nome,freguesia):
        self.nome = nome
        self.freguesia = freguesia

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFreguesia(self, freguesia):
        self.freguesia = freguesia

    def getFreguesia(self):
        return self.freguesia

    def __str__(self):
        return "Nome: " + str(self.getNome()) + "; " + "Freguesia: " + str(self.getFreguesia())

    def __eq__(self, other):
        if(isinstance(other, Cliente)):
            return self.nome == other.nome and self.freguesia == other.freguesia
        return False


