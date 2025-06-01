class Nodo:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)
