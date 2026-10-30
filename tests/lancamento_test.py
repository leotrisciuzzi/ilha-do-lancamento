"""Teste headless da Ilha do Lançamento (edição de marketing, livro "A Fórmula do Lançamento").
    venv/bin/python tests/lancamento_test.py <pasta_saida>"""
import os, sys, random, importlib
os.environ["SDL_VIDEODRIVER"] = "dummy"; os.environ["SDL_AUDIODRIVER"] = "dummy"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pygame
from ilha import edicao, data
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
edicao.ativar_lancamento()
data.SAVE_DIR = OUT; data.SAVE_FILE = os.path.join(OUT, "save.json")
if os.path.exists(data.SAVE_FILE):
    os.remove(data.SAVE_FILE)
from ilha import ui, game, heroi, menus, lancamento as L
from tools.checar_pilulas import problemas_pilula

assert edicao.LANCAMENTO and edicao.STEAM and edicao.NOME == "Ilha do Lançamento"
assert heroi.PADRAO == "lancador" and set(heroi.PERSONAGENS) == {"lancador", "lancadora", "copywriter", "afiliado",
                                                                  "influencer"}
assert not {"esculapio", "bisturi", "estetoscopio", "seringa"} & set(heroi.BASTOES)
app = ui.App(mudo=True)
app.push(L.menu_lancamento(app))
assert isinstance(app.pilha[-1], L.MenuLancamento)


def quadros(n=3):
    for _ in range(n):
        app.pilha[-1].update(Inp()); app.pilha[-1].draw(app.tela)


class Inp:
    ap, held, atual = set(), set(), None
    def foi(s, a): return a in s.ap
    def seg(s, a): return a in s.held


def shot(nome, n=90):
    quadros(n)
    pygame.image.save(app.tela, os.path.join(OUT, f"{nome}.png"))


shot("0_menu")
rot = [i["label"] for i in app.pilha[-1].itens if i.get("label")]
assert [L.NOMES[t.chave] for t in L.MUNDOS] == [r for r in rot if r[:2] in ("1.", "2.", "3.", "4.", "5.", "6.")], rot
# nada médico no menu
texto = repr(app.pilha[-1].itens).lower()
for proibido in ("residente", "médic", "doutor", "clínica", "paciente"):
    assert proibido not in texto, proibido

rng = random.Random(4)
total = 0
for t in L.MUNDOS:
    C, T = t.C, t.T
    total += len(C.todas())
    erros = [(m["id"], pp["titulo"], e) for m in C.MODULOS for pp in m["aula"] for k, e in problemas_pilula(pp) if k == "erro"]
    assert not erros, erros
    assert all(pp.get("exemplo") for m in C.MODULOS for pp in m["aula"])
    assert all(len(q["alts"]) == 5 and q["coment"].startswith("Por quê:") for q in C.todas())
    destaca = [q["id"] for q in C.todas()
               if len(dict(q["alts"])[q["gab"]]) > 1.25 * max(len(x) for k, x in q["alts"] if k != q["gab"])]
    assert not destaca, destaca
    for h in T.HABILIDADES:
        for _ in range(300):
            q = T.questao(rng, h)
            txt = [x for _, x in q["alts"]]
            assert len(set(txt)) == len(txt) == 5 and q["gab"] in dict(q["alts"]), (t.chave, h, txt)
    # o mundo: estilo → modos → aprendizado → fase com briefing → quiz
    L.abrir_mundo(app, t); quadros(2)
    est = app.pilha[-1]; assert est.titulo == "Como quer jogar?"
    est.itens[0]["acao"](); shot(f"{t.chave}_1_modos", 30)
    assert [i["label"] for i in app.pilha[-1].itens][:3] == ["Modo Aprendizado", "Modo Treino", "Prova final"]
    menus.jogar_modulo(app, t, 0)
    b = app.pilha[-1]; assert isinstance(b, ui.Briefing); shot(f"{t.chave}_2_briefing", 5)
    app.pop(); b.iniciar()
    j = app.pilha[-1].jogo
    bicho = next(e for e in j.ents if isinstance(e, game.BichoQuestao)); j.abrir_quiz(bicho)
    qz = app.pilha[-1]; assert isinstance(qz, ui.Quiz)
    qz._responder(qz.gab); quadros(2); shot(f"{t.chave}_3_quiz", 2)
    app.registrar(qz.q, True); app.pop(); qz.cb(qz.escolha, True)
    menus.abrir_treino(app, t); menus.jogar_treino(app, t, next(iter(T.HABILIDADES)))
    assert isinstance(app.pilha[-1], ui.Briefing)
    menus.prova_tema(app, t); assert isinstance(app.pilha[-1], ui.Briefing)
    while len(app.pilha) > 1:
        app.pilha.pop()
    print(t.nome, "·", len(C.MODULOS), "módulos,", len(C.todas()), "perguntas,", len(T.HABILIDADES), "treinos")
app.pilha[-1].ao_voltar(); shot("9_menu_depois")
print("perguntas:", total)
print("OK")
