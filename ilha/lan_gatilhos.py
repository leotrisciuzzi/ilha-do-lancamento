"""Ilha do Lançamento — Mundo 2: vender sem empurrar (capítulos 4 e 5 de "A Fórmula do Lançamento", Jeff Walker).

A Sideways Sales Letter (a venda contada em capítulos, ao longo de vários conteúdos) e os estímulos mentais que o livro
usa: autoridade, reciprocidade, confiança, expectativa, simpatia, eventos e rituais, comunidade, escassez e prova
social. Texto do jogo escrito com palavras próprias, a partir do livro."""
from .lan_base import LIVRO, mundo
from .base_mundo import c, p, q

MATERIA = "Marketing"
_M = mundo("lgt", "Vender sem empurrar")
F = LIVRO + ", caps. 4–5"

NIVEIS = {1: "A venda em capítulos", 2: "Os estímulos mentais", 3: "Combinando os estímulos"}

_M.mod("sideways", 1, "A carta de vendas em capítulos", [
    p("Sideways Sales Letter: a venda em série",
      "Em vez de uma carta de vendas enorme lida de uma vez, a oferta é contada em capítulos, ao longo de dias. Cada "
      "capítulo entrega valor sozinho, e a soma prepara a compra sem parecer venda.",
      ["Cada conteúdo do pré-lançamento é um capítulo que se sustenta sozinho e termina apontando para o próximo.",
       "Como o público recebe valor antes de qualquer pedido, a venda acontece sem pressão de vendedor.",
       "O formato serial dá tempo para o público digerir a ideia e voltar a pensar nela.",
       "Os comentários entre os capítulos formam o diálogo de lançamento e ajustam a oferta."],
      "A pergunta descreve uma série de vídeos gratuitos que antecede a oferta: é a Sideways Sales Letter.",
      F,
      "Um consultor de finanças publica três vídeos em sete dias: por que sair das dívidas muda tudo, um método simples "
      "de orçamento e como seria a vida sem dívidas em um ano. No oitavo dia, abre o curso."),
    p("Venda é conversa, não empurrão",
      "O livro defende que ninguém gosta de ser vendido, mas todos gostam de comprar. A sequência deixa a pessoa chegar "
      "sozinha à decisão, e por isso a venda soa como ajuda.",
      ["Ensinar algo útil antes de vender mostra que o produto funciona.",
       "Responder às objeções nos conteúdos tira os medos antes do dia da oferta.",
       "O tom é de conversa com uma pessoa, não de anúncio para uma multidão.",
       "Vendedor inconveniente pressiona no primeiro contato, e o lançamento evita isso."],
      "Pegadinha: oferta logo no primeiro conteúdo quebra a sequência e soa como empurrão.",
      F,
      "Em vez de mandar um e-mail dizendo compre meu curso de pão caseiro, a padeira manda um vídeo ensinando a "
      "fermentação natural e pergunta qual pão a pessoa quer acertar. A venda vem dias depois."),
], [
    q("O que é a Sideways Sales Letter?",
      ["a venda contada em capítulos ao longo de vários conteúdos",
       "uma carta de vendas longa, lida de uma só vez",
       "um anúncio pago exibido várias vezes nas redes sociais",
       "a página onde o cliente digita os dados do cartão",
       "o e-mail de fechamento enviado no último dia"],
      c("é o processo serial: cada conteúdo é um capítulo de valor que prepara a oferta.",
        "a carta longa única é o oposto; anúncio pago é tráfego; a página do cartão é a de pedidos; o e-mail de "
        "fechamento é só uma peça.",
        "venda em série, capítulo a capítulo.")),
    q("Por que o lançamento parece menos com venda?",
      ["entrega valor antes de pedir a compra",
       "nunca menciona o produto em momento algum",
       "oferece desconto desde o primeiro contato",
       "esconde o preço até depois da compra",
       "usa só mensagens automáticas impessoais"],
      c("o público recebe conteúdo útil antes da oferta; quando ela chega, é continuação, não interrupção.",
        "o produto aparece sim, no fim; desconto imediato é empurrão; o preço é mostrado; o tom é pessoal.",
        "dar antes de pedir.")),
    q("Qual erro quebra a lógica da Sideways Sales Letter?",
      ["fazer a oferta já no primeiro conteúdo",
       "terminar cada vídeo apontando para o próximo",
       "responder às objeções ao longo da série",
       "pedir comentários no fim de cada conteúdo",
       "ensinar algo útil antes de vender"],
      c("a oferta antecipada transforma o primeiro capítulo em anúncio e derruba a confiança.",
        "as outras são justamente práticas recomendadas.",
        "a oferta vem no fim da série.")),
    q("Para que servem os comentários entre os capítulos?",
      ["formar o diálogo de lançamento e ajustar a oferta",
       "aumentar o preço a cada novo comentário recebido",
       "substituir a entrega do produto depois da compra",
       "dispensar o pré-pré-lançamento da sequência",
       "gerar escassez artificial no meio da série"],
      c("as respostas do público mostram objeções e desejos, que você usa nos próximos conteúdos e na oferta.",
        "o preço não sobe por comentário; o produto continua sendo entregue; o aquecimento continua; escassez vem do "
        "fechamento.",
        "comentários orientam a oferta.")),
    q("Qual a melhor forma de lidar com as objeções no lançamento?",
      ["responder às objeções dentro dos conteúdos, antes da oferta",
       "ignorar as objeções até o carrinho fechar de vez",
       "apagar os comentários que mostram dúvidas do público",
       "falar das objeções só depois que a compra foi feita",
       "dar um desconto novo sempre que surgir uma dúvida"],
      c("quando a dúvida é respondida antes, a pessoa chega à oferta sem o freio do medo.",
        "ignorar e apagar mantêm o freio; depois da compra é tarde; desconto não responde a dúvida.",
        "objeção respondida antes vira venda.")),
])

_M.mod("estimulos", 2, "Os estímulos mentais", [
    p("Autoridade, reciprocidade, confiança, simpatia",
      "Os estímulos mentais são atalhos que todo mundo usa para decidir. O livro mostra que um bom conteúdo de "
      "pré-lançamento aciona vários deles ao mesmo tempo, sem truque.",
      ["Autoridade: seguimos quem mostra domínio do assunto, e ensinar bem é a forma mais honesta de mostrar isso.",
       "Reciprocidade: quem recebe algo de valor sente vontade de retribuir.",
       "Confiança: cumprir o que se promete, como lançar o vídeo no dia anunciado, constrói confiança.",
       "Simpatia: compramos de quem gostamos, e contar a própria história aproxima."],
      "A pergunta descreve um conteúdo gratuito excelente e pergunta o estímulo: reciprocidade e autoridade juntas.",
      F,
      "Uma confeiteira ensina de graça o ponto exato da ganache. O público aprende, sente que ela sabe, isto é, "
      "autoridade, e quer retribuir, que é a reciprocidade."),
    p("Expectativa, evento, grupo, escassez e prova",
      "Os outros estímulos fazem a decisão acontecer numa data. A expectativa e o evento marcam o dia, a comunidade e a "
      "prova social mostram que outros estão indo, e a escassez faz agir antes do fim.",
      ["Expectativa é um pilar da Fórmula: anunciar o que vem e a data faz o público esperar pelo dia.",
       "Eventos e rituais transformam o lançamento num acontecimento, com data, contagem e abertura.",
       "Comunidade aparece quando o público conversa entre si nos comentários e se sente parte de um grupo.",
       "Escassez é um dos estímulos mais fortes: o que acaba é mais desejado, e ela precisa ser real."],
      "Pegadinha: escassez falsa, como prazo que nunca acaba, destrói a confiança e o próximo lançamento.",
      F,
      "O lançamento abre na segunda às 10 horas, com contagem regressiva: evento. A turma comenta junta: comunidade. "
      "Centenas de depoimentos: prova social. O bônus sai na quinta à meia-noite: escassez."),
], [
    q("Você entrega três vídeos gratuitos e muito úteis, e o público sente vontade de retribuir. Que estímulo é esse?",
      ["reciprocidade",
       "escassez",
       "autoridade",
       "comunidade",
       "expectativa"],
      c("receber valor gera a vontade de devolver: reciprocidade.",
        "escassez é o que acaba; autoridade é domínio do assunto; comunidade é o grupo; expectativa é aguardar a data.",
        "deu valor, gerou dívida simpática.")),
    q("O lançamento tem data de abertura, contagem regressiva e um horário marcado. Que estímulo principal?",
      ["eventos e rituais",
       "simpatia pelo autor",
       "reciprocidade",
       "prova social",
       "autoridade no assunto"],
      c("transformar a venda num acontecimento com data e ritual é o estímulo de eventos e rituais.",
        "simpatia é gostar da pessoa; reciprocidade é retribuir; prova social é ver os outros; autoridade é domínio.",
        "data marcada = evento.")),
    q("Qual estímulo o livro considera um dos mais poderosos, e que precisa ser real?",
      ["escassez",
       "simpatia",
       "comunidade",
       "confiança",
       "autoridade"],
      c("a escassez move a decisão, e a falsa destrói a confiança para os próximos lançamentos.",
        "os outros são importantes, mas o livro dá à escassez o destaque de mais poderoso.",
        "escassez real, sempre.")),
    q("Você lança o vídeo exatamente no dia e na hora que prometeu. Que estímulo está construindo?",
      ["confiança",
       "escassez",
       "prova social",
       "comunidade",
       "eventos e rituais"],
      c("promessa cumprida, mesmo pequena, constrói confiança.",
        "não há nada acabando; ninguém está sendo mostrado; não há grupo; o evento é o lançamento todo, não o "
        "cumprimento da promessa.",
        "cumprir o prometido = confiança.")),
    q("Os inscritos começam a conversar entre si e a se ajudar nos comentários. Que estímulo aparece?",
      ["comunidade",
       "autoridade",
       "escassez",
       "reciprocidade",
       "simpatia"],
      c("quando o público se sente parte de um grupo, o comportamento do grupo puxa a decisão de cada um.",
        "autoridade é de quem ensina; escassez é o que acaba; reciprocidade é retribuir; simpatia é gostar de você.",
        "grupo que conversa = comunidade.")),
])

_M.mod("combinar", 3, "Estímulos ao longo da sequência", [
    p("Cada fase acende estímulos diferentes",
      "Os estímulos não são usados um de cada vez. Eles se acumulam ao longo da sequência, e por isso o dia da abertura "
      "chega com todos acesos ao mesmo tempo.",
      ["No pré-lançamento o conteúdo gratuito acende reciprocidade e autoridade.",
       "Os comentários do pré-lançamento acendem comunidade e prova social.",
       "A data anunciada e a contagem acendem expectativa e evento.",
       "O fechamento do carrinho acende a escassez, que gera o pico final de vendas."],
      "A pergunta clássica: qual estímulo gera o pico do último dia? Escassez. O do primeiro dia vem da expectativa.",
      F,
      "Primeiro dia de carrinho aberto com muitas vendas: expectativa acumulada. Último dia com outro pico: o bônus e o "
      "preço especial vão acabar, isto é, escassez."),
    p("Ética: estímulo não é manipulação",
      "Os estímulos funcionam porque refletem como as pessoas decidem. Usados com produto bom e promessa verdadeira, "
      "ajudam a pessoa a agir; usados para enganar, destroem o negócio.",
      ["Escassez inventada ou prazo que reabre todo mês ensina o público a não acreditar em você.",
       "Depoimento falso fere a confiança e pode trazer problema legal.",
       "A melhor proteção é um produto que entrega o que promete e uma garantia clara.",
       "O livro trata a lista como relação de longo prazo, e por isso a honestidade é estratégia."],
      "Pegadinha: reabrir o carrinho logo depois do fechamento mata a escassez dos próximos lançamentos.",
      F,
      "Um vendedor fecha o carrinho na sexta e reabre na segunda com o mesmo preço. No lançamento seguinte, ninguém acredita "
      "no prazo, e o pico do último dia some."),
], [
    q("Qual estímulo explica o pico de vendas no último dia de carrinho aberto?",
      ["escassez",
       "reciprocidade",
       "autoridade",
       "simpatia",
       "confiança"],
      c("a consequência de perder o bônus ou o preço faz quem estava em dúvida agir.",
        "reciprocidade e autoridade se constroem antes; simpatia e confiança não explicam o pico final.",
        "último dia = escassez.")),
    q("Qual estímulo explica o pico de vendas no primeiro dia de carrinho aberto?",
      ["expectativa acumulada",
       "escassez do último dia",
       "prova social dos clientes antigos",
       "autoridade de um parceiro",
       "desconto escondido na página"],
      c("quem já esperava pela oferta compra assim que ela abre: é a expectativa construída no pré-lançamento.",
        "a escassez pesa no fim; clientes antigos e parceiros não explicam o primeiro dia; desconto escondido não é o "
        "motor.",
        "primeiro dia = expectativa.")),
    q("Um empreendedor fecha o carrinho e reabre dois dias depois, com o mesmo preço. O efeito no próximo lançamento é:",
      ["a escassez perde força, porque o público não acredita no prazo",
       "a escassez fica mais forte, porque o público aprendeu",
       "nada muda, porque cada lançamento é independente",
       "as vendas do primeiro dia aumentam muito",
       "a comunidade cresce mais rápido que antes"],
      c("o público aprende que o prazo não é real e espera a próxima reabertura.",
        "o efeito é o contrário; os lançamentos se ligam pela confiança; não há ganho no primeiro dia nem na comunidade.",
        "prazo falso destrói escassez futura.")),
    q("Conteúdo gratuito de alta qualidade no pré-lançamento aciona principalmente:",
      ["reciprocidade e autoridade",
       "escassez e eventos",
       "prova social e escassez",
       "comunidade e escassez",
       "simpatia e escassez"],
      c("dar valor gera retribuição, e ensinar bem mostra domínio.",
        "escassez vem do fechamento; eventos vêm da data; prova social e comunidade vêm dos comentários.",
        "conteúdo bom = reciprocidade + autoridade.")),
    q("Qual a melhor proteção contra a fama de manipulador num lançamento?",
      ["produto que entrega o prometido e garantia clara",
       "muitos depoimentos inventados na página",
       "prazos curtos que reabrem todo mês",
       "esconder o preço até o fim do vídeo",
       "não responder às perguntas do público"],
      c("promessa verdadeira e garantia tornam os estímulos honestos e mantêm a lista confiando.",
        "depoimento falso e prazo que reabre minam a confiança; esconder preço e ignorar perguntas afastam.",
        "estímulo honesto = produto bom + promessa cumprida.")),
])

MODULOS = _M.modulos
ROTEIRO = [MODULOS[1]["aula"][1]]
POR_ID = {qq["id"]: qq for m in MODULOS for qq in m["questoes"]}


def todas():
    return [qq for m in MODULOS for qq in m["questoes"]]
