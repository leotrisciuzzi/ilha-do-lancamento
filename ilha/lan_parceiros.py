"""Ilha do Lançamento — Mundo 5: começar do zero e crescer com parceiros (capítulos 9 e 10 de "A Fórmula do
Lançamento", Jeff Walker).

O Seed Launch (microlista, vender antes de criar, produto feito com os primeiros clientes) e o Lançamento Conjunto
(parceiros e associados, comissão, rastreamento, relações de longo prazo), além do ciclo que liga os lançamentos.
Texto do jogo escrito com palavras próprias, a partir do livro."""
from .lan_base import LIVRO, mundo
from .base_mundo import c, p, q

MATERIA = "Marketing"
_M = mundo("lsj", "Seed Launch e parceiros")
F9, F10 = LIVRO + ", cap. 9", LIVRO + ", cap. 10"

NIVEIS = {1: "Seed Launch", 2: "Lançamento Conjunto", 3: "O ciclo dos lançamentos"}

_M.mod("seed", 1, "Seed Launch: começar do zero", [
    p("Microlista e venda antes de criar",
      "Quem não tem lista nem produto começa pequeno: junta uma microlista e vende o produto antes de criá-lo. Assim o "
      "mercado paga para você descobrir o que ele quer.",
      ["A microlista pode ter 30 pessoas, mas o ideal fica entre 100 e 300.",
       "Ela nasce publicando conteúdo relevante sobre o tema nas redes sociais, de forma constante.",
       "Antes de criar, se pergunta à microlista o que ela mais quer aprender ou resolver.",
       "A oferta é feita antes de o produto existir, e quem compra recebe o produto feito em aulas ao vivo."],
      "A pergunta descreve alguém sem lista nem produto que quer começar: a resposta é o Seed Launch com microlista.",
      F9,
      "Uma fisioterapeuta posta dicas de postura por dois meses e junta 180 pessoas na lista. Pergunta qual a maior dor, "
      "ouve que é a lombar, vende um curso ao vivo de 4 semanas para 22 pessoas e grava as aulas."),
    p("O produto nasce com os primeiros clientes",
      "No Seed Launch o produto é entregue ao vivo, aula por aula, e moldado pelas perguntas dos alunos. Por isso o "
      "primeiro produto já sai do jeito que o mercado quer.",
      ["As aulas ao vivo, por transmissão ou videoconferência, viram o produto gravado depois.",
       "As perguntas dos primeiros alunos mostram o que falta e o que sobra no conteúdo.",
       "Os resultados desses alunos viram depoimentos para o próximo lançamento.",
       "O preço pode ser menor, porque o produto ainda está sendo construído com eles."],
      "Pegadinha: gastar meses criando o produto perfeito antes de vender. O Seed Launch vende primeiro.",
      F9,
      "Os 22 alunos da fisioterapeuta fazem as aulas ao vivo e pedem uma aula sobre trabalhar sentado. Ela inclui. O curso "
      "gravado já sai com isso e com 15 depoimentos para o próximo lançamento."),
], [
    q("Qual o tamanho ideal da microlista para um Seed Launch, segundo o livro?",
      ["entre 100 e 300 pessoas",
       "pelo menos 50 mil pessoas",
       "exatamente 10 pessoas",
       "mais de 1 milhão de seguidores",
       "não é preciso lista nenhuma"],
      c("dá para começar com 30, mas o ideal fica entre 100 e 300.",
        "50 mil e 1 milhão são para outros estágios; 10 é pouco; sem lista não há para quem vender.",
        "microlista: 100 a 300.")),
    q("No Seed Launch, quando o produto é criado?",
      ["depois da venda, com os primeiros clientes",
       "meses antes, sem falar com ninguém",
       "só depois do terceiro lançamento",
       "nunca, porque só se vende a ideia",
       "durante o pré-pré-lançamento, em segredo"],
      c("vende-se primeiro e cria-se o produto ao vivo com os compradores.",
        "criar antes arrisca fazer o que ninguém quer; o produto é criado no primeiro lançamento; ele precisa ser "
        "entregue; não é segredo.",
        "Seed: vende, depois cria com eles.")),
    q("Como a microlista costuma ser formada?",
      ["publicando conteúdo relevante nas redes sociais",
       "comprando contatos de uma empresa de dados",
       "mandando mensagens em massa para desconhecidos",
       "esperando que as pessoas descubram sozinhas",
       "pagando parceiros grandes desde o início"],
      c("conteúdo útil sobre o tema atrai seguidores que viram a microlista.",
        "comprar e spam não geram relação; esperar não constrói; parceiros grandes vêm depois.",
        "conteúdo atrai a microlista.")),
    q("Qual a vantagem de entregar o primeiro produto ao vivo?",
      ["moldar o conteúdo pelas perguntas dos alunos",
       "evitar qualquer contato com os clientes",
       "cobrar o dobro do preço normal",
       "dispensar depoimentos no futuro",
       "não precisar ensinar nada de verdade"],
      c("os alunos mostram o que falta, e o produto gravado sai mais certeiro.",
        "o ao vivo é contato direto; o preço tende a ser menor; ele gera depoimentos; ensinar é o centro.",
        "ao vivo = produto feito com o mercado.")),
    q("Para quem o Seed Launch é mais indicado?",
      ["quem está começando, sem lista nem produto",
       "quem tem lista grande e produto pronto",
       "quem só quer vender por anúncio pago",
       "quem quer evitar qualquer pesquisa com o público",
       "quem já tem dezenas de parceiros"],
      c("é o lançamento de começo de jornada, e também serve para testar uma ideia nova.",
        "com lista e produto se faz o Interno; não depende de anúncio; exige ouvir o público; parceiros são do Conjunto.",
        "começando do zero = Seed Launch.")),
])

_M.mod("conjunto", 2, "Lançamento Conjunto e parceiros", [
    p("Parceiros mandam público por comissão",
      "No Lançamento Conjunto, parceiros com listas próprias mandam o público deles para a sua sequência. Em troca, "
      "recebem comissão sobre as vendas que indicaram.",
      ["Associado e parceiro de empreendimento conjunto são quase a mesma coisa: os dois indicam em troca de comissão.",
       "Cada indicação é rastreada por um link próprio, para pagar a comissão ao parceiro certo.",
       "Em produto digital, comissões de cerca de 50% são comuns, como no primeiro lançamento do autor.",
       "Todos os indicados entram na sua lista de lançamento, que você mantém depois."],
      "A pergunta clássica: a maior vantagem do Lançamento Conjunto além das vendas? A lista cresce muito rápido.",
      F10,
      "Curso de R$ 997 com comissão de 50%. Um parceiro indica 30 vendas e recebe 30 × R$ 498,50, cerca de R$ 14.955. "
      "Além das vendas, os 2.000 inscritos que ele mandou ficam na lista do dono do curso."),
    p("Relação de longo prazo com parceiros",
      "Parceria boa é relação, não favor de uma vez só. O livro recomenda provar o lançamento antes de usar a lista dos "
      "parceiros e retribuir divulgando os lançamentos deles.",
      ["Não use a lista dos parceiros para testar: teste antes com a sua própria lista.",
       "Mostre números de um lançamento anterior para o parceiro saber que a sequência converte.",
       "Retribuir, divulgando o lançamento do parceiro, sustenta a relação.",
       "Concursos e premiações entre parceiros aumentam o empenho na divulgação."],
      "Pegadinha: estrear uma oferta nunca testada direto na lista de um parceiro grande. Isso queima a relação.",
      F10,
      "Antes de chamar parceiros, um professor faz um Lançamento Interno e converte 3% da lista. Com esse número em mãos, "
      "convida cinco parceiros, e depois divulga o curso de cada um para a lista dele."),
], [
    q("Qual a diferença entre associado e parceiro de empreendimento conjunto?",
      ["quase nenhuma: ambos indicam em troca de comissão",
       "o associado nunca recebe comissão",
       "o parceiro conjunto compra o produto antes",
       "o associado é sempre uma empresa grande",
       "o parceiro conjunto não usa link rastreado"],
      c("o livro trata os dois como quase sinônimos; parceiro conjunto sugere relação mais próxima.",
        "ambos recebem comissão; ninguém precisa comprar antes; tamanho não define; os dois usam rastreamento.",
        "associado ≈ parceiro conjunto.")),
    q("Curso de R$ 500 com comissão de 50%. Um parceiro indicou 20 vendas. Quanto ele recebe?",
      ["R$ 5.000",
       "R$ 10.000",
       "R$ 2.500",
       "R$ 500",
       "R$ 1.000"],
      c("20 vendas × R$ 500 × 50% = R$ 5.000.",
        "R$ 10.000 é o faturamento total; R$ 2.500 aplica 25%; R$ 500 e R$ 1.000 erram a conta.",
        "comissão = vendas × preço × %.")),
    q("Por que cada parceiro usa um link próprio no Lançamento Conjunto?",
      ["rastrear as indicações e pagar a comissão",
       "para impedir que o público consiga comprar",
       "para esconder do público o preço do produto",
       "para trocar o produto por outro",
       "para tirar os indicados da sua lista"],
      c("o rastreamento mostra de quem veio cada inscrito e cada venda.",
        "as outras opções não têm relação com o link de parceiro.",
        "link próprio = comissão justa.")),
    q("Além das vendas, qual o grande ganho do Lançamento Conjunto?",
      ["a lista cresce rápido e fica com você",
       "o preço do produto dobra sozinho no fim",
       "não é preciso mais pré-lançamento",
       "os parceiros passam a criar o produto",
       "os clientes deixam de pedir garantia"],
      c("os indicados entram na sua lista, e ela permanece depois do lançamento.",
        "preço não dobra; o pré-lançamento continua; os parceiros não criam o produto; a garantia continua.",
        "conjunto = lista cresce rápido.")),
    q("Qual o erro que o livro pede para evitar com parceiros?",
      ["testar uma oferta nova direto na lista do parceiro",
       "mostrar números de lançamentos anteriores",
       "retribuir divulgando o lançamento do parceiro",
       "rastrear as indicações com links próprios",
       "fazer concursos entre os parceiros"],
      c("a oferta deve ser provada antes na própria lista; queimar a lista do parceiro destrói a relação.",
        "as outras são boas práticas.",
        "teste na sua lista, não na dele.")),
])

_M.mod("ciclo", 3, "O ciclo que soma os lançamentos", [
    p("Seed, Interno e Conjunto em círculo",
      "Os três tipos de lançamento se alimentam. O Seed cria o produto e os primeiros clientes, o Interno prova a oferta "
      "na lista, e o Conjunto multiplica a lista com parceiros.",
      ["O Seed Launch testa a ideia e gera o produto e os primeiros depoimentos.",
       "O Lançamento Interno vende para a lista que cresceu e prova a conversão.",
       "O Lançamento Conjunto usa essa prova para atrair parceiros e aumentar a lista.",
       "A lista maior volta a alimentar o próximo Seed ou Interno, e o ciclo recomeça."],
      "A pergunta clássica: a ordem natural para quem começa do zero? Seed, depois Interno, depois Conjunto.",
      F10,
      "Ano 1: Seed com 200 pessoas e 20 alunos. Ano 1, mês 6: Interno para 1.500 pessoas, com depoimentos. Ano 2: "
      "Conjunto com 8 parceiros, e a lista passa de 10 mil."),
    p("O lançamento conjunto exige base",
      "Parceiros grandes só aceitam divulgar quem já mostrou que converte. Por isso o Conjunto vem depois de ter "
      "produto testado, números e depoimentos.",
      ["Sem lançamento anterior, é difícil convencer parceiros de que a oferta vende.",
       "Números de conversão e de faturamento por inscrito são o argumento para o parceiro.",
       "Depoimentos de alunos reais aumentam a confiança do parceiro e da lista dele.",
       "Relações com parceiros se constroem antes de precisar delas."],
      "Pegadinha: começar pelo Lançamento Conjunto sem nunca ter lançado. Falta prova para os parceiros.",
      F10,
      "Um parceiro pergunta quanto o lançamento fatura por inscrito. O empreendedor mostra: R$ 12 por inscrito no último "
      "Interno. Com 2.000 inscritos, o parceiro calcula cerca de R$ 24 mil em vendas e aceita."),
], [
    q("Para quem começa do zero, qual a ordem natural dos lançamentos?",
      ["Seed Launch, depois Lançamento Interno, depois Conjunto",
       "Lançamento Conjunto, depois Seed, depois Interno",
       "Interno, depois Conjunto, depois Seed",
       "só o Conjunto, repetido várias vezes",
       "só o Seed, sem nunca mudar"],
      c("o Seed cria produto e lista, o Interno prova a oferta e o Conjunto multiplica com parceiros.",
        "começar pelo Conjunto falta prova; as outras ordens invertem a lógica; repetir um só tipo não cresce igual.",
        "Seed → Interno → Conjunto.")),
    q("Qual o melhor argumento para convencer um parceiro a divulgar seu lançamento?",
      ["números de conversão de um lançamento anterior",
       "a promessa de que desta vez vai dar certo",
       "um vídeo bonito sem resultado medido",
       "o número de curtidas na sua página",
       "a opinião de um amigo próximo"],
      c("o parceiro quer saber quanto a lista dele vai render, e números reais mostram isso.",
        "promessa, vídeo sem números, curtidas e opinião não mostram conversão.",
        "parceiro decide por números.")),
    q("Um lançamento faturou R$ 15 por inscrito. Um parceiro vai mandar 3.000 inscritos. Vendas esperadas:",
      ["R$ 45.000",
       "R$ 4.500",
       "R$ 15.000",
       "R$ 3.000",
       "R$ 450.000"],
      c("3.000 × R$ 15 = R$ 45.000.",
        "as outras erram a multiplicação ou usam só um dos números.",
        "vendas ≈ inscritos × faturamento por inscrito.")),
    q("O que o Seed Launch entrega para o ciclo dos lançamentos?",
      ["o produto testado e os primeiros depoimentos",
       "a lista de parceiros grandes",
       "o fim da necessidade de pré-lançamento",
       "o preço final mais alto possível",
       "uma garantia sem prazo"],
      c("o Seed cria o produto com os primeiros clientes e gera prova social.",
        "parceiros vêm no Conjunto; o pré-lançamento continua; preço alto e garantia eterna não são o ponto.",
        "Seed = produto + primeiros depoimentos.")),
    q("Quando construir relações com parceiros, segundo o livro?",
      ["antes de precisar delas, com troca de ajuda",
       "só no dia em que o carrinho abre",
       "apenas depois de desistir do negócio",
       "nunca, porque parceiro é concorrente",
       "somente por contrato com multa"],
      c("relações de longo prazo se constroem com antecedência e reciprocidade.",
        "na abertura é tarde; desistir não faz sentido; o livro trata concorrentes como parceiros; contrato não "
        "substitui relação.",
        "parceria se planta antes.")),
])

MODULOS = _M.modulos
ROTEIRO = [MODULOS[2]["aula"][0]]
POR_ID = {qq["id"]: qq for m in MODULOS for qq in m["questoes"]}


def todas():
    return [qq for m in MODULOS for qq in m["questoes"]]
