from flask import Flask, render_template, request, redirect, url_for
import json
import os
import random

# Importação das estruturas de dados customizadas

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
chamadas_carregadas = []

# Peso da vegetação para prioridade
pesos_vegetacao = {
    "cerrado": 1.2,
    "mata_atlantica": 1.5,
    "pantanal": 2.0
}

# Equipes Disponíveis
equipes = [
    {"id": 1, "nome": "Equipe Alpha"},
    {"id": 2, "nome": "Equipe Bravo"},
    {"id": 3, "nome": "Equipe Charlie"},
]

@app.route('/home')
def home():
    chamadas_ativas = len(fila_prioridade.itens()) # Chamadas ativas = quantas estão na fila de prioridade

    status_areas = lista_status.exibir() # Status vindo da lista ligada

    em_atendimento = sum(1 for s in status_areas if "controle em andamento" in s)
    atendimentos_concluidos = sum(1 for s in status_areas if "área controlada" in s)

    total_equipes = len(equipes)

    return render_template(
        'index.html',
        chamadas_ativas=chamadas_ativas,
        em_atendimento=em_atendimento,
        atendimentos_concluidos=atendimentos_concluidos,
        total_equipes=total_equipes
    )

@app.route('/carregar_chamadas')
def carregar_chamadas():
    global chamadas_carregadas # Carrega os dados do arquivo JSON e insere nas filas
    with open('dados/chamadas.json') as f:
        chamadas = json.load(f)
        chamadas_carregadas = chamadas
        for chamada in chamadas:
            fila_chamadas.enfileirar(chamada)  
            fila_prioridade.inserir(chamada)   # Ordem por prioridade
    return render_template('chamadas.html', chamadas=chamadas_carregadas)

@app.route('/visualizar_prioridades')
def visualizar_prioridades(): # Exibe as chamadas organizadas pela fila de prioridade
    prioridades_ordenadas = sorted(fila_prioridade.fila)
    print("Prioridades:", prioridades_ordenadas)  # DEBUG
    return render_template('prioridades.html', prioridades=prioridades_ordenadas)

@app.route('/atender')
def atender():
    global ultima_area_atendida, historico_acoes # Simula o atendimento de uma ocorrência

    # Se a fila estiver vazia, finaliza o atendimento anterior
    if fila_prioridade.vazia():
        if ultima_area_atendida is not None:
            lista_status.atualizar_status(ultima_area_atendida, "área controlada")
            ultima_area_atendida = None
        return render_template('atender.html', resultado="Todas as ocorrências foram atendidas.")
    
    # Marca como concluída a ocorrência anterior, se houver
    if ultima_area_atendida is not None:
        lista_status.atualizar_status(ultima_area_atendida, "área controlada")
    
    # Remove a próxima chamada com maior prioridade
    prioridade, chamada = fila_prioridade.remover()
    origem = "Base Central"
    destino = chamada['local']
    caminho, tempo = grafo.dijkstra(origem, destino) # Gera rota otimizada com Dijkstra

    lista_status.atualizar_status(destino, "controle em andamento")
    ultima_area_atendida = destino

    # Ações possíveis para a ocorrência
    acoes_disponiveis = [
            "Criar aceiro",
            "Aplicar barreira de contenção",
            "Pulverizar água nas bordas",
            "Monitorar temperatura do local",
            "Isolar área afetada",
            "Realizar controle de fumaça",
            "Reforçar equipe no local",
            "Avaliar risco de propagação",
            "Usar equipamento de combate manual",
            "Realizar patrulha aérea",
            "Instalar sensores de calor",
            "Acionar reforço de bombeiros",
            "Planejar evacuação",
        ]

    # Seleciona aleatoriamente 5 ações para o atendimento
    acoes = random.sample(acoes_disponiveis, 5)

    # Armazena no histórico as ações realizadas
    historico_acoes.append({
        "id_chamada": chamada['id'],
        "local": chamada['local'],
        "acoes": list(acoes)
    })

    # Empilha as ações realizadas
    for acao in acoes:
        pilha_acoes.empilhar(acao)

    # Informações da ocorrência e da equipe envolvida
    resultado = {
        "chamada": chamada,
        "rota": caminho,
        "tempo": tempo
    }

    equipe = chamada.get('equipe_designada')
    if not equipe:
        equipe = 'Equipe não designada'


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
    if request.method == 'POST': # Adiciona uma nova equipe ao sistema
        nome_novo = request.form['nome']
        if nome_novo:
            novo_id = max([e['id'] for e in equipes]) + 1 if equipes else 1
            equipes.append({"id": novo_id, "nome": nome_novo})
        return redirect(url_for('gerenciar_equipes'))

    return render_template('equipes.html', equipes=equipes)

@app.route('/designar_equipes', methods=['GET', 'POST'])
def designar_equipe():
    if request.method == 'POST': # Atribui uma equipe a uma chamada específica
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
    return render_template('acoes.html', historico=historico_acoes) # Exibe o histórico de ações realizadas

@app.route('/status')
def status():
    status_areas = lista_status.exibir()
    return render_template('status.html', status=status_areas)  # Exibe o status atual das áreas monitoradas

if __name__ == '__main__':
    app.run(debug=True)
