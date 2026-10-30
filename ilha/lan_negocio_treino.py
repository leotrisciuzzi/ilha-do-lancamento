"""Treino do Mundo do lançamento ao negócio (Ilha do Lançamento): faturamento por inscrito, o funil inteiro (visitas →
cadastros → vendas → faturamento) e qual número aponta o passo fraco."""
from .lan_base import MATERIA, alts_reais, classificar, fmt, reais
from .base_mundo import Treino

PREFIXO = "lng-treino"

HABILIDADES = {
    "epi": ("Faturamento por inscrito", "Faturamento ÷ inscritos"),
    "funil": ("O funil inteiro", "Visitas → cadastros → vendas → faturamento"),
    "metrica": ("Que número olhar?", "Problema → métrica"),
}


def _q_epi(rng):
    insc = rng.randrange(1000, 30000, 500)
    epi = rng.choice([4, 6, 8, 10, 12, 15, 20, 25])
    fat = insc * epi
    certo, erradas = alts_reais(rng, epi, [epi * 10, epi / 10 if epi >= 10 else epi + 30, fat / 100, insc / 100], passo=3)
    return (f"Lançamento com {insc} inscritos e faturamento de {reais(fat)}. Faturamento por inscrito:", certo, erradas,
            f"{reais(fat)} ÷ {insc} = {reais(epi)}. É o número que resume o lançamento e convence parceiros.")


def _q_funil(rng):
    vis = rng.randrange(5000, 60000, 5000)
    cap = rng.choice([20, 30, 40, 50])
    conv = rng.choice([1, 2, 3, 4])
    preco = rng.choice([197, 297, 497])
    cad = vis * cap / 100
    vendas = cad * conv / 100
    fat = vendas * preco
    certo, erradas = alts_reais(rng, fat, [vis * conv / 100 * preco, cad * preco, vendas * preco * cap / 100,
                                           vis * cap * conv / 100 * preco], passo=max(1000, round(fat / 8)))
    return (f"{vis} visitas na página de captura (conversão de {cap}%), lista de lançamento convertendo {conv}% em vendas "
            f"a {reais(preco)}. Faturamento:", certo, erradas,
            f"Cadastros = {vis} × {cap}% = {fmt(cad)}; vendas = {fmt(cad)} × {conv}% = {fmt(vendas)}; faturamento = "
            f"{fmt(vendas)} × {reais(preco)} = {reais(fat)}.")


_METRICA = [
    ("Muita visita na página, mas quase ninguém se cadastra", "conversão da página de captura",
     "o problema está na oferta de adesão ou na página."),
    ("Muita gente se inscreve, mas os vídeos têm poucas visualizações e comentários", "engajamento dos conteúdos",
     "o pré-lançamento não prende."),
    ("Os vídeos engajam, mas pouca gente compra na abertura", "conversão da lista em vendas",
     "a oferta não convence ou falta responder a objeção."),
    ("Muita venda, mas muitos pedidos de devolução", "taxa de reembolso", "o produto não entrega o prometido."),
    ("Parceiro quer saber quanto a lista dele vai render", "faturamento por inscrito",
     "resume o lançamento para o parceiro."),
]


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "epi": _q_epi, "funil": _q_funil,
    "metrica": lambda rng: classificar(rng, _METRICA, "Que número olhar primeiro?"),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
