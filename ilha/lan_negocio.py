"""Ilha do Lançamento — Mundo 6: do lançamento ao negócio (capítulos 11 a 14 de "A Fórmula do Lançamento", Jeff
Walker).

A Business Launch Formula (lançamentos em sequência construindo um negócio inteiro), conteúdo de alta qualidade em todo
lançamento, o negócio que você adora (o grande porquê, os clientes que você quer, mente mestra, aprendizado contínuo,
parcerias, toque humano) e o primeiro passo. Texto do jogo escrito com palavras próprias, a partir do livro."""
from .lan_base import LIVRO, mundo
from .base_mundo import c, p, q

MATERIA = "Marketing"
_M = mundo("lng", "Do lançamento ao negócio")
F11, F12 = LIVRO + ", cap. 11", LIVRO + ", caps. 12–14"

NIVEIS = {1: "Business Launch Formula", 2: "Um negócio que você adora", 3: "Sua vez de lançar"}

_M.mod("blf", 1, "Lançamentos que constroem um negócio", [
    p("Um lançamento depois do outro",
      "Um lançamento sozinho é um bom mês. Lançamentos em sequência, cada um maior que o anterior, constroem um negócio "
      "inteiro, e é isso que o livro chama de Business Launch Formula.",
      ["Cada lançamento deixa lista maior, mais depoimentos e mais autoridade no mercado.",
       "Os produtos novos podem ser lançados para a mesma lista, ampliando o que você oferece.",
       "O lançamento não serve só para produto: serve para evento, serviço, assinatura e até negócio físico.",
       "Todo lançamento deve trazer conteúdo de pré-lançamento de alta qualidade, sem exceção."],
      "A pergunta clássica: o primeiro princípio da Business Launch Formula? Sempre oferecer conteúdo de alta qualidade.",
      F11,
      "Um adestrador começa com um curso de comandos básicos. Seis meses depois lança um de filhotes, depois um evento "
      "presencial e depois uma assinatura mensal. Cada lançamento cresce a lista para o seguinte."),
    p("Lançar não é só para produto digital",
      "O processo de criar expectativa, entregar valor e abrir uma oferta com prazo funciona para quase tudo que se vende. "
      "Por isso o livro mostra casos de jogo de tabuleiro, eventos e serviços.",
      ["Um produto físico pode ser lançado em pré-venda com a mesma sequência de conteúdos.",
       "Um evento presencial pode usar os conteúdos para encher as vagas antes da data.",
       "Uma assinatura pode abrir turmas em lançamentos, e não ficar aberta o tempo todo.",
       "Serviços de alto valor podem lançar vagas limitadas de atendimento."],
      "Pegadinha: achar que a Fórmula só serve para curso on-line. O primeiro caso do livro é um jogo de tabuleiro.",
      F11,
      "Um casal tem um estoque de jogos de tabuleiro parado. Com uma lista pequena, três conteúdos sobre o tema do jogo "
      "e cinco dias de oferta, vende o estoque e paga o empréstimo."),
], [
    q("O que é a Business Launch Formula, em uma frase?",
      ["construir o negócio com lançamentos em série",
       "fazer um único lançamento enorme e depois parar",
       "vender só por anúncios, sem lançamento",
       "abrir o carrinho sem prazo de fechamento",
       "trocar o pré-lançamento por descontos"],
      c("lançamentos sucessivos, cada um aproveitando o anterior, formam o negócio.",
        "um único lançamento é um evento; anúncio sem lançamento, carrinho sem prazo e desconto no lugar de conteúdo "
        "fogem do método.",
        "negócio = lançamentos em série.")),
    q("Qual o primeiro princípio que o livro destaca para a Business Launch Formula?",
      ["sempre entregar conteúdo de alta qualidade",
       "sempre cobrar o menor preço de todo o mercado",
       "nunca usar garantia nos produtos",
       "lançar o mais raramente possível",
       "esconder o nome de quem vende"],
      c("o valor entregue antes da oferta é o que sustenta a confiança em todos os lançamentos.",
        "preço baixo não é princípio; garantia é recomendada; a frequência vem da sequência; o toque humano pede "
        "mostrar quem vende.",
        "todo lançamento entrega valor antes.")),
    q("A Fórmula do Lançamento serve para vender produtos físicos?",
      ["sim, o primeiro caso do livro é um jogo de tabuleiro",
       "não, só serve para cursos on-line",
       "não, só serve para serviços de consultoria",
       "sim, mas só com anúncios na televisão",
       "não, produto físico não pode ter pré-lançamento"],
      c("a sequência de expectativa, valor e oferta com prazo funciona para produto físico também.",
        "o livro mostra casos fora do digital; televisão não é exigida; produto físico pode ter pré-lançamento.",
        "a Fórmula vale além do digital.")),
    q("Uma assinatura mensal pode usar lançamentos?",
      ["sim, abrindo turmas em lançamentos com prazo",
       "não, assinatura precisa ficar aberta sempre",
       "não, assinatura não tem pré-lançamento",
       "sim, mas só sem garantia",
       "sim, mas só para quem já cancelou"],
      c("abrir a assinatura em janelas cria evento e escassez.",
        "ficar sempre aberta perde a escassez; ela pode ter pré-lançamento; garantia e ex-clientes não são condição.",
        "assinatura também abre por turmas.")),
    q("O que cada lançamento deixa para o seguinte?",
      ["lista maior, depoimentos e autoridade",
       "a obrigação de baixar o preço",
       "o fim da necessidade de conteúdo",
       "uma lista menor e mais cansada",
       "o fechamento definitivo do negócio"],
      c("lançamento bem feito acumula lista, prova social e reputação.",
        "não obriga a baixar preço; conteúdo continua necessário; lista bem cuidada cresce; o negócio continua.",
        "cada lançamento aduba o próximo.")),
])

_M.mod("adorar", 2, "Um negócio que você adora", [
    p("O grande porquê e os clientes que você quer",
      "Antes de escolher o que vender, o livro pede para definir por que você quer esse negócio. O porquê guia as "
      "escolhas difíceis e decide que clientes você atrai.",
      ["O grande porquê pode ser liberdade, família, propósito ou dinheiro, e precisa estar claro para você.",
       "Seu marketing atrai o tipo de cliente que você quer ou o que você não quer, por isso escolha a mensagem.",
       "Olhar além das curvas é planejar o próximo passo enquanto executa o atual.",
       "Custo de oportunidade: escolher a oportunidade errada custa meses ou anos."],
      "A pergunta clássica: o primeiro passo para um negócio que você adora? Definir o grande porquê.",
      F12,
      "Uma confeiteira quer tempo com os filhos. Esse porquê a faz escolher cursos gravados com lançamentos duas vezes por "
      "ano, em vez de encomendas diárias que tomariam todas as noites."),
    p("Mente mestra, aprendizado e toque humano",
      "Ninguém constrói um negócio sozinho. O livro defende grupos de apoio, aprendizado contínuo, parceiros em vez de "
      "concorrentes e o jeito pessoal de falar com o público.",
      ["Mente mestra é um grupo de pessoas que se ajudam com ideias e cobrança, ideia de Napoleon Hill.",
       "Ser um eterno aprendiz é necessário porque mercado, clientes e concorrentes mudam o tempo todo.",
       "Em vez de concorrentes, o livro fala em parceiros, porque relações abrem portas para lançamentos conjuntos.",
       "O toque humano vende mais: falar como pessoa, sem fingir ser uma grande empresa."],
      "Pegadinha: tratar todos do mercado como inimigos. O livro trata como possíveis parceiros.",
      F12,
      "Quatro empreendedores de nichos diferentes se reúnem a cada quinze dias por vídeo. Trocam números de lançamento, "
      "revisam páginas uns dos outros e divulgam os lançamentos entre si."),
], [
    q("Qual o primeiro passo para criar um negócio que você adora, segundo o livro?",
      ["definir o grande porquê do negócio",
       "escolher o logotipo e as cores da marca",
       "comprar a maior lista de e-mails possível",
       "copiar exatamente o negócio de outra pessoa",
       "abrir o carrinho antes de pensar no público"],
      c("o porquê orienta as escolhas e o tipo de negócio que vale a pena construir.",
        "marca vem depois; lista comprada não serve; copiar ignora suas regras; abrir sem público não funciona.",
        "comece pelo porquê.")),
    q("O que é uma mente mestra?",
      ["um grupo de pessoas que se ajudam com ideias e cobrança",
       "um software que escreve os e-mails do lançamento",
       "o parceiro que recebe a maior comissão",
       "o cliente que mais compra seus produtos",
       "a página de captura com maior conversão"],
      c("é o grupo de apoio mútuo descrito por Napoleon Hill e usado pelo autor.",
        "não é software, parceiro, cliente nem página.",
        "mente mestra = grupo de apoio.")),
    q("Como o livro sugere enxergar os concorrentes?",
      ["como possíveis parceiros",
       "como inimigos a derrotar",
       "como gente a ignorar sempre",
       "como compradores obrigatórios",
       "como ameaça que impede lançar"],
      c("relações no mercado geram parcerias e lançamentos conjuntos.",
        "inimizade e ignorar fecham portas; concorrente não é comprador; não impedem lançar.",
        "concorrente pode ser parceiro.")),
    q("O que é o toque humano no negócio?",
      ["falar como pessoa, sem fingir ser corporação",
       "atender só por mensagens automáticas",
       "esconder quem está por trás do produto",
       "usar linguagem formal de contrato",
       "evitar qualquer contato com os clientes"],
      c("ser você mesmo aproxima e vende mais.",
        "automação total, anonimato, juridiquês e distância afastam.",
        "gente compra de gente.")),
    q("Por que ser um eterno aprendiz é necessário nos negócios?",
      ["mercado, clientes e concorrentes mudam o tempo todo",
       "porque estudar substitui lançar",
       "porque o primeiro lançamento é sempre perfeito",
       "porque as regras de venda nunca mudam",
       "porque aprender dispensa ouvir o cliente"],
      c("quem para de aprender fica para trás num mercado que muda.",
        "estudar não substitui agir; lançamentos se aprimoram; as táticas mudam; ouvir o cliente é parte do aprendizado.",
        "o mercado anda: aprenda sempre.")),
])

_M.mod("sua_vez", 3, "Sua vez de lançar", [
    p("Comece pequeno, mas comece",
      "O livro termina com um chamado à ação: o primeiro lançamento não precisa ser perfeito nem grande. Ele precisa "
      "acontecer, porque é lançando que se aprende a lançar.",
      ["Escolha um tema que você domina e um público que você quer ajudar.",
       "Comece a lista hoje com conteúdo útil e uma oferta de adesão simples.",
       "Faça um Seed Launch para conseguir os primeiros clientes e o primeiro produto.",
       "Meça cada passo: cadastros, comentários, vendas, e melhore no próximo."],
      "A pergunta clássica: o que fazer depois de ler o livro? Lançar algo pequeno agora, não esperar a perfeição.",
      F12,
      "Um professor de xadrez decide começar: posta uma dica por dia, junta 120 pessoas, faz um Seed Launch de quatro "
      "aulas ao vivo e vende 14 vagas. O segundo lançamento já tem depoimentos."),
    p("Os números que o lançador acompanha",
      "Quem mede sabe onde melhorar. Os números principais seguem o caminho da pessoa: visita, cadastro, conteúdo, oferta "
      "e compra.",
      ["Conversão da página de captura mostra se a oferta de adesão atrai.",
       "Comentários e visualizações dos conteúdos mostram se o pré-lançamento engaja.",
       "Conversão da lista de lançamento em vendas mostra se a oferta convence.",
       "Faturamento por inscrito resume o lançamento e serve de argumento para parceiros."],
      "Pegadinha: medir só o faturamento. Sem os números do caminho, não se sabe o que corrigir.",
      F12,
      "Lançamento com 2.000 inscritos e R$ 30 mil de faturamento: R$ 15 por inscrito. Os comentários caíram no PLC nº 2, "
      "então o próximo lançamento reforça esse vídeo."),
], [
    q("Depois de ler o livro, qual o conselho do autor?",
      ["lançar algo pequeno agora, sem esperar",
       "esperar até ter uma lista de 100 mil pessoas",
       "criar o produto perfeito por dois anos",
       "estudar mais dez livros antes de agir",
       "lançar só quando tiver parceiros grandes"],
      c("lançando se aprende a lançar; o pequeno feito agora ensina mais que o grande adiado.",
        "lista enorme, produto perfeito, estudo infinito e parceiros grandes adiam o começo.",
        "comece pequeno, mas comece.")),
    q("Lançamento com 4.000 inscritos e R$ 60.000 de faturamento. Faturamento por inscrito:",
      ["R$ 15",
       "R$ 1,50",
       "R$ 150",
       "R$ 240",
       "R$ 6"],
      c("R$ 60.000 ÷ 4.000 = R$ 15 por inscrito.",
        "as outras erram a divisão.",
        "faturamento ÷ inscritos.")),
    q("Os comentários caíram muito no PLC nº 2. O que isso indica?",
      ["o PLC nº 2 precisa ser reforçado da próxima vez",
       "o produto deve ser abandonado de vez agora",
       "o carrinho deve abrir sem o PLC nº 3",
       "a página de captura está perfeita",
       "os parceiros pagaram comissão errada"],
      c("a queda mostra onde o público perdeu o interesse; é ali que se melhora.",
        "abandonar é exagero; pular o PLC nº 3 piora; a captura é outro número; comissão não tem relação.",
        "o número aponta o passo fraco.")),
    q("Qual número mostra se a oferta de adesão está atraindo?",
      ["a conversão da página de captura",
       "o faturamento do último dia",
       "a comissão dos parceiros",
       "a taxa de reembolso da garantia",
       "o número de dias de carrinho aberto"],
      c("cadastros ÷ visitas mostra se o presente oferecido convence.",
        "último dia, comissão e reembolso medem outras etapas; dias abertos não medem adesão.",
        "adesão = conversão da captura.")),
    q("Por que medir só o faturamento é um erro?",
      ["não mostra em que etapa o lançamento perdeu gente",
       "porque o faturamento nunca importa",
       "porque é proibido saber quanto se vendeu",
       "porque o faturamento é sempre igual",
       "porque só os parceiros podem medir"],
      c("sem os números do caminho, não se sabe se o problema foi captura, conteúdo ou oferta.",
        "faturamento importa, mas não basta; não é proibido nem fixo; quem lança deve medir.",
        "meça o caminho, não só o fim.")),
])

MODULOS = _M.modulos
ROTEIRO = [MODULOS[2]["aula"][1]]
POR_ID = {qq["id"]: qq for m in MODULOS for qq in m["questoes"]}


def todas():
    return [qq for m in MODULOS for qq in m["questoes"]]
