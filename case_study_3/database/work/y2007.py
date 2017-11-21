# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kitchenham2007a = DB(WorkOk(
    2007, "Cross versus within-company cost estimation studies: A systematic review",
    display="kitchenham",
    authors="Kitchenham, Barbara A and Mendes, Emilia and Travassos, Guilherme H",
    place=ToSE,
    pp="316-329",
    entrytype="article",
    volume="33",
    number="5",
    doi="10.1109/TSE.2007.1001",
    note="cited By 175",
    ID="Kitchenham2007316",
    cluster_id="5114316298578620154",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=5114316298578620154&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

mendes2007a = DB(WorkOk(
    2007, "Effort estimation: how valuable is it for a web company to use a cross-company data set, compared to using its own single-company data set?",
    display="mendes",
    authors="Mendes, Emilia and Di Martino, Sergio and Ferrucci, Filomena and Gravino, Carmine",
    place=WWW,
    pp="963--972",
    entrytype="inproceedings",
    doi="10.1145/1242572.1242702",
    note="cited By 19",
    ID="Mendes2007963",
    cluster_id="1433474841917917990",
    scholar="http://scholar.google.com/scholar?cites=1433474841917917990&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    scholar_ok=True,
))
