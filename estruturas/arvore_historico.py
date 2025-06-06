class NoHistorico:
    def __init__(self, local, acoes=None):
        self.local = local
        self.acoes = acoes if acoes else []
        self.esquerda = None 
        self.direita = None  

    def adicionar_acao(self, acao):
        self.acoes.append(acao)


class ArvoreHistorico:
    def __init__(self):
        self.raiz = None  # Raiz da árvore binária

    def adicionar_atendimento(self, local, acoes):
        # Cria um novo nó com o local e as ações do atendimento
        novo_no = NoHistorico(local, acoes)

        if self.raiz is None:
            # Se a árvore estiver vazia, define o novo nó como raiz
            self.raiz = novo_no
        else:
            # Insere recursivamente na posição correta
            self._inserir(self.raiz, novo_no)

    def _inserir(self, atual, novo_no):
        # Insere o novo nó na subárvore correta com base na ordem alfabética do local
        if novo_no.local < atual.local:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir(atual.direita, novo_no)

    def listar(self):
        # Retorna uma lista ordenada dos atendimentos usando percurso em ordem
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        # Percorre a árvore em ordem (esquerda, raiz, direita)
        if no is not None:
            self._em_ordem(no.esquerda, resultado)
            resultado.append({
                "local": no.local,
                "acoes": no.acoes
            })
            self._em_ordem(no.direita, resultado)
