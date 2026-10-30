"""Ilha do Lançamento — edição de marketing (o mesmo jogo, com mundos do livro "A Fórmula do Lançamento", de Jeff
Walker): seis mundos na ordem do livro, cada um com Aprendizado (módulos com aula antes da fase e comentário depois),
Treino (casos gerados na hora, com as contas do lançamento) e Prova final. Ativada por edicao.ativar_lancamento()."""
from . import edicao
from .menus import (Tema, abrir_aprendizado, abrir_treino, prova_tema, _dominadas, escolher_estilo, _estilo_item,
                    jogar_modulo, item_continuar)
from .ui import AMARELO, Menu, Mensagem, carteira_txt


def _tema(chave, nome, mod, paleta, cor, rot=(0, 0), extra=((1, 0), (2, 0))):
    return Tema(chave, nome, chave, mod, mod + "_treino", None, chave + "-treino", paleta, cor, "",
                lambda C: C.ROTEIRO, lambda C: C.ROTEIRO + [C.MODULOS[m]["aula"][a] for m, a in extra])


MUNDOS = [
    _tema("lfo", "A Fórmula e a lista", "lan_formula", 9, (120, 200, 255)),
    _tema("lgt", "Vender sem empurrar", "lan_gatilhos", 13, (255, 170, 210)),
    _tema("lpr", "O aquecimento e os três vídeos", "lan_pre", 4, (190, 160, 255)),
    _tema("lca", "A abertura do carrinho", "lan_carrinho", 6, (255, 200, 110)),
    _tema("lsj", "Seed Launch e parceiros", "lan_parceiros", 3, (140, 220, 140)),
    _tema("lng", "Do lançamento ao negócio", "lan_negocio", 12, (240, 140, 120)),
]
NOMES = {"lfo": "1. A Fórmula e a lista", "lgt": "2. Vender sem empurrar", "lpr": "3. O aquecimento e os três vídeos",
         "lca": "4. A abertura do carrinho", "lsj": "5. Seed Launch e parceiros", "lng": "6. Do lançamento ao negócio"}
DESC = {"lfo": "As fases do lançamento, página de captura, lista responsiva e conversão (caps. 1–3)",
        "lgt": "A venda em capítulos e os estímulos mentais: autoridade, reciprocidade, escassez… (caps. 4–5)",
        "lpr": "Pré-pré-lançamento e os PLCs: oportunidade, transformação e experiência da propriedade (caps. 6–7)",
        "lca": "E-mail de abertura, a oferta, os dois picos e o grande fechamento (cap. 8)",
        "lsj": "Microlista, vender antes de criar, afiliados, comissão e o ciclo dos lançamentos (caps. 9–10)",
        "lng": "Business Launch Formula, o negócio que você adora e os números do lançador (caps. 11–14)"}

AJUDA = """MOVER: setas / WASD ou direcional do controle (no celular, o personagem corre sozinho)
PULAR: Z ou Espaço (A no controle; no celular, toque) — segure no ar para planar
ATAQUE: X (golpe com o que estiver na mão) · PISÃO: ↓ no ar · PAUSA: Esc

BICHOS-QUESTÃO (placa ?): acerte para abrir a pergunta sobre o lançamento. Acertou: vira FLOR. Errou: ele te acerta e você cai numa bolha — pegue a bolha antes de a contagem zerar.
ANTES DE CADA FASE: a aula do módulo, com um caso resolvido. Leia — é o que a fase cobra.
SEM RISADINHA: ao abrir um mundo, escolha só as perguntas, uma atrás da outra, sem a fase.
TREINO: casos novos a cada vez, com as contas do lançamento (conversão, faturamento, comissão).
PONTOS (100): estrelas (30) + 5 fichas-coração (20) + acertos (50). Moedas compram personagens e itens na loja."""

CREDITOS = f"""Ilha do Lançamento · versão {edicao.VERSAO} · criado por {edicao.AUTOR}

Jogo de estudo baseado no livro "A Fórmula do Lançamento" (Launch), de Jeff Walker. As aulas, perguntas e casos foram escritos para este jogo, com palavras próprias, para quem já leu ou está lendo o livro; não substituem a leitura. Product Launch Formula, Seed Launch, Sideways Sales Letter e Business Launch Formula são marcas do autor.

Programação, arte em pixel e música: feitos para este jogo. Trilhas: composições originais e arranjos de obras em domínio público.

Feito com Python, pygame-ce (LGPL 2.1), SDL 2 (zlib), NumPy (BSD) e a fonte DejaVu."""


def _info(app, t):
    tot = len(t.C.todas())
    ok = sum(_dominadas(app, m) for m in t.C.MODULOS)
    return ok, tot


def abrir_mundo(app, t):
    escolher_estilo(app, NOMES[t.chave], lambda: _abrir_modos(app, t))


def _abrir_modos(app, t):
    menu = Menu(app, NOMES[t.chave], [], DESC[t.chave])

    def montar():
        ok, tot = _info(app, t)
        tr_c = tr_e = 0
        for h in t.T.HABILIDADES:
            s = app.save.stat(f"{t.treino_pref}:{h}") or {}
            tr_c, tr_e = tr_c + s.get("c", 0), tr_e + s.get("e", 0)
        tr = (f"{tr_c + tr_e} casos · {round(100 * tr_c / (tr_c + tr_e))}% de acerto" if tr_c + tr_e
              else "nenhum caso ainda")
        menu.itens = [
            {"label": "Modo Aprendizado", "cor": (120, 210, 255), "acao": lambda: abrir_aprendizado(app, t),
             "info": f"{len(t.C.MODULOS)} módulos com aula antes e comentário depois · {ok}/{tot} dominadas"},
            {"label": "Modo Treino", "cor": (140, 230, 140), "acao": lambda: abrir_treino(app, t),
             "info": f"Casos gerados na hora, infinitos · {tr}"},
            {"label": "Prova final", "cor": (200, 160, 250), "acao": lambda: prova_tema(app, t),
             "info": "10 perguntas de todos os módulos, erros e inéditas primeiro"},
            _estilo_item(app, t, abrir_mundo),
            {"label": "Voltar", "cor": (180, 180, 180), "acao": app.pop}]

    menu.ao_voltar = montar
    montar()
    app.push(menu)


def _proximo(app):
    for t in MUNDOS:
        for k, m in enumerate(t.C.MODULOS):
            if _dominadas(app, m) < len(m["questoes"]):
                jogar_modulo(app, t, k)
                return
    app.push(Mensagem(app, "Tudo dominado", "Você dominou todos os módulos. Vá para o Treino de cada mundo."))


def _barra(app):
    tot = sum(len(t.C.todas()) for t in MUNDOS)
    ok = sum(_dominadas(app, m) for t in MUNDOS for m in t.C.MODULOS)
    return {"frac": ok / tot, "vistas": sum(1 for t in MUNDOS for q in t.C.todas() if app.save.stat(q["id"])) / tot,
            "texto": f"O livro: {ok}/{tot} perguntas dominadas" if ok < tot else "O livro inteiro dominado!"}


def _opcoes(app):
    import pygame
    menu = Menu(app, "Opções", [], "")

    def som():
        app.save.config["mudo"] = app.audio.alternar_mudo()
        app.save.salvar()

    def montar():
        menu.itens = []
        if not edicao.ANDROID:
            cheia = pygame.display.is_fullscreen()
            menu.itens.append({"label": f"Tela cheia: {'ligada' if cheia else 'desligada'}", "info": "Também no F11",
                               "cor": (120, 210, 255), "acao": lambda: (app.alternar_tela_cheia(), montar())})
        js = app.pad.conectados()
        menu.itens += [
            {"label": f"Som: {'desligado' if app.audio.mudo else 'ligado'}", "info": "Música e efeitos",
             "cor": (140, 230, 140), "acao": lambda: (som(), montar())},
            {"label": "Controle", "cor": (160, 160, 200), "acao": app.configurar_controle,
             "info": f"Conectado: {js[0].get_name().strip()} · remapear" if js else "Nenhum controle conectado"},
            {"label": "Voltar", "cor": (180, 180, 180), "acao": app.pop}]

    menu.ao_voltar = montar
    montar()
    app.push(menu)


class MenuLancamento(Menu):
    def __init__(self, app):
        super().__init__(app, "Ilha do Lançamento", [], "")
        self._montar()

    def _montar(self):
        app = self.app
        from .personagens import abrir_escolha
        self.subtitulo = carteira_txt(app.save)
        self.barra = _barra(app)
        self.itens = []
        cont = item_continuar(app, MUNDOS)
        if cont:
            self.itens.append(cont)
        self.itens += [
            {"label": "▶ Estudar o que falta", "cor": AMARELO, "acao": lambda: _proximo(app),
             "info": "Abre o primeiro módulo, na ordem do livro, com pergunta ainda não dominada"},
            {"secao": "Os mundos do livro", "label": ""}]
        for t in MUNDOS:
            ok, tot = _info(app, t)
            self.itens.append({"label": NOMES[t.chave], "cor": t.cor, "acao": (lambda t=t: abrir_mundo(app, t)),
                               "info": DESC[t.chave], "dir": f"{ok}/{tot}", "prog": ok / tot if tot else 0})
        self.itens += [
            {"secao": "Seu lançador e ajustes", "label": ""},
            {"label": "Personagem e loja", "cor": (255, 170, 210), "acao": lambda: abrir_escolha(app),
             "info": "Trocar de personagem e comprar nuvens, itens e roupas com moedas"},
            {"label": "Como jogar", "cor": (255, 255, 255), "info": "Controles e regras",
             "acao": lambda: app.push(Mensagem(app, "Como jogar", AJUDA))},
            {"label": "Opções", "cor": (160, 160, 200), "info": "Tela cheia, som e controle", "acao": lambda: _opcoes(app)},
            {"label": "Créditos", "cor": (255, 220, 100), "info": f"Versão {edicao.VERSAO}",
             "acao": lambda: app.push(Mensagem(app, "Créditos", CREDITOS))}]
        if not edicao.ANDROID:
            self.itens.append({"label": "Sair", "cor": (180, 180, 180), "acao": lambda: setattr(app, "rodando", False)})
        self.sel = min(self.sel, len(self.itens) - 1)
        self._pular_desab(1)

    def ao_voltar(self):
        self._montar()

    def evento(self, e, inp):
        if inp.foi("voltar"):
            if edicao.ANDROID:          # padrão do Android: voltar duas vezes (em 2 s) sai do jogo
                import pygame
                agora = pygame.time.get_ticks()
                if agora - getattr(self, "_voltar_t", -10000) < 2000:
                    self.app.save.salvar()
                    self.app.rodando = False
                else:
                    self._voltar_t = agora
                    self.app.toast("Toque em voltar de novo para sair")
            return
        super().evento(e, inp)


def menu_lancamento(app):
    return MenuLancamento(app)
