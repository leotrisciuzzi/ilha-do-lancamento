#!/usr/bin/env python3
"""Confere a DIDÁTICA das pílulas (o resumo antes de cada fase) — o padrão que todo mundo novo segue.

    venv/bin/python tools/checar_pilulas.py                 # relatório de todos os mundos
    venv/bin/python tools/checar_pilulas.py reumatologia    # só um mundo (sai com erro se reprovar)

Padrão de uma pílula (ilha/<tema>.py, campo "aula" de cada módulo):
  titulo    curto (até 48 caracteres), diz o assunto;
  ideia     1–2 frases com o PORQUÊ (mecanismo em linguagem simples) — a frase que o aluno leva para a prova;
  pontos    2–4 frases COMPLETAS (sujeito + verbo), uma ideia por frase, com conectivo de causa quando houver
            ("porque", "por isso", "então"); números sempre com unidade e com o que significam;
  na_prova  como a banca cobra / a pegadinha clássica, em 1–2 frases;
  fonte     diretriz/consenso padrão-ouro e o ano (ex.: "EULAR 2025; ACR 2021");
  exemplo   (opcional) caso resolvido: a regra aplicada a um paciente, com números, em 15–90 palavras.
Proibido: lista de nomes separada por vírgulas no lugar de frase, palavra GRITADA em maiúsculas no lugar
de explicação, parênteses dentro de parênteses, "etc.", seta (→) como substituto de verbo em excesso.

MUNDOS_PADRAO = mundos já no padrão novo: aqui um erro reprova (os testes chamam checar())."""
import importlib
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

MFC = ["mfc_epidemio", "mfc_sus", "mfc_consulta", "mfc_vigilancia", "mfc_trabalhador", "mfc_indicadores", "mfc_idoso",
       "mfc_etica"]           # Internato · MFC, por prevalência nas provas (nov/2026)
MUNDOS = ["reumatologia", "gasometria", "ventilacao", "hipercalemia", "insuf_cardiaca", "farmaco_cardio", "farmaco_atb",
          "internato_asma", "internato_dpoc", "internato_vm", "internato_transf", "internato_reum", "internato_fa", "internato_endo", "internato_cognicao", "internato_parkinson",
          "internato_nefro", "internato_has", "internato_hemato", "internato_pneumo", "internato_neuro", "internato_dermato", "internato_hepato", "internato_relatos",
          "caso_pneumonia", "caso_abscesso_renal", "caso_graves", "caso_coledoco"] + MFC
MUNDOS_PADRAO = {"reumatologia", "hipercalemia", "insuf_cardiaca", "gasometria", "ventilacao", "farmaco_cardio", "farmaco_atb",
                 "internato_asma", "internato_dpoc", "internato_vm", "internato_transf", "internato_reum", "internato_fa", "internato_endo", "internato_cognicao", "internato_parkinson",
                 "internato_nefro", "internato_has", "internato_hemato", "internato_pneumo", "internato_neuro", "internato_dermato", "internato_hepato", "internato_relatos",
                 "caso_pneumonia", "caso_abscesso_renal", "caso_graves", "caso_coledoco"} | set(MFC)

# siglas e nomes próprios que são legitimamente em maiúsculas
SIGLAS = set("""ACR EULAR ASAS SBR KDIGO OMS WHO AHA ANCA HLA FAN DNA RNP SSA SSB SCL CCP PCR VHS LES SAF AR AIJ
AINE AINES DMARD DMARDS JAK TNF IL HCQ MTX MMF AAS HBPM INR AVC IAM TEP TVP TC RM USG PET ECG ECO EAS IECA BRA
DPI HAP PCR VHS UTI DRC TFG TFGE ICAP GPA MPA EGPA PAN ACG PMR CPPD HAQ DAS CDAI SDAI BASDAI ASDAS CASPAR GRAPPA
OARSI IVIG IGIV IGA IGE IGG IGM HIV HCV HBV HBSAG PPD IGRA TB EULAR/ACR ACR/EULAR SUS SUS-SP USP ENARE PSU-MG
CAD FR AV SA SNC SNP RX TGO TGP CPK CK LDH PTH VDRL ASLO ICC IC FEVE BNP NT-PROBNP PAM PA FC FR SPO2 PAO2 PACO2
HCO3 SDRA VNI PEEP VCV PCV PSV CPAP BIPAP FIO2 VT PPLAT DP IMC ATR SIADH ADH ECA ARA ARNI SGLT2 ISGLT2 BB MRA
DOAC VKA NOAC AVK UFH LMWH BCG VSR EBV CMV HPV HSV OMS-2024 CRAB PNA MDA5 HMGCR SRP TIF1 NXP2 MI2 SAE JO-1
ORAL MALT EDTA ENAC ROMK ESBL ISRS CURB CURB-65 PEN-FAST FAST KPC GINA MART SABA LABA LAMA SAMA PCDT SBPT GOLD CONITEC TSLP DRGE ABPA AMIB PADIS RASS ESICM SCCM PROSEVA PLATINO EXACOS-CV SKOPOS-MAZI EPAP IPAP NDM AMPC MRSA VRE MSSA DPOC GOLDMARK LEMON FLORALI DOPE ROX EOLIA ARDSNET NYHA BENEFIT FINEARTS FINEARTS-HF STRONG STRONG-HF SODIUM SODIUM-HF DOSE ADVOR IRONMAN AFFIRM AFFIRM-AHF SCAI ECMO HARMONIZE H2FPEF CHA2DS2-VA HFA GIACTA PROSEVA RAISE PRODERM PL-7 PL-12 EJ OJ MRSA MSSA VDRL FTA-ABS TPHA LCR LCS PFA PFP NNT NNH RR OR IC95% K⁺ NA⁺ CL⁻ CO₂ O₂ H⁺ TACO TRALI RFNH AABB ICTMG GRADE CIVD TCTH ANVISA PATCH CARES DRESS DECT ELISA NICE BLYS BAFF HEP-2 VIII XIII ILAE TDPM ICHD SNOOP LARC ACOG DAPT ACTH TOTG MEEM BBRC UPDRS MDS-UPDRS COMT NMDA APOE HAS-BLED BLED ACOD DOAC INVICTUS RE-ALIGN ALIGN ETE
HCTZ GNPE DDAVP FENA PLA2R ASLO GNRP SRAA CIVD AEIOU IDSA KDIGO-2024 CURB QSOFA SOFA PREVENT MAPA MRPA ICFEP ICFER
HFPEF HFREF ILAE SIRS GASA TIPS HBSAG ANTI-HBS ANTI-HBC HBEAG CHCM NIHSS SAMU AHA/ASA SCL-70 CREST HLA-B27 SCASSST IAMCSST
TIMI GRACE HEART ACC/AHA SBD/SBEM NCEP MMRC PLATO DDAVP PTH-I EPO WELLS PERC HBPM-SC DOAC-S LEMS PENFIGO MOHS SBPT
AIRE ACCP BAAR CPFE MGUS PAUSE HUGS VATS MIST TTPA CPRE ASGE LADA PRES ESPEN ASHP EASD MASLD AHAI TRAB MELD PICC ANTI SSC-2026 SIADH DRESS NECROLISE STEVENS-JOHNSON ABCDE PAAF TIRADS BRAF FEOCROMOCITOMA SEPSE-3 ACLS PROCAPS VASC DPP-4 DLCO DXA MALT
NASF RENASES RENAME INAMPS CAPS CAPSI PNAB COAP APS UBS ESF EMULTI SINAN SINASC SIAB SISAB CIAP CID SOAP SPIKES MCCP
USPSTF INCA CEREST NTEP INSS DORT PAIR PCMSO SESMT CIPA RAPS CEM ECA BEERS AVD AIVD SBGG IVCF CAGE AUDIT PHQ GAD MRSA
FIRO PRACTICE APGAR ACS ESUS E-SUS COVID DTP DTPA ROTAVÍRUS SRAG LOAS SAMU NOB NOAS PPA LDO LOA RENAST FGTS CLT PPP
LTCAT EPI EPC SAT FAP SUS-MG MEDCURSO SBMFC STOPP START ZARIT CONASS CONASEMS SINAN-NET PCDT-HIV TSH PSA HPV-DNA ADA USG-TV OMS-2025
""".split())
_PALAVRA_CAPS = re.compile(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{4,}\b")


def _palavras(t):
    return len(re.findall(r"\w+", t))


def problemas_pilula(p):
    """Lista de (gravidade, mensagem). gravidade: 'erro' reprova; 'aviso' só aponta."""
    out = []
    tit = p.get("titulo", "")
    if not tit or len(tit) > 48:
        out.append(("erro", f"título vazio ou longo ({len(tit)} > 48)"))
    ideia = p.get("ideia", "")
    if not ideia:
        out.append(("erro", "falta a IDEIA (o porquê em 1–2 frases)"))
    elif not (10 <= _palavras(ideia) <= 50):
        out.append(("erro", f"ideia com {_palavras(ideia)} palavras (10–50)"))
    pontos = p.get("pontos", [])
    if not 2 <= len(pontos) <= 4:
        out.append(("erro", f"{len(pontos)} pontos (o padrão é 2–4)"))
    for i, t in enumerate(pontos, 1):
        n = _palavras(t)
        if n < 7 or n > 45:
            out.append(("erro", f"ponto {i} com {n} palavras (7–45): {t[:60]}…"))
        if not t.rstrip().endswith((".", "!", "?", ":")):
            out.append(("erro", f"ponto {i} não termina como frase: …{t[-30:]}"))
        virgulas = len(re.findall(r"(?<!\d),|,(?!\d)", t))          # vírgula decimal (5,5) não conta
        if virgulas >= 6 and not re.search(r"\b(porque|pois|então|quando|se|que)\b", t):
            out.append(("erro", f"ponto {i} parece lista solta (muitas vírgulas, nenhum conectivo)"))
        if t.count("(") > 2 or re.search(r"\([^)]*\(", t):
            out.append(("erro", f"ponto {i} com parênteses demais"))
        if t.count("→") > 2:
            out.append(("aviso", f"ponto {i} com muitas setas: troque por verbo"))
        if re.search(r"\betc\b", t, re.I):
            out.append(("erro", f"ponto {i} usa 'etc.'"))
    texto = " ".join([p.get("ideia", ""), p.get("na_prova", "")] + pontos)
    for m in _PALAVRA_CAPS.finditer(texto):
        w = m.group(0)
        antes = texto[max(0, m.start() - 40):m.start()].lower()
        nome_de_estudo = re.search(r"estudos?\b[^.]*$", antes) or re.search(r"\b(e|nos|no)\s*$", antes) and "estud" in antes
        if w.upper() not in SIGLAS and not any(ch.isdigit() for ch in w) and not nome_de_estudo:
            out.append(("erro", f"palavra gritada '{w}': explique em vez de pôr em maiúsculas"))
            break
    np = p.get("na_prova", "")
    if not np:
        out.append(("erro", "falta NA PROVA (como a banca cobra / pegadinha)"))
    elif _palavras(np) > 50:
        out.append(("erro", f"na_prova com {_palavras(np)} palavras (até 50)"))
    ex = p.get("exemplo")
    if ex is not None and not (15 <= _palavras(ex) <= 90):
        out.append(("erro", f"exemplo com {_palavras(ex)} palavras (15–90)"))
    if not p.get("fonte"):
        out.append(("erro", "falta a FONTE (diretriz padrão-ouro e ano)"))
    return out


def checar(mundo):
    """(n_pílulas, [(módulo, título, gravidade, msg)])"""
    C = importlib.import_module(f"ilha.{mundo}")
    achados, n = [], 0
    for m in C.MODULOS:
        for p in m["aula"]:
            n += 1
            for g, msg in problemas_pilula(p):
                achados.append((m["titulo"], p.get("titulo", "?"), g, msg))
    for p in getattr(C, "ROTEIRO", []):
        if p not in [a for m in C.MODULOS for a in m["aula"]]:
            n += 1
            for g, msg in problemas_pilula(p):
                achados.append(("ROTEIRO", p.get("titulo", "?"), g, msg))
    return n, achados


def main():
    alvo = sys.argv[1:] or MUNDOS
    reprovou = False
    for mundo in alvo:
        try:
            n, ach = checar(mundo)
        except ModuleNotFoundError:
            print(f"{mundo}: não existe")
            continue
        erros = [a for a in ach if a[2] == "erro"]
        status = "OK" if not erros else f"{len(erros)} erros"
        print(f"\n== {mundo}: {n} pílulas · {status} · {len(ach) - len(erros)} avisos")
        for mod, tit, g, msg in ach[:40]:
            print(f"  [{g}] {mod} › {tit}: {msg}")
        if erros and (mundo in MUNDOS_PADRAO or sys.argv[1:]):
            reprovou = True
    sys.exit(1 if reprovou else 0)


if __name__ == "__main__":
    main()
