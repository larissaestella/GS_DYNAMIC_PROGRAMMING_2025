import heapq

class Grafo:
    def __init__(self):
        self.mapa = {
            "Base Central": {"Zona Norte": 10, "Mata Alta": 12, "Serra Azul": 24},
            "Zona Norte": {"Mata Alta": 7, "Base Central": 10},
            "Mata Alta": {"Zona Norte": 7, "Base Central": 12, "Serra Azul": 15},
            "Serra Azul": {"Base Central": 24, "Mata Alta": 15}
        }


    def dijkstra(self, origem, destino):
        fila = [(0, origem, [])]
        visitados = set()

        while fila:
            custo, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            if atual == destino:
                return caminho, custo
            visitados.add(atual)
            for vizinho, peso in self.mapa.get(atual, {}).items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (custo + peso, vizinho, caminho))
        return [], float('inf')
