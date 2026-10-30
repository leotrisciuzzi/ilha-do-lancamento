"""Elenco da Ilha do Vestibulando: estudantes no lugar dos médicos.

ativar() troca, dentro de heroi.py, o catálogo de personagens, roupas e bastões (a edição roda um elenco
só por processo): todos de pé na nuvem, com corpo próprio (camiseta na cor da roupa, mochila nas costas,
jeans e tênis) e material escolar no lugar dos bastões médicos. O resto (nuvens, golpe de bastão, loja,
escolha de personagem) é o mesmo motor.

Personagens: Vestibulando e Vestibulanda (já vêm), Gabaritador 150, Skatista 200, Black Power 250."""
from . import heroi

# corpo do estudante (linhas 15–29 do sprite 20x30; a mão da frente fica em (18, 3), como no jaleco)
CORPO = """
.....KUUUuuuUUUK....
..KKKXUUUUuUUUUUK...
.KXXKXUUUUUUUUUUUKK.
.KXxKXUUUUUUUUUUUUFK
.KXxKXUUUUUUUUUUUUFK
.KXxKXUUUUUUUUUUKKK.
.KXxKXUUUUUUUUUUK...
.KxxKXUUUUUUUUUUK...
..KKKuuuuuuuuuuuK...
.....KDDDDDDDDDK....
.....KDDDkKDDDkK....
.....KDDDkKDDDkK....
.....KDDDkKDDDkK....
.....KWWRWKWWRWWK...
.....KKKKKKKKKKKK...
""".split()

CAB_VESTIBULANDO = """
......K.KK.K........
....KKhKhhKhKK......
...KhhhhhhhhhhKK....
..KhhjhhhjhhhhhhK...
..KhhhhhhhhhhhhhK...
..KhhhhhhhhhhFFhK...
..KhhhhhhhFFFFFFK...
..KhhhhhhFFFFFFFFK..
..KhhFFhfFFFNFFFNK..
..KhFffhfFFFNFFFNF..
..KhhFFffFFPFFFPFK..
...KhhhfFFFFFFFFK...
....KhhKfFFFFMMFK...
.....KKKKffffFK.....
......KKKKKKKKK.....
""".split()

# óculos de aro grosso (N) e cabelo repartido de lado
CAB_GABARITADOR = """
.......KKKKKK.......
.....KKhhhhjjKK.....
....KhhhhhjjjjhK....
...KhhhhhjjjjjjhK...
..KhhhhhhhhhhhhhK...
..KhhhhhhhhhFFFhK...
..KhhhhhhhFFFFFFK...
..KhhhhhhNNNNNNNNNK.
..KhhFFhNFKFNNFKFN..
..KhFffhNFFFNNFFFN..
..KhhFFffNNNFFNNNK..
...KhhhfFFFFFFFFK...
....KhhKfFFFFMMFK...
.....KKKKffffFK.....
......KKKKKKKKK.....
""".split()

# boné virado para trás (C/c), aba apontando para as costas
CAB_SKATISTA = """
......KKKKKKK.......
....KKCCCCCCCKK.....
...KCCCcCCCCCCCK....
KKKKCCCCCCCCCCCK....
KccKCCCCCCCCCCCCK...
.KKKKKKKKKKKKKKKK...
..KhhhhhhhhFFFFhK...
..KhhhhhhFFFFFFFFK..
..KhhFFhfFFFNFFFNK..
..KhFffhfFFFNFFFNF..
..KhhFFffFFPFFFPFK..
...KhhhfFFFFFFFFK...
....KhhKfFFFFMMFK...
.....KKKKffffFK.....
......KKKKKKKKK.....
""".split()


def _caras(cab):
    """Piscada (olhos viram traço) e susto (boca aberta), derivadas da cabeça."""
    linhas = [k for k, l in enumerate(cab) if "N" in l and "NNN" not in l and "NN" not in l]
    pisca = {}
    if len(linhas) >= 2:
        pisca = {linhas[0]: cab[linhas[0]].replace("N", "F"), linhas[1]: cab[linhas[1]].replace("N", "K")}
    elif any("FKF" in l for l in cab):           # de óculos: a pupila (K) some
        pisca = {k: l.replace("FKF", "FFF") for k, l in enumerate(cab) if "FKF" in l}
    boca = next(k for k, l in enumerate(cab) if "MM" in l)
    return {"pisca": pisca, "susto": {boca: cab[boca].replace("FMMF", "KMKF")}}


PAL_BASE = {"D": (70, 100, 160), "k": (44, 64, 110), "W": (246, 246, 250), "R": (226, 60, 60)}
PERSONAGENS = {
    "vestibulando": dict(
        nome="Vestibulando", artigo="o", preco=0, tipo="pe", cab=CAB_VESTIBULANDO,
        pal={"h": (62, 42, 32), "j": (104, 74, 56), "F": (232, 182, 140), "f": (194, 138, 100), "N": (40, 28, 36),
             "M": (190, 80, 90), "P": (246, 150, 130), "X": (240, 150, 40), "x": (180, 96, 20)},
        desc="Mochila laranja, lápis na mão e a cabeça no ENEM",
        padrao={"nuvem": "celeste", "bastao": "lapis", "roupa": "cam_azul"}),
    "vestibulanda": dict(
        nome="Vestibulanda", artigo="a", preco=0, tipo="pe", cab=heroi.DOUTORA[:15],
        pal={"h": (138, 74, 40), "j": (190, 118, 66), "F": (246, 200, 164), "f": (214, 154, 116), "N": (44, 30, 36),
             "M": (210, 80, 100), "P": (250, 150, 140), "a": (90, 160, 250), "X": (150, 90, 210), "x": (96, 52, 150)},
        desc="Rabo de cavalo, caneta azul e cronograma em dia",
        padrao={"nuvem": "lilas", "bastao": "caneta", "roupa": "cam_amarela"}),
    "gabaritador": dict(
        nome="Gabaritador", artigo="o", preco=150, tipo="pe", cab=CAB_GABARITADOR,
        pal={"h": (28, 24, 32), "j": (52, 46, 60), "F": (240, 196, 158), "f": (204, 150, 116), "N": (36, 36, 56),
             "M": (180, 80, 90), "X": (60, 70, 90), "x": (36, 42, 56)},
        desc="Óculos de aro grosso e régua na mão: não erra uma",
        padrao={"nuvem": "branca", "bastao": "regua", "roupa": "cam_verde"}),
    "skatista": dict(
        nome="Skatista", artigo="o", preco=200, tipo="pe", cab=CAB_SKATISTA,
        pal={"h": (40, 28, 24), "j": (80, 56, 44), "F": (176, 118, 80), "f": (138, 88, 58), "N": (30, 20, 22),
             "M": (150, 60, 66), "P": (200, 120, 100), "C": (228, 60, 60), "c": (150, 30, 40),
             "X": (40, 40, 48), "x": (20, 20, 26)},
        desc="Boné para trás e marca-texto: estuda no intervalo da sessão",
        padrao={"nuvem": "menta", "bastao": "marcatexto", "roupa": "cam_preta"}),
    "blackpower": dict(
        nome="Black Power", artigo="a", preco=250, tipo="pe", cab=heroi.CABECAS["cachos"],
        pal={"h": (34, 22, 24), "j": (78, 54, 56), "F": (138, 90, 62), "f": (106, 66, 44), "N": (24, 14, 18),
             "M": (170, 60, 80), "P": (188, 104, 92), "X": (230, 70, 140), "x": (160, 40, 96)},
        desc="Black power, lapiseira de metal e redação nota mil",
        padrao={"nuvem": "pessego", "bastao": "lapiseira", "roupa": "cam_roxa"}),
}

ROUPAS = {
    "cam_azul": dict(nome="Camiseta azul", preco=0, desc="A camiseta do Vestibulando", cor=(70, 130, 220)),
    "cam_amarela": dict(nome="Camiseta amarela", preco=0, desc="A camiseta da Vestibulanda", cor=(250, 200, 60)),
    "cam_verde": dict(nome="Camiseta verde", preco=60, desc="Verde-bandeira (vem com o Gabaritador)", cor=(50, 170, 90)),
    "cam_preta": dict(nome="Camiseta preta", preco=60, desc="Básica (vem com o Skatista)", cor=(52, 50, 64)),
    "cam_roxa": dict(nome="Camiseta roxa", preco=60, desc="Roxo-uva (vem com a Black Power)", cor=(140, 80, 200)),
    "cam_vermelha": dict(nome="Camiseta vermelha", preco=60, desc="Para ser visto de longe no dia da prova",
                         cor=(220, 60, 60)),
    "moletom": dict(nome="Moletom cinza", preco=90, desc="Para o ar-condicionado gelado da sala de prova",
                    cor=(150, 154, 166)),
    "cam_laranja": dict(nome="Camiseta laranja", preco=120, desc="Cor de quem acorda cedo para estudar",
                        cor=(250, 140, 40)),
    "cam_branca": dict(nome="Camiseta branca", preco=120, desc="Limpa como gabarito sem rasura", cor=(236, 236, 242)),
}

# bastões médicos saem; material escolar entra (os mágicos ficam)
SAEM = ("esculapio", "bisturi", "bengala", "termometro", "estetoscopio", "seringa", "martelo", "lanterna")
BASTOES = {
    "lapis": dict(nome="Lápis gigante", preco=0, desc="Amarelo, apontado, com borracha (vem com o Vestibulando)"),
    "caneta": dict(nome="Caneta azul", preco=0, desc="Tinta azul, tampa e corpo transparente (vem com a Vestibulanda)"),
    "regua": dict(nome="Régua", preco=100, desc="30 centímetros de precisão (vem com o Gabaritador)"),
    "marcatexto": dict(nome="Marca-texto", preco=120, desc="Amarelo-neon para grifar o que cai (vem com o Skatista)"),
    "lapiseira": dict(nome="Lapiseira", preco=150, desc="Metal e grafite 0,7 (vem com a Black Power)"),
}
NUVENS_DESC = {
    "lilas": "A nuvem da Vestibulanda",
    "menta": "Fresca como a manhã do dia da prova (vem com o Skatista)",
    "fogo": "Para quem chega voando antes de o portão fechar",
    "celeste": "Azul-claro de céu limpo (vem com o Vestibulando)",
    "branca": "Nuvem de verdade (vem com o Gabaritador)",
    "pessego": "Laranja-rosado de fim de tarde (vem com a Black Power)",
    "neve": "Flocos brilhando, como a cabeça fria na hora da prova",
    "aurora": "Verde e violeta dançando no céu",
    "oceano": "Azul do mar com espuma",
    "floresta": "Verde-mata",
    "chumbo": "Azul-marinho da madrugada de revisão",
}
PAL_BASTAO = {"T": (240, 200, 150), "P": (250, 150, 170), "p": (200, 100, 120), "N": (40, 90, 210), "n": (20, 50, 140),
              "M": (250, 246, 60), "m": (200, 190, 20), "Z": (210, 214, 226)}


def _grade(tipo, h):
    g = [["."] * 8 for _ in range(h)]

    def haste(c1, c2, y0=0, y1=h):
        for y in range(y0, y1):
            g[y][2], g[y][3], g[y][4], g[y][5] = "K", c1, c2, "K"

    def topo(linhas, y0=0):
        for y, linha in enumerate(linhas):
            g[y0 + y] = list(linha)

    if tipo == "lapis":
        haste("Y", "y", 6, h - 7)
        for y in range(7, h - 7, 4):
            g[y][4] = "y"
        topo(("...KK...", "...KK...", "..KTTK..", "..KTTK..", "..KTTK..", "..KTTK.."))
        haste("s", "q", h - 7, h - 4)
        haste("P", "p", h - 4, h - 1)
        g[h - 1][2:6] = list("KKKK")
    elif tipo == "caneta":
        haste("Z", "w", 4, h - 9)
        for y in range(4, h - 9):
            g[y][3] = "N"                              # carga de tinta
        topo(("...KK...", "..KssK..", "..KssK..", "..KZwK.."))
        haste("N", "n", h - 9, h - 1)
        for y in range(h - 8, h - 3):
            g[y][6] = "N"                              # clipe da tampa
        g[h - 3][6] = "K"
        g[h - 1][2:6] = list("KKKK")
    elif tipo == "regua":
        for y in range(h):
            g[y][1], g[y][6] = "K", "K"
            for x in (2, 3, 4, 5):
                g[y][x] = "Y" if x < 5 else "y"
            if y % 2 == 0 and 0 < y < h - 1:
                g[y][2] = "K" if y % 10 == 2 else "y"  # marquinhas de centímetro
        g[0][1:7] = list("KKKKKK")
        g[h - 1][1:7] = list("KKKKKK")
    elif tipo == "marcatexto":
        for y in range(7, h):
            g[y][1], g[y][2], g[y][3], g[y][4], g[y][5], g[y][6] = "K", "M", "M", "m", "m", "K"
        topo(("...KK...", "..KMMK..", "..KMMK..", "..KmmK..", ".KKKKKK.", ".KZZwwK.", ".KZZwwK."))
        for y in range(h - 9, h - 2):
            g[y][1] = "K"
        g[h - 1][1:7] = list("KKKKKK")
    elif tipo == "lapiseira":
        haste("s", "q", 4, h)
        for y in range(h - 14, h - 4):
            g[y][3], g[y][4] = ("N", "n") if y % 2 else ("n", "n")   # empunhadura emborrachada
        topo(("...KK...", "...Kq...", "...Kq...", "..KZsK.."))
        g[0][3], g[0][4] = "K", "."
        g[h - 1][2:6] = list("KKKK")
    else:
        return None
    return ["".join(r) for r in g]


def ativar():
    """Troca o elenco de heroi.py pelo dos estudantes (chamado por edicao.ativar_vestibulando)."""
    if heroi.PADRAO == "vestibulando":
        return
    heroi.PERSONAGENS.clear()
    for pid, d in PERSONAGENS.items():
        heroi.CABECAS[pid] = d["cab"]
        heroi.CORPOS[pid] = CORPO
        heroi.CARAS[pid] = _caras(d["cab"]) if pid not in heroi.CARAS else heroi.CARAS[pid]
        dados = {k: v for k, v in d.items() if k != "cab"}
        dados["pal"] = {**PAL_BASE, **d["pal"]}
        heroi.PERSONAGENS[pid] = dados
    # a Vestibulanda e a Black Power reaproveitam as cabeças da Doutora e da Doutora Cachos
    heroi.CARAS["vestibulanda"] = heroi.CARAS["doutora"]
    heroi.CARAS["blackpower"] = heroi.CARAS["cachos"]
    heroi.ROUPAS.clear()
    heroi.ROUPAS.update(ROUPAS)
    for b in SAEM:
        heroi.BASTOES.pop(b, None)
    nenhum = heroi.BASTOES.pop("nenhum")
    resto = dict(heroi.BASTOES)
    heroi.BASTOES.clear()
    heroi.BASTOES.update({"nenhum": nenhum, **BASTOES, **resto})
    for n, txt in NUVENS_DESC.items():
        heroi.NUVENS[n]["desc"] = txt
    heroi.PAL_BASTAO.update(PAL_BASTAO)
    heroi.GRADES_EXTRA.append(_grade)
    heroi.PADRAO = "vestibulando"
    heroi.equipar({"personagem": "vestibulando"})
