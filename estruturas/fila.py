class Fila:
    def __init__(self):
        self.itens = []  # Lista usada para armazenar os elementos da fila

    def enfileirar(self, item):
        self.itens.append(item)  # Adiciona um item ao final da fila

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)  # Remove o primeiro item da fila (regra FIFO)

    def esta_vazia(self):
        return len(self.itens) == 0  # Retorna True se a fila estiver vazia

    def __len__(self):
        return len(self.itens)  # Retorna a quantidade de elementos na fila

    def __iter__(self):
        return iter(self.itens)  # Permite iterar diretamente pela fila 
