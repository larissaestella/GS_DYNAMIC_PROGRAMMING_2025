## Integrantes

* FELIPE CASQUET FERREIRA – RM553680
* JOSEH GABRIEL TRIMBOLI AGRA – RM553094
* LARISSA ESTELLA GONÇALVES DOS SANTOS – RM552695

# GLOBAL SOLUTION - DYNAMIC PROGRAMMING

## Descrição

Este sistema simula uma **central inteligente de resposta a focos de queimadas**, com prioridade baseada em severidade e tipo de vegetação, designação de equipes, rotas otimizadas com Dijkstra e registro das ações de contenção.

O objetivo é integrar **estruturas de dados eficientes** com uma interface web responsiva, visualmente clara e informativa, auxiliando a tomada de decisão no combate a desastres ambientais.

---

## 🔍 Objetivo

O objetivo principal é demonstrar a aplicação prática de estruturas de dados como filas, pilhas, listas ligadas e grafos em um contexto realista de gerenciamento de emergências, destacando a importância da programação dinâmica na otimização de processos.

---

## 📌 Funcionalidades

- 📥 **Carregamento de Chamadas** via JSON
- 🚨 **Fila de Prioridade** com heap (baseada em severidade e tipo de vegetação)
- 🧭 **Cálculo de Rotas Otimizadas** utilizando grafos e algoritmo de Dijkstra
- 🔁 **Controle de Ações** com pilha e histórico
- 🔁 **Monitoramento do Status** com listas ligadas
- 📊 **Painel de Status Dinâmico** com gráficos Chart.js
- 🌐 **Interface Web com Flask**

---

## 🗂️ Estrutura de Arquivos

```
GS_DYNAMIC_PROGRAMMING_2025/
├── app.py                 # Interface web com Flask
├── requirements.txt       # Lista de dependências do projeto
├── README.md
├── dados/
│   └── chamadas.json      # Dados simulados de chamadas de emergência
├── estruturas/
│   ├── __init__.py
│   ├── fila.py            # Implementação de fila comum
│   ├── heap_prioridade.py # Implementação de fila de prioridade (heap)
│   ├── pilha.py           # Implementação de pilha para ações
│   ├── lista_ligada.py    # Implementação de lista ligada para status
│   └── grafo.py           # Algoritmo de Dijkstra para rotas
├── static/
    ├── style.css
├── templates/
    ├── acoes.html
    ├── atender.html
    ├── chamadas.html
    ├── designar_equipes.html
    ├── equipes.html
    ├── index.html
    ├── prioridades.html
    └── status.html
```
---

## 🚀 Como Executar

1. **Clone esse repositório ou baixe os arquivos** para sua máquina.
2. Verifique se você tem o Python 3 instalado.
3. No terminal, navegue até a pasta do projeto:

   ```bash
   cd caminho/para/GS_DYNAMIC_PROGRAMMING_2025
   ```
4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```
5. Execute a aplicação:

   ```bash
   python app.py
   ```
6. Acesse o sistema no navegador via:

   ```bash
   http://localhost:5000
   ```
---

### 📦 Dependências

Certifique-se de instalar as dependências listadas no arquivo requirements.txt para rodar o projeto corretamente:

   ```
    Flask 
   ```

---

## 🎯 Exemplo de Fluxo

1. O usuário carrega as chamadas via `/carregar_chamadas`
2. O sistema calcula e organiza as prioridades em `/visualizar_prioridades`
3. Após verificar qual a sequência de prioridade o usuário escolhe as equipes em `/designar_equipes`, caso queira adicionar novas pode seguir em `/equipes`
3. A opção "Atender Ocorrência" em `/atender` executa o atendimento à chamada de maior prioridade, exibindo ID, local, rota e equipe designada
4. A rota é exibida com início, destino, caminho percorrido e tempo
5. Ações são registradas via pilha que será exibido em `/acoes`
6. Status são atualizados dinamicamente em `/status`
7. Dashboard atualiza em tempo real na `/home`

---

## 🌐 Interface

A aplicação web exibe:

- 🔥 **Chamadas Ativas**: número de ocorrências pendentes  
- ⏳ **Em Atendimento**: áreas sendo atendidas  
- ✅ **Concluídas**: locais já controlados  
- 👨‍🚒 **Equipes Ativas**: número de equipes disponíveis  
- 📊 **Gráfico** com o progresso dos atendimentos  

---

## 🧪 Tecnologias e Conceitos

* **Python**
* **Flask**
* **HTML + CSS (responsivo)**
* **JavaScript + Chart.js**
* **Algoritmo de Dijkstra**
* **Heap de prioridade**
* **Estruturas lineares: pilha, fila, lista ligada**
* **Design UI/UX responsivo e acessível**

---


## 🧠 Estruturas de Dados Utilizadas

| Estrutura | Função |
|----------|--------|
| `Fila de Prioridade (Heap)` | Ordena e recupera ocorrências com maior prioridade |
| `Lista Ligada` | Armazena status das áreas afetadas |
| `Pilha` | Armazena ações executadas por ocorrência |
| `Grafo` | Representa o mapa com pesos e calcula a rota mais curta com Dijkstra |
| `Fila Simples` | Armazena chamadas para atendimento sequencial |

---


## 🎓 Desenvolvido para

**Global Solution FIAP - 2025
Engenharia de Software**

