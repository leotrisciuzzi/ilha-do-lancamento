"""Ilha do Lançamento — Mundo 4: a abertura do carrinho (capítulo 8 de "A Fórmula do Lançamento", Jeff Walker).

O dia da abertura, a oferta (produto, bônus, preço, condições e garantia), os dias de carrinho aberto, os dois picos de
vendas e o grande fechamento com escassez real; o que fazer quando ninguém compra e depois do lançamento. Texto do jogo
escrito com palavras próprias, a partir do livro."""
from .lan_base import LIVRO, mundo
from .base_mundo import c, p, q

MATERIA = "Marketing"
_M = mundo("lca", "A abertura do carrinho")
F = LIVRO + ", cap. 8"

NIVEIS = {1: "O dia da abertura", 2: "Carrinho aberto e fechamento", 3: "Quando dá errado e depois"}

_M.mod("abertura", 1, "Abrir o carrinho", [
    p("O e-mail de abertura é curto",
      "No dia da abertura o trabalho de convencer já foi feito pelos conteúdos. Por isso o e-mail de abertura é curto: "
      "avisa que abriu e manda o link da página de vendas.",
      ["Abertura do carrinho é o momento em que você começa a aceitar pedidos.",
       "O e-mail tem poucas frases e um link claro para a página de vendas.",
       "O P.S. é a parte mais lida do e-mail e é um bom lugar para lembrar do prazo.",
       "Antes de enviar, teste todos os passos: página de vendas, página de pedidos e pagamento."],
      "Pegadinha: e-mail de abertura longo e cheio de argumentos. Os argumentos estavam nos conteúdos.",
      F,
      "Às 10 horas a padeira manda: as inscrições do curso de pão caseiro estão abertas, clique aqui. P.S.: o bônus de "
      "receitas de fermentação fica disponível só até quinta à meia-noite."),
    p("A oferta tem cinco partes",
      "A oferta não é só o produto. Ela junta o produto, os bônus, o preço, as condições de pagamento e a garantia, e "
      "cada parte pode tirar um motivo para não comprar.",
      ["O produto é a transformação prometida nos conteúdos, agora com caminho completo.",
       "Os bônus somam valor e podem ser usados como escassez, saindo do ar numa data.",
       "As condições de pagamento, como parcelar, tiram a barreira do preço à vista.",
       "A garantia transfere o risco para quem vende e reduz o medo de errar na compra."],
      "A pergunta pede os componentes da oferta: produto com bônus, preço, condições de pagamento e garantia.",
      F,
      "Oferta do curso de horta: 8 aulas e um guia de pragas como bônus, R$ 297 ou 6 vezes de R$ 55, e garantia de 30 "
      "dias. Quem tinha medo de não dar certo encontra na garantia a resposta."),
], [
    q("Como deve ser o e-mail da abertura do carrinho?",
      ["curto, avisando que abriu e com o link da página de vendas",
       "longo, repetindo todos os argumentos dos vídeos",
       "sem link, para criar curiosidade",
       "enviado só para quem já comprou antes",
       "com o preço escondido até o fim do texto"],
      c("o convencimento já aconteceu no pré-lançamento; a abertura só aponta o caminho.",
        "repetir tudo cansa; sem link não há compra; clientes antigos são parte da lista, não toda; esconder o preço "
        "irrita.",
        "abertura = aviso + link.")),
    q("Qual parte do e-mail o livro diz ser a mais lida?",
      ["o P.S.",
       "o assunto escrito em maiúsculas",
       "a assinatura com o telefone",
       "o primeiro parágrafo longo",
       "o rodapé com o descadastro"],
      c("o P.S. é muito lido e foi usado para lembrar a escassez.",
        "as outras partes não são as destacadas pelo livro.",
        "use o P.S. para o prazo.")),
    q("Antes de enviar o e-mail de abertura, o que é indispensável fazer?",
      ["testar páginas, pedido e pagamento",
       "mudar o preço anunciado no último vídeo",
       "apagar os comentários do pré-lançamento",
       "trocar o nome do produto na última hora",
       "desligar a página de vendas para revisar"],
      c("se o pagamento falha na hora do pico, as vendas se perdem.",
        "mudar preço ou nome quebra a confiança; apagar comentários perde a prova social; desligar a página impede a "
        "venda.",
        "testa tudo antes de abrir.")),
    q("Quais são as partes de uma oferta, segundo o livro?",
      ["produto com bônus, preço, condições de pagamento e garantia",
       "somente o produto e o preço à vista, sem mais nada",
       "logotipo, cores da marca e uma página bonita",
       "número de seguidores, curtidas e comentários",
       "comissão dos afiliados e verba de anúncios pagos"],
      c("a oferta reúne o que se entrega, quanto custa, como pagar e a garantia.",
        "só produto e preço é incompleto; marca, seguidores e afiliados não são a oferta.",
        "oferta = produto + bônus + preço + condições + garantia.")),
    q("Qual a função principal da garantia na oferta?",
      ["transferir o risco para quem vende e reduzir o medo",
       "aumentar o preço do produto em dobro",
       "impedir que o cliente peça o dinheiro de volta",
       "substituir o conteúdo do pré-lançamento",
       "criar escassez no primeiro dia"],
      c("com garantia, o cliente arrisca pouco, e a objeção do medo some.",
        "não muda o preço; ela permite a devolução; não substitui conteúdo; escassez vem do prazo.",
        "garantia tira o risco do cliente.")),
])

_M.mod("fechamento", 2, "Carrinho aberto e o grande fechamento", [
    p("Dois picos de vendas",
      "As vendas não se espalham por igual. Há um pico na abertura, pela expectativa, e outro no fechamento, pela "
      "escassez, com um vale no meio que pede e-mails de apoio.",
      ["O carrinho costuma ficar aberto de quatro a sete dias.",
       "No primeiro dia vende quem já esperava a oferta, graças à expectativa criada.",
       "No meio do período se mandam e-mails com depoimentos, perguntas respondidas e casos.",
       "Nas últimas 24 horas vem o maior pico, porque a escassez faz agir quem estava em dúvida."],
      "Pegadinha: parar de mandar e-mails depois da abertura. O vale do meio e o fechamento pedem comunicação.",
      F,
      "Lançamento de 5 dias: 35% das vendas no primeiro dia, 20% espalhadas nos três dias do meio e 45% no último dia, "
      "depois de três e-mails avisando que o bônus ia sair do ar."),
    p("O fechamento precisa doer",
      "Sem consequência para quem não comprar, não há escassez. O livro diz que um fechamento real pode dobrar o "
      "resultado, e que evitar a escassez corta as vendas pela metade.",
      ["Fechamento real pode ser fim das vagas, fim do bônus ou subida do preço depois da data.",
       "No último dia se mandam vários e-mails, porque é quando a maioria decide.",
       "O prazo tem de ser cumprido, senão a escassez do próximo lançamento morre.",
       "Quem pediu para não receber mais e-mails do lançamento deve ser respeitado."],
      "A pergunta clássica: o que acontece sem fechamento real? O pico final some e as vendas caem muito.",
      F,
      "O curso de horta fecha na quinta à meia-noite e só reabre em seis meses, com preço maior. Na quinta saem três "
      "e-mails, às 9, às 18 e às 22 horas, e a última hora tem mais vendas que a terça inteira."),
], [
    q("Por quantos dias o carrinho costuma ficar aberto, segundo o livro?",
      ["de quatro a sete dias",
       "uma hora apenas",
       "trinta dias corridos",
       "um ano inteiro",
       "sem prazo para fechar"],
      c("o período curto concentra a decisão entre os dois picos.",
        "uma hora é exceção; trinta dias e um ano diluem a escassez; sem prazo não há fechamento.",
        "carrinho aberto: 4 a 7 dias.")),
    q("Em que momento costuma acontecer o maior pico de vendas?",
      ["nas últimas 24 horas antes do fechamento",
       "no meio do período de carrinho aberto",
       "uma semana depois do fechamento",
       "antes do primeiro conteúdo gratuito",
       "no pré-pré-lançamento"],
      c("a escassez real faz quem estava em dúvida decidir no fim.",
        "o meio é o vale; depois do fechamento não há venda; antes da oferta não se vende.",
        "pico final = escassez.")),
    q("O que o livro afirma sobre evitar a escassez real no fim do lançamento?",
      ["pode reduzir as vendas pela metade",
       "não muda nada nas vendas do lançamento",
       "dobra as vendas do primeiro dia",
       "é o jeito mais seguro de lançar",
       "só importa para produtos físicos"],
      c("sem consequência por esperar, as pessoas adiam e não compram.",
        "muda muito; não age no primeiro dia; não é mais seguro; vale para qualquer produto.",
        "sem fechamento real, metade das vendas.")),
    q("No vale do meio do carrinho aberto, o que fazer?",
      ["mandar e-mails com depoimentos e respostas às dúvidas",
       "parar de se comunicar até chegar o último dia",
       "fechar o carrinho mais cedo, sem avisar ninguém",
       "abaixar o preço a cada dia, sem nenhum critério",
       "apagar a página de vendas por alguns dias"],
      c("o meio do período pede prova social e resposta a objeções para manter o interesse.",
        "silêncio desperdiça vendas; fechar sem aviso quebra a confiança; preço caindo ensina a esperar; apagar a página "
        "impede comprar.",
        "carrinho aberto pede comunicação.")),
    q("Qual destes é um fechamento real?",
      ["o bônus sai do ar e o preço sobe depois da data",
       "o prazo é prorrogado toda vez que chega ao fim",
       "o carrinho fecha e reabre no dia seguinte",
       "o mesmo desconto existe o ano todo",
       "a data de fechamento nunca é informada"],
      c("há perda concreta para quem não comprar no prazo.",
        "prorrogar, reabrir e desconto eterno ensinam que o prazo é falso; sem data não há escassez.",
        "fechamento real tem consequência.")),
])

_M.mod("depois", 3, "Quando dá errado e depois do lançamento", [
    p("E se ninguém comprar?",
      "Lançamento fraco também ensina. O livro recomenda ouvir o mercado, descobrir a objeção que travou a compra e "
      "ajustar a oferta, em vez de desistir.",
      ["Pergunte a quem não comprou o que impediu, e leia os comentários de novo.",
       "Muitas vezes o problema é uma objeção não respondida, como preço, tempo ou medo de não conseguir.",
       "Ajustar a oferta, como incluir parcelamento ou garantia maior, pode virar o resultado.",
       "Um lançamento pequeno ainda deixa lista, depoimentos e aprendizado para o próximo."],
      "A pergunta clássica: a primeira atitude após vendas baixas? Ouvir o público e achar a objeção, não desistir.",
      F,
      "O curso de pão vendeu 6 vagas. A pesquisa mostrou que o medo era não ter forno bom. A padeira acrescentou uma aula "
      "de pão na panela e, no lançamento seguinte, vendeu 60."),
    p("Depois do lançamento: cuide de quem comprou",
      "O lançamento bem feito deixa prestígio no mercado. O pós-lançamento entrega o prometido, recebe bem os novos "
      "clientes e prepara o próximo ciclo.",
      ["Entregar mais do que o prometido transforma clientes em fãs e depoimentos.",
       "Quem não comprou continua na lista e pode comprar no próximo lançamento.",
       "Os resultados dos alunos viram prova social para o lançamento seguinte.",
       "Cada lançamento aumenta a lista, e isso deixa o próximo mais fácil."],
      "Pegadinha: tratar o lançamento como fim. Ele é o começo da relação com quem comprou.",
      F,
      "Depois de vender 60 vagas, a padeira manda um vídeo de boas-vindas, acompanha as primeiras fornadas e pede fotos. "
      "Seis meses depois, as fotos das alunas viram a prova social do novo lançamento."),
], [
    q("O lançamento vendeu muito pouco. Qual a primeira atitude recomendada?",
      ["ouvir o público e descobrir a objeção que travou a compra",
       "desistir do produto e do mercado",
       "culpar a lista e comprar outra",
       "reabrir o carrinho com metade do preço sem explicar",
       "apagar todos os conteúdos publicados"],
      c("a resposta do mercado mostra o que ajustar; muitas vezes é uma objeção sem resposta.",
        "desistir, culpar a lista, cortar preço sem critério ou apagar conteúdo não resolvem a causa.",
        "lançamento fraco = escute e ajuste.")),
    q("O que acontece com quem não comprou no lançamento?",
      ["continua na lista e pode comprar no próximo",
       "deve ser removido da lista imediatamente",
       "recebe a cobrança do produto mesmo assim",
       "é transferido para a lista dos parceiros",
       "perde o acesso a qualquer conteúdo futuro"],
      c("a lista de lançamento é um ativo; muita gente compra no lançamento seguinte.",
        "remover desperdiça a relação; cobrar sem compra é errado; não se passa a lista adiante; não se pune quem não "
        "comprou.",
        "quem não comprou ainda é público.")),
    q("Qual a maior fonte de prova social para o próximo lançamento?",
      ["os resultados dos alunos que compraram",
       "o número de anúncios pagos rodados",
       "a cor da página de vendas",
       "o tamanho do e-mail de abertura",
       "o número de dias de carrinho aberto"],
      c("depoimentos e resultados reais mostram que o produto funciona.",
        "anúncios, cor, tamanho do e-mail e dias abertos não provam resultado.",
        "aluno com resultado = prova social.")),
    q("Por que cada lançamento facilita o seguinte?",
      ["deixa a lista maior e mais prova social",
       "porque o preço cai automaticamente",
       "porque dispensa o pré-lançamento seguinte",
       "porque os parceiros passam a trabalhar de graça",
       "porque o público esquece o lançamento anterior"],
      c("o lançamento cresce a lista e acumula depoimentos e confiança.",
        "o preço não cai sozinho; o pré-lançamento continua; parceiros recebem comissão; esquecer não ajuda.",
        "lançamento gera lista e prova para o próximo.")),
    q("Uma objeção comum que trava compras e pode ser resolvida mudando a oferta é:",
      ["o preço à vista, resolvido com parcelamento",
       "a cor do botão, resolvida com outro tom",
       "o número de bônus, resolvido tirando todos",
       "a garantia, resolvida eliminando a garantia",
       "o horário da abertura, resolvido sem data"],
      c("o parcelamento tira a barreira do valor à vista, uma objeção frequente.",
        "cor não é objeção relevante; tirar bônus e garantia piora; sem data perde o evento.",
        "objeção de preço → condições de pagamento.")),
])

MODULOS = _M.modulos
ROTEIRO = [MODULOS[1]["aula"][1]]
POR_ID = {qq["id"]: qq for m in MODULOS for qq in m["questoes"]}


def todas():
    return [qq for m in MODULOS for qq in m["questoes"]]
