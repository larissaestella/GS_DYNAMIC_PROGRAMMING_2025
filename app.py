# # app.py

# from flask import Flask, render_template, redirect, url_for
# import json
# from estruturas.fila import FilaChamadas
# from estruturas.heap_prioridade import FilaPrioridade
# from estruturas.pilha import PilhaAcoes
# from estruturas.lista_ligada import ListaStatus
# from estruturas.grafo import dijkstra

# app = Flask(__name__)

# fila = FilaChamadas()
# heap = FilaPrioridade()
# pilha_acoes = PilhaAcoes()
# lista_status = ListaStatus()

# def carregar_chamadas():
#     with open('dados/chamadas.json') as f:
#         chamadas = json.load(f)
#         for chamada in chamadas:
#             fila.enfileirar(chamada)
#             heap.inserir(chamada)
#             lista_status.inserir_status(chamada['local'], 'ativo')

# mapa = {
#     "Base Central": {"Zona Norte": 10, "Mata Alta": 12},
#     "Zona Norte": {"Mata Alta": 7},
#     "Mata Alta": {"Zona Norte": 7}
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/carregar')
# def carregar():
#     carregar_chamadas()
#     return redirect(url_for('index'))

# @app.route('/prioridades')
# def prioridades():
#     prioridades = sorted([(-p, c) for p, c in heap.heap], reverse=True)
#     return render_template('prioridades.html', prioridades=prioridades)

# @app.route('/atender')
# def atender():
#     chamada = heap.remover()
#     if not chamada:
#         return render_template('atender.html', chamada=None)

#     origem = "Base Central"
#     destino = chamada['local']
#     caminho, tempo = dijkstra(mapa, origem, destino)
#     acoes = ["Aplicar barreira de contenção", "Criar aceiro"]
#     for acao in acoes:
#         pilha_acoes.registrar_acao(acao)
#     lista_status.atualizar_status(destino, "controle em andamento")

#     return render_template('atender.html', chamada=chamada, rota=caminho, tempo=tempo, acoes=acoes)

# @app.route('/acoes')
# def acoes():
#     return render_template('acoes.html', acoes=reversed(pilha_acoes.pilha))

# @app.route('/status')
# def status():
#     atual = lista_status.head
#     status_list = []
#     while atual:
#         status_list.append((atual.area, atual.status))
#         atual = atual.proximo
#     return render_template('status.html', status_list=status_list)

# if __name__ == '__main__':
#     app.run(debug=True)



# ***********************************************************************************

# from flask import Flask, render_template, request, redirect
# import json
# from estruturas.heap_prioridade import FilaPrioridade
# from estruturas.grafo import Grafo
# from estruturas.pilha import Pilha
# from estruturas.lista_ligada import ListaLigada

# app = Flask(__name__)

# fila = FilaPrioridade()
# grafo = Grafo()
# pilha_acoes = Pilha()
# status_areas = ListaLigada()

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/prioridades')
# def prioridades():
#     return render_template("prioridades.html", fila=fila.fila)

# @app.route('/carregar_chamadas')
# def carregar_chamadas():
#     with open("dados/chamadas.json") as f:
#         chamadas = json.load(f)
#     for chamada in chamadas:
#         fila.inserir(chamada)
#     return redirect("/prioridades")

# @app.route('/atender')
# def atender():
#     chamada = fila.remover()
#     if chamada:
#         rota, tempo = grafo.dijkstra("Base Central", chamada["local"])
#         acoes = ["Aplicar barreira de contenção", "Criar aceiro"]
#         for acao in acoes:
#             pilha_acoes.empilhar(acao)
#         status_areas.atualizar_status(chamada["local"], "controle em andamento")
#         return render_template("atender.html", chamada=chamada, rota=rota, tempo=tempo, acoes=acoes)
#     return "Nenhuma chamada disponível."

# @app.route('/acoes')
# def acoes():
#     return render_template("acoes.html", acoes=pilha_acoes.pilha[::-1])

# @app.route('/status')
# def status():
#     return render_template("status.html", status=status_areas.exibir())

# if __name__ == '__main__':
#     app.run(debug=True)


# ********************************************************************

from flask import Flask, render_template, request, redirect, url_for
import json
import os

from estruturas.fila import Fila
from estruturas.heap_prioridade import FilaPrioridade
from estruturas.pilha import Pilha
from estruturas.lista_ligada import ListaLigada
from estruturas.grafo import Grafo

app = Flask(__name__)

ultima_area_atendida = None

# Estruturas Globais
fila_chamadas = Fila()
fila_prioridade = FilaPrioridade()
pilha_acoes = Pilha()
lista_status = ListaLigada()
grafo = Grafo()

# Peso da vegetação para prioridade
pesos_vegetacao = {
    "cerrado": 1.2,
    "mata_atlantica": 1.5,
    "pantanal": 2.0
}

# Mapa fixo (grafo)
# grafo.adicionar_aresta("Base Central", "Zona Norte", 10)
# grafo.adicionar_aresta("Base Central", "Mata Alta", 12)
# grafo.adicionar_aresta("Zona Norte", "Mata Alta", 7)

# Variáveis auxiliares
chamadas_carregadas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carregar_chamadas')
def carregar_chamadas():
    global chamadas_carregadas
    with open('dados/chamadas.json') as f:
        chamadas = json.load(f)
        chamadas_carregadas = chamadas
        for chamada in chamadas:
            fila_chamadas.enfileirar(chamada)  # Garante que fila_chamadas tem método enfileirar()
            fila_prioridade.inserir(chamada)   # A prioridade será calculada internamente
    return render_template('chamadas.html', chamadas=chamadas_carregadas)

@app.route('/visualizar_prioridades')
def visualizar_prioridades():
    prioridades_ordenadas = sorted(fila_prioridade.fila)
    print("Prioridades:", prioridades_ordenadas)  # DEBUG
    return render_template('prioridades.html', prioridades=prioridades_ordenadas)


@app.route('/atender')
def atender():
    global ultima_area_atendida

    if fila_prioridade.vazia():
        # Atualiza o status da última área para "área controlada" caso haja uma área pendente
        if ultima_area_atendida is not None:
            lista_status.atualizar_status(ultima_area_atendida, "área controlada")
            ultima_area_atendida = None
        return render_template('atender.html', resultado="Todas as ocorrências foram atendidas.")
    
    # Se existir uma última área, significa que foi atendida antes, então atualiza seu status para "área controlada"
    if ultima_area_atendida is not None:
        lista_status.atualizar_status(ultima_area_atendida, "área controlada")
    
    prioridade, chamada = fila_prioridade.remover()
    origem = "Base Central"
    destino = chamada['local']
    caminho, tempo = grafo.dijkstra(origem, destino)

    # Atualiza status para "controle em andamento" da nova chamada
    lista_status.atualizar_status(destino, "controle em andamento")

    # Atualiza a última área atendida para a atual
    ultima_area_atendida = destino

    # Simular ações
    acoes = ["Criar aceiro", "Aplicar barreira de contenção"]
    for acao in acoes:
        pilha_acoes.empilhar(acao)

    resultado = {
        "chamada": chamada,
        "rota": caminho,
        "tempo": tempo
    }
    return render_template(
        'atender.html',
        chamada=resultado['chamada'],
        rota=resultado['rota'],
        tempo=resultado['tempo'],
        acoes=acoes
    )



@app.route('/acoes')
def acoes():
    acoes_realizadas = pilha_acoes.itens()
    return render_template('acoes.html', acoes=acoes_realizadas)

@app.route('/status')
def status():
    status_areas = lista_status.exibir()
    return render_template('status.html', status=status_areas)

if __name__ == '__main__':
    app.run(debug=True)
