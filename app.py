# app.py

from flask import Flask, render_template, redirect, url_for
import json
from estruturas.fila import FilaChamadas
from estruturas.heap_prioridade import FilaPrioridade
from estruturas.pilha import PilhaAcoes
from estruturas.lista_ligada import ListaStatus
from estruturas.grafo import dijkstra

app = Flask(__name__)

fila = FilaChamadas()
heap = FilaPrioridade()
pilha_acoes = PilhaAcoes()
lista_status = ListaStatus()

def carregar_chamadas():
    with open('dados/chamadas.json') as f:
        chamadas = json.load(f)
        for chamada in chamadas:
            fila.enfileirar(chamada)
            heap.inserir(chamada)
            lista_status.inserir_status(chamada['local'], 'ativo')

mapa = {
    "Base Central": {"Zona Norte": 10, "Mata Alta": 12},
    "Zona Norte": {"Mata Alta": 7},
    "Mata Alta": {"Zona Norte": 7}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carregar')
def carregar():
    carregar_chamadas()
    return redirect(url_for('index'))

@app.route('/prioridades')
def prioridades():
    prioridades = sorted([(-p, c) for p, c in heap.heap], reverse=True)
    return render_template('prioridades.html', prioridades=prioridades)

@app.route('/atender')
def atender():
    chamada = heap.remover()
    if not chamada:
        return render_template('atender.html', chamada=None)

    origem = "Base Central"
    destino = chamada['local']
    caminho, tempo = dijkstra(mapa, origem, destino)
    acoes = ["Aplicar barreira de contenção", "Criar aceiro"]
    for acao in acoes:
        pilha_acoes.registrar_acao(acao)
    lista_status.atualizar_status(destino, "controle em andamento")

    return render_template('atender.html', chamada=chamada, rota=caminho, tempo=tempo, acoes=acoes)

@app.route('/acoes')
def acoes():
    return render_template('acoes.html', acoes=reversed(pilha_acoes.pilha))

@app.route('/status')
def status():
    atual = lista_status.head
    status_list = []
    while atual:
        status_list.append((atual.area, atual.status))
        atual = atual.proximo
    return render_template('status.html', status_list=status_list)

if __name__ == '__main__':
    app.run(debug=True)
