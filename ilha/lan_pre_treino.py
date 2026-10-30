"""Treino do Mundo do aquecimento e dos três vídeos (Ilha do Lançamento): cena → PLC (por quê, o quê, como), ação →
fase do lançamento e peça do roteiro de cada conteúdo. Gabarito pela tabela dos capítulos 6 e 7."""
from .lan_base import FASES, MATERIA, classificar
from .base_mundo import Treino

PREFIXO = "lpr-treino"

HABILIDADES = {
    "plc": ("Qual PLC é esse?", "Conteúdo → PLC nº 1, 2 ou 3"),
    "fase": ("Em que fase estamos?", "Ação → fase do lançamento"),
    "roteiro": ("Peça do roteiro", "Trecho do vídeo → função"),
}

_PLC = [
    ("Vídeo que mostra por que aprender a investir muda a vida de quem ganha pouco", "PLC nº 1: oportunidade",
     "responde ao porquê."),
    ("Vídeo que ensina a montar uma planilha de gastos em 10 minutos", "PLC nº 2: transformação",
     "ensina e já muda algo."),
    ("Vídeo que mostra como seria ter a reserva de emergência pronta em um ano", "PLC nº 3: experiência da propriedade",
     "mostra como é ter o resultado."),
    ("Vídeo em que a autora conta por que a confeitaria caseira virou renda para muita gente", "PLC nº 1: oportunidade",
     "apresenta a oportunidade."),
    ("Vídeo que ensina o ponto da calda de chocolate passo a passo", "PLC nº 2: transformação", "ensinamento prático."),
    ("Vídeo que mostra a rotina de quem já vende 200 bolos por mês e o que há no curso",
     "PLC nº 3: experiência da propriedade", "como seria viver o resultado e o produto aparecendo."),
]

_ROTEIRO = [
    ("'Eu já estive onde você está e hoje ensino milhares de pessoas'", "posicionamento",
     "mostra por que ouvir você."),
    ("'Muita gente acha que precisa de muito dinheiro para começar, e vou mostrar que não'", "resposta a objeção",
     "derruba um medo antes da oferta."),
    ("'No próximo vídeo vou mostrar o erro que derruba 9 em cada 10 iniciantes'", "gancho para o próximo",
     "cria expectativa."),
    ("'Conte nos comentários qual é a sua maior dificuldade'", "convocação à ação", "pede um compromisso."),
    ("'Faça agora este exercício de 5 minutos'", "ensinamento", "entrega valor real."),
]


T = Treino(MATERIA, PREFIXO, HABILIDADES, {
    "plc": lambda rng: classificar(rng, _PLC, "Qual conteúdo do pré-lançamento é esse?",
                                   extras=["tiro de aviso do pré-pré", "vídeo de vendas da abertura"]),
    "fase": lambda rng: classificar(rng, FASES, "Em que fase do lançamento isso acontece?"),
    "roteiro": lambda rng: classificar(rng, _ROTEIRO, "Que peça do roteiro do conteúdo é essa?",
                                       extras=["oferta com preço"]),
})
questao, taxa_erro, fase = T.questao, T.taxa_erro, T.fase
