"""Ilha do Lançamento — Mundo 1: a Fórmula e a lista (capítulos 1 a 3 de "A Fórmula do Lançamento", Jeff Walker).

O que é o lançamento ao estilo da Fórmula, as fases da sequência e por que a lista de e-mails é o ativo central do
negócio: página de captura, oferta de adesão e lista responsiva. Texto do jogo escrito com palavras próprias, a partir
do livro; nenhum trecho copiado."""
from .lan_base import LIVRO, mundo
from .base_mundo import c, p, q

MATERIA = "Marketing"
_M = mundo("lfo", "A Fórmula e a lista")
F = LIVRO + ", caps. 1–3"

NIVEIS = {1: "O que é um lançamento", 2: "A lista", 3: "Conversão e convocação à ação"}

_M.mod("formula", 1, "A Fórmula em uma página", [
    p("Lançar é transformar a venda num evento",
      "A Fórmula troca o anúncio solto por uma sequência que cria expectativa. Quando o carrinho abre, o público já "
      "espera pela oferta, e por isso as vendas se concentram em poucos dias.",
      ["A sequência tem pré-pré-lançamento, pré-lançamento, lançamento e pós-lançamento, nessa ordem.",
       "No pré-lançamento se entrega conteúdo de valor antes de pedir qualquer compra.",
       "O lançamento abre o carrinho por um tempo limitado, e o fechamento cria escassez real.",
       "O mesmo processo serve para produto digital, serviço, curso presencial ou produto físico."],
      "Pegadinha: o lançamento não começa no dia de abrir o carrinho. Ele começa semanas antes, com aquecimento e "
      "conteúdo.",
      F,
      "Um professor de violão quer vender um curso. Em vez de anunciar e torcer, ele avisa a lista, publica três vídeos "
      "úteis em uma semana, abre as vendas por cinco dias e fecha com data marcada."),
    p("Dois tipos de negócio, um mesmo método",
      "O livro mostra que gente comum, sem grande estrutura, conseguiu vender muito em poucos dias. O motivo não é sorte: "
      "é ter uma lista que confia e uma sequência que leva essa lista até a oferta.",
      ["O Lançamento Interno é feito só para a sua lista, sem parceiros de fora.",
       "O Lançamento Conjunto usa parceiros que mandam o público deles para a sua sequência em troca de comissão.",
       "O Seed Launch é o lançamento-semente, para quem ainda não tem produto nem lista.",
       "Os três se alternam num ciclo em que cada lançamento deixa a lista maior para o seguinte."],
      "A pergunta pede o nome do lançamento feito só para a própria lista: Lançamento Interno.",
      F,
      "Uma nutricionista começa com um Seed Launch para 150 seguidores, cria o curso com as primeiras alunas, faz um "
      "Lançamento Interno para a lista que cresceu e depois um Lançamento Conjunto com parceiros."),
], [
    q("Qual é a ordem correta das fases da Fórmula do Lançamento?",
      ["pré-pré-lançamento, pré-lançamento, lançamento, pós-lançamento",
       "lançamento, pré-lançamento, pós-lançamento, pré-pré-lançamento",
       "pré-lançamento, pré-pré-lançamento, lançamento, pós-lançamento",
       "pós-lançamento, lançamento, pré-lançamento, pré-pré-lançamento",
       "pré-pré-lançamento, lançamento, pré-lançamento, pós-lançamento"],
      c("primeiro se aquece o mercado, depois se entrega conteúdo, aí se abre o carrinho e, por fim, se cuida dos "
        "clientes.",
        "as outras ordens abrem o carrinho antes do conteúdo ou aquecem depois de vender.",
        "aquece, entrega, vende, cuida.")),
    q("Qual a principal diferença entre um lançamento e um anúncio comum de venda?",
      ["o lançamento cria expectativa antes da oferta",
       "o lançamento usa sempre anúncios pagos",
       "o lançamento dispensa uma lista de e-mails",
       "o lançamento vende por tempo indeterminado",
       "o lançamento só serve para produtos digitais"],
      c("a sequência transforma a oferta num evento esperado; quando o carrinho abre, o público já quer comprar.",
        "anúncio pago é opcional; a lista é central; o carrinho fecha; o método vale para produto físico e serviço.",
        "lançamento = expectativa antes da oferta.")),
    q("O lançamento feito apenas para a sua própria lista, sem parceiros, chama-se:",
      ["Lançamento Interno",
       "Lançamento Conjunto",
       "Seed Launch",
       "Circle of Awesome",
       "Lançamento Pago"],
      c("é o lançamento clássico da Fórmula, feito para a lista que você já tem.",
        "o Conjunto usa parceiros; o Seed Launch é para quem não tem produto nem lista; o Circle of Awesome é o ciclo "
        "entre os três; lançamento pago não é termo do livro.",
        "Interno = só a sua lista.")),
    q("Para quem o Seed Launch é indicado, segundo o livro?",
      ["quem ainda não tem produto nem lista",
       "quem já tem uma lista de milhares de compradores",
       "quem quer vender só por anúncios pagos",
       "quem quer evitar qualquer contato com o público",
       "quem vende só produtos físicos em loja"],
      c("é um lançamento simplificado para testar a ideia, conseguir os primeiros clientes e criar o produto com eles.",
        "com lista grande se faz o Interno; o Seed não depende de anúncio pago; ele exige contato direto; vale para "
        "vários tipos de produto.",
        "sem produto e sem lista: Seed Launch.")),
    q("O que acontece com as vendas quando o carrinho fica aberto para sempre?",
      ["perdem o pico do fechamento, porque não há escassez",
       "aumentam, porque há mais tempo para comprar",
       "ficam iguais, porque o prazo não influencia",
       "concentram-se todas no primeiro dia",
       "dobram, porque o cliente decide com calma"],
      c("sem consequência por esperar, o cliente adia; o fechamento definitivo é o que gera o pico final.",
        "mais tempo não vira mais venda; o prazo influencia muito; o pico do primeiro dia existe, mas o do fechamento "
        "some.",
        "carrinho que não fecha não cria escassez.")),
])

_M.mod("lista", 2, "A lista é o ativo do negócio", [
    p("Página de captura e oferta de adesão",
      "A lista de e-mails é o ativo que permite lançar quando quiser. Para construí-la, a pessoa troca o e-mail por algo "
      "de valor, que o livro chama de suborno ético.",
      ["A página de captura tem uma única escolha: deixar o e-mail para receber o conteúdo ou sair da página.",
       "A oferta de adesão é o presente que convence o visitante a entrar na lista, como um vídeo, um guia ou uma aula.",
       "Não precisa acertar a página de primeira, porque ela se testa e melhora com o tempo.",
       "Comprar lista não funciona, porque a lista vale pela relação, não pelo número de endereços."],
      "A pergunta descreve uma página com formulário e nenhum outro link: é a página de captura.",
      F,
      "Uma personal trainer cria uma página com um único formulário: deixe o e-mail e receba o treino de 15 minutos para "
      "fazer em casa. Quem não quer o treino sai; quem quer, entra na lista dela."),
    p("Lista responsiva vale mais que lista grande",
      "O que importa é quantas pessoas leem e agem, não quantos endereços existem. Uma lista pequena que confia em você "
      "vende mais que uma enorme que ignora seus e-mails.",
      ["Uma lista de 100 pessoas com 60% de abertura tem 60 leitores, mais que uma de 1.000 com 1% de abertura.",
       "A lista fica responsiva quando você manda conteúdo útil com frequência, e não só ofertas.",
       "Cliente em potencial está na lista mas ainda não comprou, e cliente já comprou de você.",
       "A lista de lançamento é a que se forma durante o pré-lançamento, com quem se inscreveu nos vídeos."],
      "Pegadinha clássica: escolher a lista maior. Compare leitores, isto é, tamanho vezes taxa de abertura.",
      F,
      "Lista A: 5.000 contatos e 2% de abertura, 100 leitores. Lista B: 800 contatos e 40% de abertura, 320 leitores. "
      "A lista B vende mais, apesar de ser seis vezes menor."),
], [
    q("Uma página com um formulário de e-mail e nenhuma outra opção além de sair é:",
      ["a página de captura",
       "a página de vendas",
       "a página de pedidos",
       "o blog de lançamento",
       "a carta de vendas"],
      c("a página de captura só oferece cadastrar-se para receber algo ou sair.",
        "a de vendas apresenta a oferta; a de pedidos recebe o pagamento; o blog hospeda o conteúdo; a carta de vendas "
        "é o texto da oferta.",
        "um formulário, uma escolha: captura.")),
    q("O presente oferecido em troca do e-mail do visitante é chamado de:",
      ["oferta de adesão",
       "bônus de fechamento",
       "garantia incondicional",
       "convocação à ação",
       "conteúdo de lançamento pago"],
      c("a oferta de adesão é o suborno ético que leva a pessoa a entrar na lista.",
        "o bônus de fechamento faz parte da oferta de venda; a garantia protege a compra; a convocação à ação é o "
        "pedido; não se cobra pelo conteúdo de captura.",
        "e-mail em troca de valor = oferta de adesão.")),
    q("Qual lista tem mais leitores: 2.000 contatos com 3% de abertura ou 300 contatos com 50% de abertura?",
      ["a de 300 contatos, com 150 leitores",
       "a de 2.000 contatos, com 60 leitores",
       "as duas, com o mesmo número de leitores",
       "a de 2.000 contatos, porque é maior",
       "não dá para comparar sem saber o preço"],
      c("2.000 × 3% = 60 leitores; 300 × 50% = 150 leitores.",
        "a maior tem menos leitores; os números não são iguais; tamanho não é o que conta; a conta não depende do preço.",
        "leitores = tamanho × abertura.")),
    q("Por que comprar uma lista de e-mails não funciona?",
      ["a lista vale pela relação, e lista comprada não conhece você",
       "porque e-mails comprados sempre chegam mais rápido",
       "porque o livro recomenda só listas acima de 10 mil",
       "porque comprar lista é a forma mais barata de vender",
       "porque lista comprada abre mais que a construída"],
      c("o valor da lista está na confiança construída; desconhecidos não leem nem compram.",
        "as outras afirmações são falsas ou invertem o argumento do livro.",
        "lista é relação, não endereço.")),
    q("O que torna uma lista responsiva?",
      ["mandar conteúdo útil com frequência, não só ofertas",
       "mandar só ofertas, uma por dia, sem conteúdo",
       "escrever raramente para não incomodar o público",
       "aumentar a lista com contatos comprados",
       "trocar de assunto a cada e-mail enviado"],
      c("o hábito de receber valor faz a pessoa abrir os próximos e-mails.",
        "só oferta cansa; sumir esfria a relação; contato comprado não responde; mudar de assunto confunde.",
        "lista responsiva = valor frequente.")),
])

_M.mod("conversao", 3, "Conversão e convocação à ação", [
    p("Conversão: quando a pessoa age",
      "Conversão é o momento em que a pessoa faz o que você pediu, seja entrar na lista, comentar ou comprar. Medir a "
      "conversão em cada passo mostra onde o lançamento perde gente.",
      ["A taxa de conversão da página de captura é cadastros divididos por visitantes.",
       "A taxa de conversão de vendas é compras divididas pelo número de pessoas na lista de lançamento.",
       "Uma página de captura que converte o dobro faz o mesmo tráfego render o dobro de lista.",
       "Testar título, presente e formulário é o jeito de subir a conversão aos poucos."],
      "A pergunta dá visitantes e cadastros e pede a taxa: divida cadastros por visitantes.",
      F,
      "A página recebeu 2.000 visitas e 700 cadastros: conversão de 35%. Ao trocar o título, foram 900 cadastros com as "
      "mesmas 2.000 visitas: 45%, e a lista cresceu sem gastar mais com tráfego."),
    p("Toda mensagem termina com um pedido",
      "Convocação à ação é pedir um compromisso claro: comentar, clicar, se inscrever ou comprar. Quem não pede, não "
      "recebe, e cada pequeno sim prepara o sim da compra.",
      ["No fim de cada vídeo do pré-lançamento se pede um comentário ou uma pergunta.",
       "Os comentários criam o diálogo de lançamento, que revela objeções e o que mais interessa ao público.",
       "Na abertura do carrinho o pedido muda para comprar, com um link direto para a página de vendas.",
       "Um pedido de cada vez funciona melhor que vários pedidos na mesma mensagem."],
      "Pegadinha: conteúdo ótimo sem convocação à ação gera aplauso, não venda nem comentário.",
      F,
      "No fim do vídeo, o professor de violão pede: conte nos comentários qual música você sonha tocar. Em dois dias são "
      "400 respostas, e ele descobre que a maior dúvida é tocar com a mão pequena."),
], [
    q("A página teve 4.000 visitas e 1.200 cadastros. A taxa de conversão é:",
      ["30%",
       "12%",
       "40%",
       "3,3%",
       "33%"],
      c("1.200 ÷ 4.000 = 0,30 = 30%.",
        "12% e 40% confundem os números; 3,3% inverte a divisão; 33% arredonda errado.",
        "conversão = ações ÷ visitantes.")),
    q("Qual o papel da convocação à ação no fim de cada vídeo do pré-lançamento?",
      ["pedir um compromisso, como comentar ou perguntar",
       "anunciar o preço final do produto e o bônus",
       "encerrar a conversa com o público por ali",
       "pedir que a pessoa saia da lista de e-mails",
       "esconder a data do próximo vídeo do público"],
      c("o pedido de comentário cria o diálogo de lançamento e pequenos compromissos.",
        "preço vem só na abertura; a ideia é abrir conversa, não fechar; sair da lista e esconder a data vão contra o "
        "método.",
        "todo conteúdo termina com um pedido.")),
    q("O diálogo de lançamento serve principalmente para:",
      ["revelar as objeções e o que mais interessa ao público",
       "substituir a página de vendas no dia da abertura",
       "evitar que o público comente nos vídeos",
       "mostrar o preço antes do pré-lançamento",
       "comprar novos contatos para a lista"],
      c("os comentários mostram dúvidas, medos e desejos que você responde nos próximos conteúdos e na oferta.",
        "não substitui a página de vendas; o objetivo é estimular comentários; preço vem depois; não compra contatos.",
        "comentários = mapa das objeções.")),
    q("Com o mesmo tráfego, uma página de captura que passa de 20% para 40% de conversão:",
      ["dobra o número de cadastros",
       "reduz pela metade os cadastros",
       "não muda o número de cadastros",
       "aumenta os cadastros em 20 vezes",
       "exige o dobro de tráfego pago"],
      c("cadastros = visitantes × conversão; dobrar a taxa dobra a lista sem mais visitas.",
        "a lista não cai; muda sim; 20 vezes é erro de conta; não precisa de mais tráfego.",
        "melhorar conversão é tráfego de graça.")),
    q("Quantos pedidos uma mensagem de lançamento deve fazer, idealmente?",
      ["um pedido claro de cada vez",
       "cinco pedidos diferentes ao mesmo tempo",
       "nenhum, para não parecer vendedor",
       "três links diferentes no mesmo e-mail",
       "um pedido escondido no rodapé"],
      c("um pedido único e claro aumenta a chance de a pessoa agir.",
        "muitos pedidos dispersam; sem pedido não há ação; links demais confundem; escondido ninguém vê.",
        "uma mensagem, um pedido.")),
])

MODULOS = _M.modulos
ROTEIRO = [MODULOS[0]["aula"][0]]
POR_ID = {qq["id"]: qq for m in MODULOS for qq in m["questoes"]}


def todas():
    return [qq for m in MODULOS for qq in m["questoes"]]
