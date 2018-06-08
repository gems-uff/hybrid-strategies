# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

cuadrado2008a = DB(WorkUnrelated(
    2008, "Software Process and Product Measurement",
    display="cuadrado",
    authors="Cuadrado-Gallego, Juan J and Dumke, René Braungarten Reiner R and Abran, Alain",
    place=FAKE,
    entrytype="article",
    publisher="Springer",
    ID="cuadrado2008software",
    gs2016="1",
    placex="",
))

dumke2008a = DB(WorkUnrelated(
    2008, "Software Process and Product Measurement: International Conferences IWSM 2008, Metrikon 2008, and Mensura 2008 Munich, Germany, November 18-19, 2008. Proceedings",
    display="dumke",
    authors="Dumke, Reiner R and Braungarten, René and Büren, Günter and Abran, Alain and Cuadrado-Gallego, Juan J",
    place=Book,
    entrytype="book",
    volume="5338",
    publisher="Springer",
    ID="dumke2008software",
    cluster_id="10526360335824865294",
    scholar="http://scholar.google.com/scholar?cites=10526360335824865294&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="",
))

guédria2008a = DB(WorkUnrelated(
    2008, "Interoperability maturity models--survey and comparison--",
    display="guédria",
    authors="Guédria, Wided and Naudet, Yannick and Chen, David",
    place=FAKE,
    pp="273--282",
    entrytype="inproceedings",
    organization="Springer",
    ID="guedria2008interoperability",
    gs2016="1",
    placex="OTM Confederated International Conferences  On the Move to Meaningful Internet Systems",
))

lee2008a = DB(WorkSnowball(
    2008, "Ontology-based intelligent decision support agent for CMMI project monitoring and control",
    display="lee",
    authors="Lee, Chang-Shing and Wang, Mei-Hui and Chen, Jui-Jen",
    place=FAKE,
    pp="62--76",
    entrytype="article",
    volume="48",
    number="1",
    publisher="Elsevier",
    ID="lee2008ontology",
    cluster_id="2941241114858892333",
    scholar="http://scholar.google.com/scholar?cites=2941241114858892333&as_sdt=2005&sciodt=0,5&hl=en",
    selected_snowballing="1",
    selected_order="14",
    final_selected="1",
    placex="International Journal of Approximate Reasoning",
))

medina2008a = DB(WorkUnrelated(
    2008, "A Collaborative Framework to Support Software Process Improvement Based on the Reuse of Process Assets.",
    display="medina",
    authors="Medina-Domínguez, Fuensanta and Ramos, Javier Saldaña and Mora-Soto, Arturo and Sanz-Esteban, Ana and Segura, Maria Isabel Sánchez",
    place=FAKE,
    pp="283--289",
    entrytype="inproceedings",
    ID="medina2008collaborative",
    gs2016="1",
    placex="ICSOFT (PL/DPS/KE)",
))

medina2008ab = DB(WorkUnrelated(
    2008, "Approaching Software Process Improvement to Organizations through the Reuse of their Processes and Products",
    display="medina",
    authors="Medina-Domínguez, Fuensanta and Sanchez-Segura, Maria-Isabel and Mora-Soto, Arturo and Guzman, Javier García and Amescua, Antonio",
    place=FAKE,
    entrytype="article",
    ID="medinaapproaching",
    gs2016="1",
    placex="EuroSPI 2008",
))

rifaut2008a = DB(WorkUnrelated(
    2008, "Using goal-oriented requirements engineering for improving the quality of iso/iec 15504 based compliance assessment frameworks",
    display="rifaut",
    authors="Rifaut, Andre and Dubois, Eric",
    place=FAKE,
    pp="33--42",
    entrytype="inproceedings",
    organization="IEEE",
    ID="rifaut2008using",
    cluster_id="1778212616113779869",
    scholar="http://scholar.google.com/scholar?cites=1778212616113779869&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="International Requirements Engineering, 2008. RE'08. 16th IEEE",
))

rungratri2008a = DB(WorkSnowball(
    2008, "Project assets ontology (PAO) to support gap analysis for organization process improvement based on CMMI v. 1.2",
    display="rungratri",
    authors="Rungratri, Suwanit and Usanavasin, Sasiporn",
    place=ICSE,
    pp="76--87",
    entrytype="inproceedings",
    organization="Springer",
    ID="rungratri2008project",
    cluster_id="9548871908039503040",
    scholar="http://scholar.google.com/scholar?cites=9548871908039503040&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="10",
    final_selected="1",
    springer2016="1",
    placex="International Conference on Software Process",
    gs2016="1",
))

ryu2008a = DB(WorkSnowball(
    2008, "A strategic test process improvement approach using an ontological description for MND-TMM",
    display="ryu",
    authors="Ryu, Hoyeon and Ryu, Dong-Kuk and Baik, Jongmoon",
    place=FAKE,
    pp="561--566",
    entrytype="inproceedings",
    organization="IEEE",
    ID="ryu2008strategic",
    cluster_id="14629050108809422318",
    scholar="http://scholar.google.com/scholar?cites=14629050108809422318&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="3",
    final_selected="1",
    gs2016="1",
    placex="Computer and Information Science, 2008. ICIS 08. Seventh IEEE/ACIS International Conference on",
))

soto2008a = DB(WorkUnrelated(
    2008, "Using model comparison to maintain model-to-standard compliance",
    display="soto",
    authors="Soto, Martín and Münch, Jürgen",
    place=FAKE,
    pp="35--40",
    entrytype="inproceedings",
    organization="ACM",
    ID="soto2008using",
    gs2016="1",
    placex="Proceedings of the 2008 international workshop on Comparison and versioning of software models",
))
