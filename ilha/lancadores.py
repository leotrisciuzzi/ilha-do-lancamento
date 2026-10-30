"""Elenco da Ilha do Lançamento: gente de marketing no lugar dos médicos.

Mesmo mecanismo do elenco do Vestibulando (estudantes.py): troca, dentro de heroi.py, o catálogo de personagens,
roupas e bastões. Reaproveita o corpo de pé e as cabeças desenhadas para os estudantes, com camisa na cor da roupa
e ferramentas de escritório no lugar dos bastões médicos.

Personagens: Lançador e Lançadora (já vêm), Copywriter 150, Afiliado 200, Influencer 250."""
from . import estudantes as E
from . import heroi

PERSONAGENS = {
    "lancador": dict(
        nome="Lançador", artigo="o", preco=0, tipo="pe", cab=E.CAB_VESTIBULANDO,
        pal={"h": (62, 42, 32), "j": (104, 74, 56), "F": (232, 182, 140), "f": (194, 138, 100), "N": (40, 28, 36),
             "M": (190, 80, 90), "P": (246, 150, 130), "X": (240, 150, 40), "x": (180, 96, 20)},
        desc="Mochila com o notebook e a data da abertura na cabeça",
        padrao={"nuvem": "celeste", "bastao": "caneta", "roupa": "camisa_azul"}),
    "lancadora": dict(
        nome="Lançadora", artigo="a", preco=0, tipo="pe", cab=heroi.DOUTORA[:15],
        pal={"h": (138, 74, 40), "j": (190, 118, 66), "F": (246, 200, 164), "f": (214, 154, 116), "N": (44, 30, 36),
             "M": (210, 80, 100), "P": (250, 150, 140), "a": (90, 160, 250), "X": (150, 90, 210), "x": (96, 52, 150)},
        desc="Rabo de cavalo, roteiro dos três vídeos pronto e lista aquecida",
        padrao={"nuvem": "lilas", "bastao": "marcatexto", "roupa": "camisa_amarela"}),
    "copywriter": dict(
        nome="Copywriter", artigo="o", preco=150, tipo="pe", cab=E.CAB_GABARITADOR,
        pal={"h": (28, 24, 32), "j": (52, 46, 60), "F": (240, 196, 158), "f": (204, 150, 116), "N": (36, 36, 56),
             "M": (180, 80, 90), "X": (60, 70, 90), "x": (36, 42, 56)},
        desc="Óculos de aro grosso: escreve o e-mail de abertura em três frases",
        padrao={"nuvem": "branca", "bastao": "lapiseira", "roupa": "camisa_verde"}),
    "afiliado": dict(
        nome="Afiliado", artigo="o", preco=200, tipo="pe", cab=E.CAB_SKATISTA,
        pal={"h": (40, 28, 24), "j": (80, 56, 44), "F": (176, 118, 80), "f": (138, 88, 58), "N": (30, 20, 22),
             "M": (150, 60, 66), "P": (200, 120, 100), "C": (228, 60, 60), "c": (150, 30, 40),
             "X": (40, 40, 48), "x": (20, 20, 26)},
        desc="Boné para trás e link rastreado no bolso: vive de comissão",
        padrao={"nuvem": "menta", "bastao": "regua", "roupa": "camisa_preta"}),
    "influencer": dict(
        nome="Influencer", artigo="a", preco=250, tipo="pe", cab=heroi.CABECAS["cachos"],
        pal={"h": (34, 22, 24), "j": (78, 54, 56), "F": (138, 90, 62), "f": (106, 66, 44), "N": (24, 14, 18),
             "M": (170, 60, 80), "P": (188, 104, 92), "X": (230, 70, 140), "x": (160, 40, 96)},
        desc="Black power e comunidade engajada: os comentários não param",
        padrao={"nuvem": "pessego", "bastao": "lapis", "roupa": "camisa_roxa"}),
}

ROUPAS = {
    "camisa_azul": dict(nome="Camisa azul", preco=0, desc="A camisa do Lançador", cor=(70, 130, 220)),
    "camisa_amarela": dict(nome="Camisa amarela", preco=0, desc="A camisa da Lançadora", cor=(250, 200, 60)),
    "camisa_verde": dict(nome="Camisa verde", preco=60, desc="Verde de gráfico subindo (vem com o Copywriter)",
                         cor=(50, 170, 90)),
    "camisa_preta": dict(nome="Camisa preta", preco=60, desc="Básica (vem com o Afiliado)", cor=(52, 50, 64)),
    "camisa_roxa": dict(nome="Camisa roxa", preco=60, desc="Roxo de marca forte (vem com a Influencer)",
                        cor=(140, 80, 200)),
    "camisa_vermelha": dict(nome="Camisa vermelha", preco=60, desc="Cor do botão de compra", cor=(220, 60, 60)),
    "blazer_cinza": dict(nome="Blazer cinza", preco=90, desc="Para a reunião com o parceiro grande",
                         cor=(150, 154, 166)),
    "camisa_laranja": dict(nome="Camisa laranja", preco=120, desc="Cor do carrinho aberto", cor=(250, 140, 40)),
    "camisa_branca": dict(nome="Camisa branca", preco=120, desc="Limpa como página de captura sem distração",
                          cor=(236, 236, 242)),
}

BASTOES = {
    "caneta": dict(nome="Caneta de copy", preco=0, desc="Tinta azul para o e-mail de abertura (vem com o Lançador)"),
    "marcatexto": dict(nome="Marca-texto", preco=0, desc="Grifa a objeção nos comentários (vem com a Lançadora)"),
    "lapiseira": dict(nome="Lapiseira", preco=100, desc="Metal e grafite 0,7 para revisar a oferta (vem com o Copywriter)"),
    "regua": dict(nome="Régua de métricas", preco=120, desc="Mede a conversão de cada página (vem com o Afiliado)"),
    "lapis": dict(nome="Lápis de roteiro", preco=150, desc="Rascunha os três vídeos (vem com a Influencer)"),
}
NUVENS_DESC = {
    "lilas": "A nuvem da Lançadora",
    "menta": "Fresca como lista recém-aquecida (vem com o Afiliado)",
    "fogo": "Para o pico do último dia de carrinho aberto",
    "celeste": "Azul de céu limpo (vem com o Lançador)",
    "branca": "Nuvem de verdade (vem com o Copywriter)",
    "pessego": "Laranja-rosado de fim de tarde (vem com a Influencer)",
    "neve": "Flocos brilhando como notificações de venda",
    "aurora": "Verde e violeta dançando no céu",
    "oceano": "Azul do mar com espuma",
    "floresta": "Verde-mata",
    "chumbo": "Azul-marinho da madrugada antes da abertura",
}


def ativar():
    """Troca o elenco de heroi.py pelo dos lançadores (chamado por edicao.ativar_lancamento)."""
    if heroi.PADRAO == "lancador":
        return
    heroi.PERSONAGENS.clear()
    for pid, d in PERSONAGENS.items():
        heroi.CABECAS[pid] = d["cab"]
        heroi.CORPOS[pid] = E.CORPO
        heroi.CARAS[pid] = E._caras(d["cab"]) if pid not in heroi.CARAS else heroi.CARAS[pid]
        dados = {k: v for k, v in d.items() if k != "cab"}
        dados["pal"] = {**E.PAL_BASE, **d["pal"]}
        heroi.PERSONAGENS[pid] = dados
    heroi.CARAS["lancadora"] = heroi.CARAS["doutora"]
    heroi.CARAS["influencer"] = heroi.CARAS["cachos"]
    heroi.ROUPAS.clear()
    heroi.ROUPAS.update(ROUPAS)
    for b in E.SAEM:
        heroi.BASTOES.pop(b, None)
    nenhum = heroi.BASTOES.pop("nenhum")
    resto = dict(heroi.BASTOES)
    heroi.BASTOES.clear()
    heroi.BASTOES.update({"nenhum": nenhum, **BASTOES, **resto})
    for n, txt in NUVENS_DESC.items():
        heroi.NUVENS[n]["desc"] = txt
    heroi.PAL_BASTAO.update(E.PAL_BASTAO)
    heroi.GRADES_EXTRA.append(E._grade)
    heroi.PADRAO = "lancador"
    heroi.equipar({"personagem": "lancador"})
