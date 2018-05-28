# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

corazza2011a = DB(WorkUnrelated(
    2011, "Investigating the use of Support Vector Regression for web effort estimation",
    display="corazza",
    authors="Corazza, Anna and Di Martino, Sergio and Ferrucci, Filomena and Gravino, Carmine and Mendes, Emilia",
    place=ESE,
    pp="211--243",
    entrytype="article",
    volume="16",
    number="2",
    publisher="Springer",
    ID="corazza2011investigating",
    cluster_id="2389357472623947693",
    scholar="http://scholar.google.com/scholar?cites=2389357472623947693&as_sdt=2005&sciodt=0,5&hl=en",
))

kocaguneli2011a = DB(WorkOk(
    2011, "How to find relevant data for effort estimation?",
    display="kocaguneli",
    authors="Kocaguneli, Ekrem and Menzies, Tim",
    place=ESEM,
    pp="255--264",
    entrytype="inproceedings",
    art_number="6092574",
    note="cited By 24",
    ID="Kocaguneli2011255",
    cluster_id="15069744916596527173",
    scholar="http://scholar.google.com/scholar?cites=15069744916596527173&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE",
    scholar_ok=True,
))

martino2011a = DB(WorkUnrelated(
    2011, "Using web objects for development effort estimation of web applications: a replicated study",
    display="martino",
    authors="Di Martino, Sergio and Ferrucci, Filomena and Gravino, Carmine and Sarro, Federica",
    place=ICPFSPI,
    pp="186--201",
    entrytype="inproceedings",
    organization="Springer",
    ID="di2011using",
    cluster_id="5521763665436668575",
    scholar="http://scholar.google.com/scholar?cites=5521763665436668575&as_sdt=2005&sciodt=0,5&hl=en",
))

menzies2011a = DB(WorkOk(
    2011, "Local vs. global models for effort estimation and defect prediction",
    display="menzies",
    authors="Menzies, Tim and Butcher, Andrew and Marcus, Andrian and Zimmermann, Thomas and Cok, David",
    place=ICASE,
    pp="343--351",
    entrytype="inproceedings",
    doi="10.1109/ASE.2011.6100072",
    art_number="6100072",
    note="cited By 56",
    ID="Menzies2011343",
    cluster_id="14175246749991764669",
    scholar="http://scholar.google.com/scholar?cites=14175246749991764669&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE",
    scholar_ok=True,
))
