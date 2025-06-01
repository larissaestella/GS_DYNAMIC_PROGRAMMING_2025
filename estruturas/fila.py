# from collections import deque

# class FilaChamadas:
#     def __init__(self):
#         self.itens = deque()

#     def enfileirar(self, item):
#         self.itens.append(item)

#     def desenfileirar(self):
#         return self.itens.popleft() if self.itens else None

#     def esta_vazia(self):
#         return len(self.itens) == 0

# from collections import deque

# class Fila:
#     def __init__(self):
#         self.fila = deque()

#     def inserir(self, item):
#         self.fila.append(item)

#     def remover(self):
#         if self.fila:
#             return self.fila.popleft()
#         return None

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)

    def esta_vazia(self):
        return len(self.itens) == 0

    def __len__(self):
        return len(self.itens)

    def __iter__(self):
        return iter(self.itens)

