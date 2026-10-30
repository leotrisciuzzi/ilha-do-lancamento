"""Treino do Mundo do Seed Launch e dos parceiros (Ilha do Lançamento): comissão do parceiro, vendas esperadas pelo
faturamento por inscrito, tamanho da microlista e qual tipo de lançamento cabe em cada situação."""
from .lan_base import MATERIA, alts_reais, classificar, reais
from .base_mundo import Treino

PREFIXO = "lsj-treino"

HABILIDADES = {
    "comissao": ("Comissão do parceiro", "Vendas × preço × %"),
    "por_inscrito": ("Vendas pelo inscrito", "Inscritos × faturamento por inscrito"),
    "tipo": ("Qual lançamento fazer?", "Situação → Seed, Interno ou Conjunto"),
}


def _q_comissao(rng):
    vendas = rng.randrange(5, 120, 5)
    preco = rng.choice([197, 297, 497, 997, 1497])
    pct = rng.choice([30, 40, 50])
    v = vendas * preco * pct / 100
    certo, erradas = alts_reais(rng, v, [vendas * preco, vendas * preco * (100 - pct) / 100, preco * pct / 100,
                                         vendas * pct], passo=max(500, round(v / 10)))
    return (f"Curso de {reais(preco)} com comissão de {pct}%. O parceiro indicou {vendas} vendas. Quanto ele recebe?",
            certo, erradas, f"{vendas} × {reais(preco)} × {pct}% = {reais(v)}. O restante fica com o dono do produto.")


def _q_por_inscrito(rng):
    insc = rng.randrange(500, 20000, 500)
    epi = rng.choice([5, 8, 10, 12, 15, 20])
    v = insc * epi
    certo, erradas = alts_reais(rng, v, [insc * epi / 10, insc + epi, v * 10, insc], passo=max(1000, round(v / 8)))
    return (f"O último lançamento faturou {reais(epi)} por inscrito. Um parceiro vai mandar {insc} inscritos. Vendas "
            f"esperadas:", certo, erradas,
            f"{insc} × {reais(epi)} = {reais(v)}. É o número que convence o parceiro a divulgar.")


_TIPO = [
    ("Começando agora, sem lista e sem produto", "Seed Launch", "microlista e venda antes de criar."),
    ("Ideia nova de produto que você quer testar antes de criar", "Seed Launch", "testa a ideia com o mercado."),
    ("Produto pronto e lista própria de 3.000 pessoas, sem parceiros", "Lançamento Interno", "lançamento para a sua lista."),
    ("Produto testado, boa conversão e vários parceiros com listas grandes", "Lançamento Conjunto",
     "parceiros mandam público por comissão."),
]


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "comissao": _q_comissao, "por_inscrito": _q_por_inscrito,
    "tipo": lambda rng: classificar(rng, _TIPO, "Que tipo de lançamento faz mais sentido?",
                                    extras=["Lançamento sem pré-lançamento", "Anúncio pago sem lista"]),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
