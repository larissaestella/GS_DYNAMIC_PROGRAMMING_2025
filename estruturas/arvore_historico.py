class NoHistorico:
    def __init__(self, local, acoes=None):
        self.local = local
        self.acoes = acoes if acoes else []
        self.filhos = []

    def adicionar_acao(self, acao):
        self.acoes.append(acao)

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

class ArvoreHistorico:
    def __init__(self):
        self.raizes = []

    def adicionar_atendimento(self, local, acoes):
        novo_no = NoHistorico(local, acoes)
        self.raizes.append(novo_no)

    def listar(self):
        resultado = []
        for raiz in self.raizes:
            resultado.append({
                "local": raiz.local,
                "acoes": raiz.acoes
            })
        return resultado
