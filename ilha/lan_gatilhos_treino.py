"""Treino do Mundo de vender sem empurrar (Ilha do Lançamento): cena → estímulo mental, e qual estímulo cada fase
acende. Gabarito pela tabela do livro (capítulo 5)."""
from .lan_base import GATILHOS, MATERIA, classificar
from .base_mundo import Treino

PREFIXO = "lgt-treino"

HABILIDADES = {
    "gatilho": ("Qual estímulo mental?", "Cena → estímulo"),
    "momento": ("Que estímulo nesta hora?", "Momento do lançamento → estímulo principal"),
}

_MOMENTO = [
    ("Pico de vendas no último dia de carrinho aberto", "escassez", "a consequência de perder faz agir."),
    ("Pico de vendas na primeira hora da abertura", "expectativa", "quem esperava compra logo."),
    ("Centenas de comentários de quem está acompanhando os vídeos", "prova social",
     "ver os outros participando puxa a decisão."),
    ("Vídeo gratuito que já resolve um problema real do público", "reciprocidade", "valor recebido pede retribuição."),
    ("Contagem regressiva para a abertura na segunda às 10 horas", "eventos e rituais", "a venda vira acontecimento."),
]


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "gatilho": lambda rng: classificar(rng, GATILHOS, "Que estímulo mental está em ação?"),
    "momento": lambda rng: classificar(rng, _MOMENTO, "Que estímulo explica isso?",
                                       extras=["autoridade", "simpatia", "comunidade"]),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
