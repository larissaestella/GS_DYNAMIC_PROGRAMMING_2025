# nó da lista ligada, com um local, status e referência ao próximo nó
class No:
    def __init__(self, local, status):
        self.local = local
        self.status = status
        self.proximo = None

# lista ligada que armazena o status de diferentes locais
class ListaLigada:
    def __init__(self):
        self.inicio = None

    def atualizar_status(self, local, status):
        atual = self.inicio
        # Percorre a lista procurando o local
        while atual:
            if atual.local == local:
                atual.status = status # Atualiza o status se o local já existir
                return
            atual = atual.proximo
        # Se o local não for encontrado, cria um novo nó e insere no início da lista
        novo = No(local, status)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        resultado = []
        atual = self.inicio
        # Percorre a lista e cria uma lista de strings formatadas
        while atual:
            resultado.append(f"{atual.local}: {atual.status}")
            atual = atual.proximo
        return resultado
    
    def to_list(self):
        atual = self.inicio
        elementos = []
        # Converte os dados da lista ligada em uma lista de dicionários
        while atual:
            elementos.append({
                "local": atual.local,
                "status": atual.status
            })
            atual = atual.proximo
        return elementos

