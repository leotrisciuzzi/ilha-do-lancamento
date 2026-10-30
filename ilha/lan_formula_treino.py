"""Treino do Mundo da Fórmula e da lista (Ilha do Lançamento): casos gerados na hora, infinitos.

Gabarito pela conta: conversão da página de captura, leitores de uma lista (tamanho × abertura), cadastros esperados
pelo tráfego e a fase do lançamento pela ação descrita."""
from .lan_base import FASES, MATERIA, classificar, fmt, num_alts
from .base_mundo import Treino

PREFIXO = "lfo-treino"

HABILIDADES = {
    "conversao": ("Taxa de conversão", "Cadastros ÷ visitantes"),
    "leitores": ("Qual lista lê mais?", "Tamanho × abertura"),
    "cadastros": ("Quantos cadastros?", "Visitantes × conversão"),
    "fase": ("Em que fase estamos?", "Ação → fase do lançamento"),
}


def _q_conversao(rng):
    vis = rng.randrange(1000, 20000, 500)
    taxa = rng.choice([15, 20, 25, 30, 35, 40, 45, 50, 60])
    cad = vis * taxa // 100
    certo, erradas = num_alts(rng, taxa, [100 * vis / cad / 10, 100 - taxa, taxa / 2, taxa + 10], passo=5)
    return (f"A página de captura recebeu {vis:,} visitas e gerou {cad:,} cadastros. Taxa de conversão (%):".replace(",", "."),
            certo, erradas, f"Conversão = cadastros ÷ visitantes = {cad} ÷ {vis} = {taxa}%.")


def _q_leitores(rng):
    a_n, a_t = rng.choice([1000, 2000, 5000, 10000]), rng.choice([1, 2, 3, 5])
    b_n, b_t = rng.choice([200, 300, 500, 800]), rng.choice([30, 40, 50, 60])
    la, lb = a_n * a_t // 100, b_n * b_t // 100
    if la == lb:
        b_t += 10
        lb = b_n * b_t // 100
    certa = (f"a de {b_n} contatos, com {lb} leitores" if lb > la else f"a de {a_n} contatos, com {la} leitores")
    erradas = [f"a de {a_n} contatos, com {la} leitores" if lb > la else f"a de {b_n} contatos, com {lb} leitores",
               f"a de {a_n} contatos, porque é a maior", "as duas têm o mesmo número de leitores",
               f"a de {b_n} contatos, com {b_n} leitores", f"a de {a_n} contatos, com {a_n * a_t // 10} leitores"]
    return (f"Lista A: {a_n} contatos e {a_t}% de abertura. Lista B: {b_n} contatos e {b_t}% de abertura. Qual tem mais "
            f"leitores?", certa, erradas,
            f"Leitores = tamanho × abertura: A = {a_n} × {a_t}% = {la}; B = {b_n} × {b_t}% = {lb}. Lista responsiva vale "
            f"mais que lista grande.")


def _q_cadastros(rng):
    vis = rng.randrange(500, 30000, 500)
    taxa = rng.choice([10, 20, 25, 30, 40, 50])
    v = vis * taxa / 100
    certo, erradas = num_alts(rng, v, [vis / taxa, vis * taxa / 10, vis - v, v / 2], passo=50)
    return (f"Uma página de captura converte {taxa}%. Com {vis} visitas, quantos cadastros entram na lista?", certo,
            erradas, f"Cadastros = visitantes × conversão = {vis} × {taxa}% = {fmt(v)}.")


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "conversao": _q_conversao, "leitores": _q_leitores, "cadastros": _q_cadastros,
    "fase": lambda rng: classificar(rng, FASES, "Em que fase do lançamento isso acontece?"),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
