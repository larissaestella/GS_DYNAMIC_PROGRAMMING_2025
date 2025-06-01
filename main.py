# main.py

import json
from estruturas.fila import FilaChamadas
from estruturas.heap_prioridade import FilaPrioridade
from estruturas.pilha import PilhaAcoes
from estruturas.lista_ligada import ListaStatus
from estruturas.grafo import dijkstra

# Carga de dados
with open('dados/chamadas.json') as f:
    chamadas_emergencia = json.load(f)

# Mapa exemplo (grafo)
mapa = {
    "Base Central": {"Zona Norte": 10, "Mata Alta": 12},
    "Zona Norte": {"Mata Alta": 7},
    "Mata Alta": {"Zona Norte": 7}
}

fila = FilaChamadas()
heap = FilaPrioridade()
pilha_acoes = PilhaAcoes()
lista_status = ListaStatus()

def carregar_chamadas():
    for chamada in chamadas_emergencia:
        fila.enfileirar(chamada)
        heap.inserir(chamada)
        lista_status.inserir_status(chamada['local'], 'ativo')
    print("Chamadas carregadas.")

def visualizar_prioridades():
    print("Chamadas por prioridade:")
    for prioridade, chamada in sorted(heap.heap, reverse=True):
        print(f"ID: {chamada['id']} | Local: {chamada['local']} | Prioridade: {-prioridade:.2f}")

def atender_ocorrencia():
    chamada = heap.remover()
    if not chamada:
        print("Nenhuma ocorrência na fila de prioridade.")
        return
    origem = "Base Central"
    destino = chamada['local']
    caminho, tempo = dijkstra(mapa, origem, destino)
    acoes = ["Aplicar barreira de contenção", "Criar aceiro"]
    for acao in acoes:
        pilha_acoes.registrar_acao(acao)
    lista_status.atualizar_status(destino, "controle em andamento")
    print(f"Ocorrência atendida: {chamada['id']}")
    print(f"Rota: {caminho} | Tempo estimado: {tempo}")
    print(f"Ações realizadas: {acoes}")

def ver_pilha_acoes():
    print("Histórico de Ações:")
    for acao in reversed(pilha_acoes.pilha):
        print(f"- {acao}")

def ver_status_areas():
    print("Status das Áreas:")
    atual = lista_status.head
    while atual:
        print(f"{atual.area}: {atual.status}")
        atual = atual.proximo

def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Carregar chamadas do JSON")
        print("2 - Visualizar fila de prioridade")
        print("3 - Atender próxima ocorrência")
        print("4 - Ver ações realizadas (Pilha)")
        print("5 - Ver status das áreas afetadas")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            carregar_chamadas()
        elif opcao == '2':
            visualizar_prioridades()
        elif opcao == '3':
            atender_ocorrencia()
        elif opcao == '4':
            ver_pilha_acoes()
        elif opcao == '5':
            ver_status_areas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
