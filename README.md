FELIPE CASQUET FERREIRA – RM553680
JOSEH GABRIEL TRIMBOLI AGRA – RM553094
LARISSA ESTELLA GONÇALVES DOS SANTOS – RM552695

GLOBAL SOLUTION - DYNAMIC PROGRAMMING

Este projeto simula o atendimento a chamadas de emergência relacionadas a queimadas, utilizando estruturas de dados e algoritmos de programação dinâmica. Ele oferece uma interface web desenvolvida com Flask, permitindo a visualização e manipulação das chamadas, priorização de atendimentos e execução de ações de resposta.

🔍 Objetivo

O objetivo principal é demonstrar a aplicação prática de estruturas de dados como filas, pilhas, listas ligadas e grafos em um contexto realista de gerenciamento de emergências, destacando a importância da programação dinâmica na otimização de processos.

🗂️ Estrutura do Projeto

```
GS_DYNAMIC_PROGRAMMING_2025/
├── app.py                 # Interface web com Flask
├── main.py                # Interface de linha de comando (CLI)
├── requirements.txt       # Lista de dependências do projeto
├── dados/
│   └── chamadas.json      # Dados simulados de chamadas de emergência
├── estruturas/
│   ├── __init__.py
│   ├── fila.py            # Implementação de fila comum
│   ├── heap_prioridade.py # Implementação de fila de prioridade (heap)
│   ├── pilha.py           # Implementação de pilha para ações
│   ├── lista_ligada.py    # Implementação de lista ligada para status
│   └── grafo.py           # Algoritmo de Dijkstra para rotas
├── templates/
    ├── index.html
    ├── prioridades.html
    ├── atender.html
    ├── acoes.html
    └── status.html
```
---
🚀 Como Executar

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

📚 Tecnologias Utilizadas
	•	Python 3.11
	•	Flask
	•	Pytest
	•	Estruturas de dados personalizadas (fila, pilha, lista ligada, heap)
	•	Algoritmo de Dijkstra para cálculo de rotas ￼

✨ Funcionalidades
	•	Visualização e gerenciamento de chamadas de emergência
	•	Priorização de atendimentos com base em filas de prioridade
	•	Execução de ações de resposta utilizando pilha
	•	Monitoramento do status das chamadas com listas ligadas
	•	Cálculo de rotas otimizadas para atendimento utilizando grafos ￼

📌 Observações

Este projeto foi desenvolvido como parte de um estudo sobre programação dinâmica e estruturas de dados aplicadas a cenários reais. Contribuições e sugestões são bem-vindas! ￼
