# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

baresi2007a = DB(WorkUnrelated(
    2007, "Three empirical studies on estimating the design effort of Web applications",
    display="baresi",
    authors="Baresi, Luciano and Morasca, Sandro",
    place=ToSE,
    pp="15",
    entrytype="article",
    volume="16",
    number="4",
    publisher="ACM",
    ID="baresi2007three",
    cluster_id="6061082431312166438",
    scholar="http://scholar.google.com/scholar?cites=6061082431312166438&as_sdt=2005&sciodt=0,5&hl=en",
))

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
    excerpt="Abstract: The objective of this paper is to determine under what circumstances individual organizations would be able to rely on cross-company-based estimation models. We performed a systematic review of studies that compared predictions from cross-company ",
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

mendes2007b = DB(WorkUnrelated(
    2007, "A comparison of techniques for web effort estimation",
    display="mendes b",
    authors="Mendes, Emilia",
    place=ESEM,
    pp="334--343",
    entrytype="inproceedings",
    organization="IEEE",
    ID="mendes2007comparison",
    cluster_id="13310036169224061952",
    scholar="http://scholar.google.com/scholar?cites=13310036169224061952&as_sdt=2005&sciodt=0,5&hl=en",
))
