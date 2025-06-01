# class NoStatus:
#     def __init__(self, area, status):
#         self.area = area
#         self.status = status
#         self.proximo = None

# class ListaStatus:
#     def __init__(self):
#         self.head = None

#     def atualizar_status(self, area, novo_status):
#         atual = self.head
#         while atual:
#             if atual.area == area:
#                 atual.status = novo_status
#                 return
#             atual = atual.proximo
#         novo = NoStatus(area, novo_status)
#         novo.proximo = self.head
#         self.head = novo

class No:
    def __init__(self, local, status):
        self.local = local
        self.status = status
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.inicio = None

    def atualizar_status(self, local, status):
        atual = self.inicio
        while atual:
            if atual.local == local:
                atual.status = status
                return
            atual = atual.proximo
        novo = No(local, status)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        resultado = []
        atual = self.inicio
        while atual:
            resultado.append(f"{atual.local}: {atual.status}")
            atual = atual.proximo
        return resultado
