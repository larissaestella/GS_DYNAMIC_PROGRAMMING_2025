from flask import Flask, render_template, request, redirect, url_for
import json
import os

from estruturas.fila import Fila
from estruturas.heap_prioridade import FilaPrioridade
from estruturas.pilha import Pilha
from estruturas.lista_ligada import ListaLigada
from estruturas.grafo import Grafo

app = Flask(__name__)

# Estruturas Globais
ultima_area_atendida = None
historico_acoes = []
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

# Designar uma ocorrência para uma equipe

equipes = [
    {"id": 1, "nome": "Equipe Alpha"},
    {"id": 2, "nome": "Equipe Bravo"},
    {"id": 3, "nome": "Equipe Charlie"},
]



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


import random

@app.route('/atender')
def atender():
    global ultima_area_atendida, historico_acoes

    if fila_prioridade.vazia():
        if ultima_area_atendida is not None:
            lista_status.atualizar_status(ultima_area_atendida, "área controlada")
            ultima_area_atendida = None
        return render_template('atender.html', resultado="Todas as ocorrências foram atendidas.")
    
    if ultima_area_atendida is not None:
        lista_status.atualizar_status(ultima_area_atendida, "área controlada")
    
    prioridade, chamada = fila_prioridade.remover()
    origem = "Base Central"
    destino = chamada['local']
    caminho, tempo = grafo.dijkstra(origem, destino)

    lista_status.atualizar_status(destino, "controle em andamento")
    ultima_area_atendida = destino

    acoes = ["Criar aceiro", "Aplicar barreira de contenção", "Monitorar focos", "Usar equipamento de resfriamento"]

    # Registrar no histórico as ações feitas para essa chamada
    historico_acoes.append({
        "id_chamada": chamada['id'],
        "local": chamada['local'],
        "acoes": list(acoes)  # copia da lista
    })

    for acao in acoes:
        pilha_acoes.empilhar(acao)

    resultado = {
        "chamada": chamada,
        "rota": caminho,
        "tempo": tempo
    }

    equipe = chamada.get('equipe_designada', 'Equipe não designada')

    return render_template(
        'atender.html',
        chamada=resultado['chamada'],
        rota=resultado['rota'],
        tempo=resultado['tempo'],
        acoes=acoes, 
        equipe=equipe
    )

@app.route('/equipes', methods=['GET', 'POST'])
def gerenciar_equipes():
    if request.method == 'POST':
        nome_novo = request.form['nome']
        if nome_novo:
            novo_id = max([e['id'] for e in equipes]) + 1 if equipes else 1
            equipes.append({"id": novo_id, "nome": nome_novo})
        return redirect(url_for('gerenciar_equipes'))

    return render_template('equipes.html', equipes=equipes)

@app.route('/designar_equipes', methods=['GET', 'POST'])
def designar_equipe():
    if request.method == 'POST':
        id_ocorrencia = int(request.form['id_ocorrencia'])
        id_equipe = int(request.form['id_equipe'])

        for chamada in fila_chamadas:
            if chamada['id'] == id_ocorrencia:
                equipe = next((e for e in equipes if e['id'] == id_equipe), None)
                if equipe:
                    chamada['equipe_designada'] = equipe['nome']
                break

        return redirect('/designar_equipes')

    return render_template('designar_equipes.html', chamadas=fila_chamadas, equipes=equipes)


@app.route('/acoes')
def acoes():
    return render_template('acoes.html', historico=historico_acoes)



@app.route('/status')
def status():
    status_areas = lista_status.exibir()
    return render_template('status.html', status=status_areas)

if __name__ == '__main__':
    app.run(debug=True)
