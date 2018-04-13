# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mei2018a = DB(WorkUnrelated(
    2018, "A Review of Software Engineering Research in China",
    display="mei",
    authors="Mei, Hong",
    place=FAKE,
    pp="6--9",
    entrytype="article",
    volume="42",
    number="4",
    publisher="ACM",
    ID="mei2018review",
    placex="ACM SIGSOFT Software Engineering Notes",
))

novais2018a = DB(WorkUnrelated(
    2018, "Software evolution visualization: status, challenges, and research directions",
    display="novais",
    authors="Novais, Renato Lima and de Mendon{ç}a Neto, Manoel Gomes",
    place=FAKE,
    pp="2053--2067",
    entrytype="incollection",
    publisher="IGI Global",
    ID="novais2018software",
    cluster_id="15201643946563438955",
    scholar="http://scholar.google.com/scholar?cites=15201643946563438955&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Computer Systems and Software Engineering: Concepts, Methodologies, Tools, and Applications",
))

oliveira2018a = DB(WorkUnrelated(
    2018, "Experimental Analysis of Stemming on Jurisprudential Documents Retrieval",
    display="oliveira",
    authors="N de Oliveira, Robert A and C Junior, Methanias",
    place=FAKE,
    pp="28",
    entrytype="article",
    volume="9",
    number="2",
    publisher="Multidisciplinary Digital Publishing Institute",
    ID="n2018experimental",
    placex="Information",
))

sanchez2018a = DB(WorkUnrelated(
    2018, "System dynamics and agent-based modelling to represent intangible process assets characterization",
    display="sanchez",
    authors="Sanchez-Segura, Maria-Isabel and Dugarte-Peña, German-Lenin and Medina-Dominguez, Fuensanta and García de Jesús, Cynthya",
    place=FAKE,
    entrytype="article",
    publisher="Emerald Publishing Limited",
    ID="sanchez2018system",
    placex="Kybernetes",
))

valente2018a = DB(WorkUnrelated(
    2018, "Bridging EE and SE: The Goals Approach",
    display="valente",
    authors="Valente, Pedro and Aveiro, David and Nunes, Nuno",
    place=FAKE,
    entrytype="article",
    ID="valentebridging",
    placex="",
))
