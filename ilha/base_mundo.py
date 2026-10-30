"""Peças comuns aos mundos do Internato · Clínica Médica 2 (asma, DPOC, ventilação mecânica).

Mesmo molde de ventilacao.py / farmaco_atb.py (alternativa certa escrita primeiro e embaralhada com semente
fixa = id) e de fa_treino.py (_montar, taxa_erro, fase), só que fatorado para os três mundos pequenos."""
import random


def q(enunciado, alts, coment):
    """alts[0] é a certa (embaralhada depois em Mundo.mod)."""
    return {"enunciado": enunciado, "alts": list(zip("ABCDE", alts)), "gab": "A", "coment": coment}


def p(titulo, ideia, pontos, na_prova, fonte, exemplo=None, fig=None):
    """Pílula no padrão didático (tools/checar_pilulas.py); `exemplo` = caso resolvido com números (opcional);
    `fig` = figura desenhada pelo jogo (ilha/figuras.py), mostrada no Briefing depois da ideia."""
    d = {"titulo": titulo, "ideia": ideia, "pontos": pontos, "na_prova": na_prova, "fonte": fonte}
    if exemplo:
        d["exemplo"] = exemplo
    if fig:
        d["fig"] = fig
    return d


def c(porque, outras=None, fixar=None):
    """Comentário em três partes: o mecanismo da certa, por que as tentadoras estão erradas e a frase para levar."""
    partes = ["Por quê: " + porque]
    if outras:
        partes.append("E as outras: " + outras)
    if fixar:
        partes.append("Para fixar: " + fixar)
    return "\n".join(partes)


def _embaralhar(qq):
    textos = [t for _, t in qq["alts"]]
    certo = textos["ABCDE".index(qq["gab"])]
    random.Random(qq["id"]).shuffle(textos)
    qq["alts"] = list(zip("ABCDE", textos))
    qq["gab"] = "ABCDE"[textos.index(certo)]


class Mundo:
    """Acumula os módulos de um mundo; o módulo do tema expõe MODULOS, POR_ID e todas()."""

    def __init__(self, pref, materia, assunto, origem="aula INTERNATO"):
        self.pref, self.materia, self.assunto, self.origem = pref, materia, assunto, origem
        self.modulos = []

    def mod(self, mid, nivel, titulo, aula, questoes):
        for i, qq in enumerate(questoes, 1):
            qq.update(id=f"{self.pref}-{mid}-{i}", materia=self.materia, subtema=titulo, assunto=self.assunto,
                      imgs=[], prev=0.5, origem=f"Nível {nivel} · {self.origem}")
            _embaralhar(qq)
        self.modulos.append({"id": mid, "nivel": nivel, "titulo": titulo, "aula": aula, "questoes": questoes})


# ------------------------------------------------------------------ treino (casos gerados)

def fmt(x, casas=0):
    return f"{x:.{casas}f}".replace(".", ",")


class Treino:
    """questao(rng, habil) a partir de um dicionário habilidade -> função(rng) que devolve
    (enunciado, certa, [erradas], comentário)."""

    def __init__(self, materia, prefixo, habilidades, funcoes):
        self.materia, self.prefixo, self.habilidades, self.funcoes = materia, prefixo, habilidades, funcoes

    def montar(self, rng, habil, enunciado, certa, erradas, coment):
        erradas = [e for e in dict.fromkeys(erradas) if e != certa]
        rng.shuffle(erradas)
        alts = [certa] + erradas[:4]
        rng.shuffle(alts)
        return {"id": f"{self.prefixo}:{habil}", "enunciado": enunciado, "alts": list(zip("ABCDE", alts)),
                "gab": "ABCDE"[alts.index(certa)], "coment": coment, "materia": self.materia, "subtema": "",
                "assunto": "", "imgs": [], "prev": 0.5, "origem": "caso gerado", "treino": True}

    def questao(self, rng, habil):
        return self.montar(rng, habil, *self.funcoes[habil](rng))

    def taxa_erro(self, save, habil):
        s = save.stat(f"{self.prefixo}:{habil}")
        if not s or s["c"] + s["e"] == 0:
            return None
        return s["e"] / (s["c"] + s["e"])

    def fase(self, save, habil=None, n=6, rng=None):
        rng = rng or random.Random()
        if habil:
            return [self.questao(rng, habil) for _ in range(n)]
        hs = list(self.habilidades)
        pesos = [1 + 3 * (self.taxa_erro(save, h) if self.taxa_erro(save, h) is not None else 0.5) for h in hs]
        return [self.questao(rng, rng.choices(hs, pesos)[0]) for _ in range(n)]


def num_alts(rng, certo, erros, casas=0, passo=None):
    """Alternativas numéricas: a certa + erros típicos + vizinhos, todas distintas depois de formatar."""
    vistos, out = {fmt(certo, casas)}, []
    for v in erros:
        t = fmt(v, casas)
        if t not in vistos:
            vistos.add(t)
            out.append(t)
    passo = passo or (1 if casas == 0 else 10 ** -casas * 5)
    k = 1
    while len(out) < 4:
        t = fmt(certo + passo * k * (1 if k % 2 else -1), casas)
        k += 1
        if t not in vistos:
            vistos.add(t)
            out.append(t)
    return fmt(certo, casas), out[:4]


def classificar(rng, tabela, pergunta, extras=(), coment=""):
    """Treino por tabela de regras: tabela = [(situação, resposta, porquê)]; sorteia uma linha, a certa é a resposta dela
    e as erradas são as outras respostas da tabela (+ extras plausíveis). Devolve a tupla de Treino.montar."""
    sit, certa, pq = rng.choice(tabela)
    outras = list(dict.fromkeys(r for _, r, _ in tabela if r != certa)) + [e for e in extras if e != certa]
    rng.shuffle(outras)
    return f"{sit}. {pergunta}", certa, outras[:4], (pq + (" " + coment if coment else "")).strip()


def caso_de_arvore(rng, arv, pergunta="Conduta:"):
    """Uma questão a partir de um fluxograma: o caso gerado para uma folha sorteada; as alternativas são as
    outras folhas da mesma árvore. Devolve (enunciado, certa, erradas, comentário) para Treino.montar."""
    from .fluxo_dados import laudo
    alvo = rng.choice(arv.alvos)
    c = arv.gerar(rng, alvo)
    cam, folha = arv.percorrer(c)
    dados = "; ".join(f"{k}: {v}" for k, v in c["mostrar"])
    erradas = [arv.nos[a].rotulo for a in arv.alvos if a != folha.id and arv.nos[a].rotulo != folha.rotulo]
    passos = " → ".join(arv.nos[nid].opcoes[i][0] for nid, i in cam)
    coment = f"{laudo(arv, cam, folha)} Caminho: {passos}. {folha.ensina}"
    return f"{c['texto']} {dados}. {pergunta}", folha.rotulo, erradas, coment


# ------------------------------------------------------------------ bancas (questões reais do banco)

def texto_q(qq):
    return qq["enunciado"] + " " + " ".join(t for _, t in qq["alts"])


def coletar_bancas(banco, grupos, eh_do_tema, grupo_de):
    """{grupo: [cópias]} como em hiperk_bancas.coletar: provas primeiro, deduplicado pelo texto, mesmo id do banco."""
    import re
    chave = lambda qq: re.sub(r"\W+", "", qq["enunciado"].lower())[:120]   # noqa: E731
    out = {g: [] for g, _, _ in grupos}
    vistos = set()
    for prova in banco.provas:
        for qq in prova["questoes"]:
            if eh_do_tema(qq):
                vistos.add(chave(qq))
                out["provas"].append(dict(qq, _prova=True))
    for qs in banco.listas.values():
        for lista in qs.values():
            for qq in lista:
                if not eh_do_tema(qq) or chave(qq) in vistos:
                    continue
                vistos.add(chave(qq))
                out[grupo_de(qq)].append(dict(qq))
    for lista in out.values():
        for qq in lista:
            qq.setdefault("origem", "banco de questões")
            if not qq["origem"] or qq["origem"] == "banco de questões":
                qq["origem"] = "banco de questões · " + (qq.get("assunto") or qq.get("subtema") or "")
    return out


def bancas_por_assunto(spec, forte=None):
    """Para os mundos da prova (nefro, HAS, hemato…): spec = [(chave, nome, desc, {subtemas banco de questões}, regex|None)].
    Entra a questão cujo subtema (ou, nas provas, o assunto) está num grupo, ou cujo enunciado casa `forte`.
    Devolve (GRUPOS, coletar)."""
    import re
    sub = lambda qq: qq.get("subtema") or qq.get("assunto") or ""      # noqa: E731
    todos = set().union(*(s for _, _, _, s, _ in spec))
    grupos = [("provas", "Provas reais", "Questões das provas, com banca e ano")] + [(k, n, d) for k, n, d, _, _ in spec]

    def eh(qq):
        return sub(qq) in todos or bool(forte and re.search(forte, qq["enunciado"], re.I))

    def grupo(qq):
        for k, _, _, s, rx in spec:
            if sub(qq) in s:
                return k
        for k, _, _, s, rx in spec:
            if rx and re.search(rx, texto_q(qq), re.I):
                return k
        return spec[0][0]

    return grupos, lambda banco: coletar_bancas(banco, grupos, eh, grupo)
