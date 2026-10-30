# Ilha do Lançamento

Jogo de plataforma em pixel art para estudar lançamento de produtos e marketing digital: você corre, pula e
enfrenta os bichos-questão. São 6 mundos (90 perguntas comentadas e treinos gerados na hora), na ordem dos
capítulos do livro *Launch* / *A Fórmula do Lançamento* (Jeff Walker).

## Jogar

```bash
python3 -m venv venv && venv/bin/pip install pygame-ce numpy
./ilha-do-lancamento          # ou: venv/bin/python ilha_do_lancamento.py [--mudo] [--tela-cheia]
```

Teste automático: `venv/bin/python tests/lancamento_test.py /tmp/saida`.

## Licença

Código: MIT (`LICENSE`) — © 2026 Leonardo Trisciuzzi. Avisos e terceiros: `NOTICE.md`.
