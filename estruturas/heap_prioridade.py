import heapq
from itertools import count

PESOS = {
    "cerrado": 1.2,
    "mata_atlantica": 1.5,
    "pantanal": 2.0
}

class FilaPrioridade:
    def __init__(self):
        self.fila = [] # Lista usada como heap
        self.contador = count() # desempate com base na ordem de inserção

    def calcular_prioridade(self, chamada):
        peso = PESOS.get(chamada["tipo_vegetacao"], 1.0)
        return chamada["severidade"] * peso

    def inserir(self, chamada):
        prioridade = -self.calcular_prioridade(chamada) # negativo min-heap para max-heap
        ordem = next(self.contador) # Garante que a ordem de chegada seja considerada em caso de empate
        heapq.heappush(self.fila, (prioridade, ordem, chamada))

    def remover(self):
        if self.fila:
            prioridade, _, chamada = heapq.heappop(self.fila)# Remove e retorna a menor prioridade
            return -prioridade, chamada # Converte de volta para o valor original positivo
        return None

    def vazia(self):
        return len(self.fila) == 0

    def itens(self):
                # Retorna uma lista com as prioridades positivas e os dados das chamadas
        return [(-prioridade, chamada) for (prioridade, _, chamada) in self.fila]

