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
    
    def to_list(self):
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append({
                "local": atual.local,
                "status": atual.status
            })
            atual = atual.proximo
        return elementos
