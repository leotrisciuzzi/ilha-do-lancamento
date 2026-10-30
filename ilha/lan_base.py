"""Ilha do Lançamento — peças comuns aos mundos de marketing (o livro "A Fórmula do Lançamento", Jeff Walker).

Os mundos usam o mesmo molde dos mundos do internato (base_mundo.Mundo: alternativa certa escrita primeiro e
embaralhada com semente = id); aqui ficam as contas e as tabelas que mais de um treino usa."""
from .base_mundo import Mundo, classificar, fmt, num_alts  # noqa: F401  (reexporta para os mundos)

MATERIA = "Marketing"
LIVRO = "Walker, A Fórmula do Lançamento"
ORIGEM = "A Fórmula do Lançamento"


def mundo(pref, assunto):
    return Mundo(pref, MATERIA, assunto, origem=ORIGEM)


def reais(v):
    """R$ 12.345 (sem centavos) no padrão brasileiro."""
    return "R$ " + f"{round(v):,}".replace(",", ".")


def alts_reais(rng, certo, erros, passo):
    """Alternativas em reais: a certa + erros típicos + vizinhos, distintas depois de formatar."""
    vistos, out = {reais(certo)}, []
    for v in erros:
        t = reais(v)
        if v > 0 and t not in vistos:
            vistos.add(t)
            out.append(t)
    k = 1
    while len(out) < 4:
        t = reais(certo + passo * k * (1 if k % 2 else -1))
        k += 1
        if t not in vistos and certo + passo * k > 0:
            vistos.add(t)
            out.append(t)
    return reais(certo), out[:4]


GATILHOS = [
    ("O especialista mostra anos de resultado e ensina com segurança antes de oferecer qualquer coisa", "autoridade",
     "seguimos quem está em posição de autoridade; ensinar bem mostra que você sabe."),
    ("Você entrega três vídeos gratuitos e muito úteis, e o público sente que deve algo em troca", "reciprocidade",
     "quem recebe valor sente a obrigação de retribuir."),
    ("Você cumpre o que promete: o vídeo sai no dia e na hora anunciados, e a promessa do conteúdo é entregue",
     "confiança", "promessa cumprida vira confiança, e confiança vira compra."),
    ("Você anuncia a data e conta o que vem no próximo vídeo, e o público conta os dias", "expectativa",
     "esperar por algo que se deseja aumenta o desejo; é um pilar do lançamento."),
    ("Você conta a própria história, com erros e bastidores, e o público passa a gostar de você", "simpatia",
     "compramos de quem gostamos."),
    ("O lançamento tem data de abertura e contagem regressiva, como um acontecimento", "eventos e rituais",
     "transformar o marketing num evento o torna sedutor."),
    ("Os inscritos conversam entre si nos comentários e se sentem parte de um grupo", "comunidade",
     "pertencer a um grupo muda o comportamento: os membros compram juntos."),
    ("O bônus some à meia-noite de quinta e o preço sobe depois do fechamento", "escassez",
     "o que fica menos disponível passa a ser mais desejado."),
    ("Você mostra depoimentos e o volume de comentários de quem já está participando", "prova social",
     "olhamos o que os outros fazem para decidir o que fazer."),
]

FASES = [
    ("Mandar um e-mail curto avisando que algo está sendo preparado e perguntando qual a maior dificuldade do público",
     "pré-pré-lançamento", "aquecimento: chamar atenção e ouvir, sem vender."),
    ("Publicar o vídeo que mostra a oportunidade e responde 'por quê' o público deveria se importar",
     "pré-lançamento: PLC nº 1", "o primeiro conteúdo é a oportunidade."),
    ("Publicar o vídeo que ensina algo útil e já transforma um pouco a vida do público", "pré-lançamento: PLC nº 2",
     "o segundo conteúdo é a transformação."),
    ("Publicar o vídeo que mostra como seria ter o resultado, e começa a revelar o produto", "pré-lançamento: PLC nº 3",
     "o terceiro conteúdo é a experiência da propriedade."),
    ("Mandar o e-mail com o link da página de vendas: as compras estão liberadas", "lançamento: abertura do carrinho",
     "a abertura colhe a expectativa criada."),
    ("Avisar que faltam poucas horas e que o bônus vai sair do ar", "lançamento: fechamento",
     "a escassez real gera o pico do último dia."),
    ("Entregar o produto, receber os novos clientes e pedir depoimentos", "pós-lançamento",
     "cuidar de quem comprou prepara o próximo lançamento."),
]
