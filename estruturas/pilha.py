# class PilhaAcoes:
#     def __init__(self):
#         self.pilha = []

#     def registrar_acao(self, acao):
#         self.pilha.append(acao)

#     def desfazer_acao(self):
#         return self.pilha.pop() if self.pilha else None

class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):
        if self.pilha:
            return self.pilha.pop()
        return None

    def itens(self):
        return self.pilha.copy()

