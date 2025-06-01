# import heapq

# peso_vegetacao = {
#     "cerrado": 1.2,
#     "mata_atlantica": 1.5,
#     "pantanal": 2.0
# }

# def calcular_prioridade(chamada):
#     return chamada["severidade"] * peso_vegetacao.get(chamada["tipo_vegetacao"], 1)

# class FilaPrioridade:
#     def __init__(self):
#         self.heap = []

#     def inserir(self, chamada):
#         prioridade = -calcular_prioridade(chamada)  # Negativo para max-heap
#         heapq.heappush(self.heap, (prioridade, chamada))

#     def extrair_chamada(self):
#         return heapq.heappop(self.heap)[1] if self.heap else None

# import heapq

# PESOS = {
#     "cerrado": 1.2,
#     "mata_atlantica": 1.5,
#     "pantanal": 2.0
# }

# class FilaPrioridade:
#     def __init__(self):
#         self.fila = []

#     def calcular_prioridade(self, chamada):
#         peso = PESOS.get(chamada["tipo_vegetacao"], 1.0)
#         return chamada["severidade"] * peso

#     def inserir(self, chamada):
#         prioridade = -self.calcular_prioridade(chamada)  # heapq é min-heap
#         heapq.heappush(self.fila, (prioridade, chamada))

#     def remover(self):
#         if self.fila:
#             return heapq.heappop(self.fila)[1]
#         return None


import heapq

PESOS = {
    "cerrado": 1.2,
    "mata_atlantica": 1.5,
    "pantanal": 2.0
}

class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def calcular_prioridade(self, chamada):
        peso = PESOS.get(chamada["tipo_vegetacao"], 1.0)
        return chamada["severidade"] * peso

    def inserir(self, chamada):
        prioridade = -self.calcular_prioridade(chamada)
        heapq.heappush(self.fila, (prioridade, chamada))

    def remover(self):
        if self.fila:
            return heapq.heappop(self.fila)
        return None

    def vazia(self):
        return len(self.fila) == 0

    def itens(self):
        # Retorna uma cópia da lista de prioridades (sem desempilhar)
        return list(self.fila)
