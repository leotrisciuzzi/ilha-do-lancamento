#!/usr/bin/env python3
"""Ilha do Lançamento — ponto de entrada (Linux: ./ilha-do-lancamento).
    python ilha_do_lancamento.py [--mudo] [--tela-cheia]"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    from ilha import edicao
    edicao.ativar_lancamento()
    from ilha.ui import App
    App(mudo="--mudo" in sys.argv, tela_cheia="--tela-cheia" in sys.argv).loop()


if __name__ == "__main__":
    main()
