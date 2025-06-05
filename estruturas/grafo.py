import heapq

class Grafo:
    def __init__(self):
        self.mapa = {
            "Base Central": {"Zona Norte": 10, "Vila Verde": 5,},
            "Zona Norte": {"Base Central": 10, "Mata Alta": 7},
            "Vila Verde": {"Base Central": 5, "Mata Alta": 3},
            "Mata Alta": {"Zona Norte": 7, "Vila Verde": 3}
        } # Mapa Grafo


    def dijkstra(self, origem, destino):
        fila = [(0, origem, [])] # Fila de prioridade: cada item é uma tupla (custo acumulado, nó atual, caminho até aqui)
        visitados = set() # Conjunto para armazenar nós já visitados

        while fila:
            custo, atual, caminho = heapq.heappop(fila) # Pega o caminho com menor custo atual

            if atual in visitados:
                continue
            caminho = caminho + [atual] # Atualiza o caminho com o nó atual

            if atual == destino:
                return caminho, custo # Retorna o caminho e o custo total se destino for alcançado
            visitados.add(atual)
            
            for vizinho, peso in self.mapa.get(atual, {}).items():
                if vizinho not in visitados:
                    # Adiciona vizinhos não visitados na fila com o custo atualizado
                    heapq.heappush(fila, (custo + peso, vizinho, caminho)) 

        return [], float('inf') # Retorna caminho vazio e custo infinito se não houver rota
