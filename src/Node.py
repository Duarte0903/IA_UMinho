# - Classe nodo para definiçao dos nodos
# - cada nodo tem um nome e um id
class Node:
# - construtor do nodo   
# -  O identificador é por padrão -1 se não for fornecido
# - __init__: é usado para inicializar os atributos da classe Nodo
    def __init__(self, name, id=-1):    
        self.m_id = id
        self.m_name = str(name)
        
# - Define a representação em string do objeto Node.
    def __str__(self):
        return "node " + self.m_name

# - Define o identificador do nó para o valor fornecido
    def setId(self, id):
        self.m_id = id
        
# - Retorna o identificador do nó
    def getId(self):
        return self.m_id
    
# - Retorna o nome do nó
    def getName(self):
        return self.m_name
    
# - Retorna True se o nome do nó atual for igual ao nome de outro nó
    def __eq__(self, other):
        return self.m_name == other.m_name
    
# - Define o cálculo do hash para o objeto Node.
# - Usa o hash do nome do nó, como identificador para hashing.
    def __hash__(self):
        return hash(self.m_name)