# Estrutura de dados do tipo Pilha (LIFO - Last In, First Out)
class Pilha:
    def __init__(self):
        self.pilha = []  # Inicializa uma lista para armazenar os itens da pilha

    def empilhar(self, item):
        self.pilha.append(item)  # Adiciona um item ao topo da pilha

    def desempilhar(self):
        if self.pilha:
            return self.pilha.pop()  # Remove e retorna o item do topo da pilha
        return None  

    def itens(self):
        return self.pilha.copy()  # Retorna uma cópia da pilha atual
