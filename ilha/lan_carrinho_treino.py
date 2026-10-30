"""Treino do Mundo da abertura do carrinho (Ilha do Lançamento): faturamento do lançamento (lista × conversão ×
preço), vendas por dia com os dois picos, quanto a garantia devolve e a parte da oferta que responde a cada objeção."""
from .lan_base import MATERIA, alts_reais, classificar, fmt, num_alts, reais
from .base_mundo import Treino

PREFIXO = "lca-treino"

HABILIDADES = {
    "faturamento": ("Faturamento do lançamento", "Lista × conversão × preço"),
    "fechamento": ("Vendas do último dia", "Total × fatia do fechamento"),
    "liquido": ("Faturamento líquido", "Bruto menos reembolsos da garantia"),
    "objecao": ("Que parte da oferta responde?", "Objeção → parte da oferta"),
}


def _q_faturamento(rng):
    lista = rng.choice([800, 1500, 3000, 5000, 12000, 20000])
    conv = rng.choice([1, 2, 3, 5])
    preco = rng.choice([97, 197, 297, 497, 997])
    vendas = lista * conv / 100
    fat = vendas * preco
    certo, erradas = alts_reais(rng, fat, [lista * preco, vendas * preco / 10, lista * conv * preco, vendas + preco],
                                passo=max(1000, round(fat / 10)))
    return (f"Lista de lançamento com {lista} pessoas, conversão de {conv}% e preço de {reais(preco)}. Faturamento "
            f"esperado:", certo, erradas,
            f"Vendas = {lista} × {conv}% = {fmt(vendas)}; faturamento = {fmt(vendas)} × {reais(preco)} = {reais(fat)}.")


def _q_fechamento(rng):
    tot = rng.randrange(40, 600, 10)
    pct = rng.choice([30, 35, 40, 45, 50])
    v = tot * pct / 100
    certo, erradas = num_alts(rng, v, [tot - v, tot / 5, tot * pct / 10, pct], passo=5)
    return (f"O lançamento vendeu {tot} vagas em 5 dias, e {pct}% vieram nas últimas 24 horas. Quantas vendas no último "
            f"dia?", certo, erradas,
            f"{tot} × {pct}% = {fmt(v)}. O pico final é a escassez: sem fechamento real, boa parte dessas vendas some.")


def _q_liquido(rng):
    vendas = rng.randrange(30, 400, 10)
    preco = rng.choice([97, 197, 297, 497])
    reemb = rng.choice([2, 3, 5, 8, 10])
    bruto = vendas * preco
    liq = bruto * (100 - reemb) / 100
    certo, erradas = alts_reais(rng, liq, [bruto, bruto * reemb / 100, bruto - reemb * preco, liq / 2],
                                passo=max(500, round(liq / 12)))
    return (f"{vendas} vendas a {reais(preco)} e {reemb}% de pedidos de reembolso pela garantia. Faturamento líquido:",
            certo, erradas,
            f"Bruto = {vendas} × {reais(preco)} = {reais(bruto)}; líquido = bruto × (100 − {reemb})% = {reais(liq)}. A "
            f"garantia custa pouco e tira o medo de quem compra.")


_OBJ = [
    ("'É caro para pagar de uma vez'", "condições de pagamento, como parcelar", "a barreira é o valor à vista."),
    ("'E se eu não gostar ou não conseguir?'", "garantia", "a garantia transfere o risco."),
    ("'Não sei se isso serve para o meu caso'", "depoimentos de quem tem o mesmo perfil", "prova social do caso parecido."),
    ("'Depois eu compro, sem pressa'", "fechamento com bônus que sai do ar", "a escassez real tira o adiamento."),
    ("'Não tenho tempo para um curso longo'", "produto em aulas curtas e um bônus de atalhos",
     "o produto em si responde à falta de tempo."),
]


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "faturamento": _q_faturamento, "fechamento": _q_fechamento, "liquido": _q_liquido,
    "objecao": lambda rng: classificar(rng, _OBJ, "Que parte da oferta responde melhor a essa objeção?"),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
