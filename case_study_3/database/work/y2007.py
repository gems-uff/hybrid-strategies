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

martino2007a = DB(WorkUnrelated(
    2007, "Comparing size measures for predicting web application development effort: a case study",
    display="martino",
    authors="Di Martino, Sergio and Ferrucci, Filomena and Gravino, Carmine and Mendes, Emilia",
    place=ESEM,
    pp="324--333",
    entrytype="inproceedings",
    organization="IEEE",
    ID="di2007comparing",
    cluster_id="11352876494609783703",
    scholar="http://scholar.google.com/scholar?cites=11352876494609783703&as_sdt=2005&sciodt=0,5&hl=en",
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
    excerpt="Abstract Previous studies comparing the prediction accuracy of effort models built using Web cross-and single-company data sets have been inconclusive, and as such replicated studies are necessary to determine under what circumstances a company can place reliance on a ",
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

mendes2007c = DB(WorkUnrelated(
    2007, "Predicting Web Development Effort Using a Bayesian Network.",
    display="mendes c",
    authors="Mendes, Emilia",
    place=EASE,
    entrytype="inproceedings",
    ID="mendes2007predicting",
    cluster_id="12517914100752042468",
    scholar="http://scholar.google.com/scholar?cites=12517914100752042468&as_sdt=2005&sciodt=0,5&hl=en",
))

mendes2007d = DB(WorkUnrelated(
    2007, "The use of a Bayesian network for web effort estimation",
    display="mendes d",
    authors="Mendes, Emilia",
    place=WE,
    pp="90--104",
    entrytype="article",
    publisher="Springer",
    ID="mendes2007use",
    cluster_id="5606683204247937713",
    scholar="http://scholar.google.com/scholar?cites=5606683204247937713&as_sdt=2005&sciodt=0,5&hl=en",
))

premraj2007a = DB(WorkSnowball(
    2007, "Building software cost estimation models using homogenous data",
    display="premraj",
    authors="Premraj, Rahul and Zimmermann, Thomas",
    place=ESEM,
    pp="393--400",
    entrytype="inproceedings",
    organization="IEEE",
    ID="premraj2007building",
    cluster_id="8455703022459318692",
    scholar="http://scholar.google.com/scholar?cites=8455703022459318692&as_sdt=2005&sciodt=0,5&hl=en",
))
