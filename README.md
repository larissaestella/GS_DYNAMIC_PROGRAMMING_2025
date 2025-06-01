combate_queimadas/
│
├── app.py                        # Interface web com Flask
├── main.py                       # Interface CLI
├── requirements.txt              # Dependências do projeto (opcional)
├── dados/
│   └── chamadas.json             # Dados de chamadas de emergência
│
├── estruturas/                   # Estruturas de dados
│   ├── __init__.py
│   ├── fila.py                   # Fila comum
│   ├── heap_prioridade.py        # Fila de prioridade (heap)
│   ├── pilha.py                  # Pilha de ações
│   ├── lista_ligada.py           # Lista ligada para status
│   └── grafo.py                  # Algoritmo de Dijkstra
│
├── templates/                    # Páginas HTML do Flask
│   ├── index.html
│   ├── prioridades.html
│   ├── atender.html
│   ├── acoes.html
│   └── status.html
│
└── tests/                        # Testes unitários com pytest
    ├── __init__.py
    ├── test_fila.py
    ├── test_heap.py
    ├── test_pilha.py
    ├── test_lista_ligada.py
    └── test_grafo.py
