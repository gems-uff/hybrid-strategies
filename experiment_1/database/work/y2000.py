# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

elliott2000a = DB(WorkUnrelated(
    2000, "Design of a product-focused customer-oriented process",
    display="elliott",
    authors="J.J Elliott",
    place=IST,
    pp="973 - 981",
    entrytype="article",
    volume="42",
    number="14",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/S0950-5849(00)00149-X",
    link="https://www.sciencedirect.com/science/article/pii/S095058490000149X",
    keyword="Product quality",
    ID="Elliott2000973",
    sciencedirect="1",
    placex="Information and Software Technology",
))

emam2000a = DB(WorkUnrelated(
    2000, "An empirical review of software process assessments",
    display="emam",
    authors="Khaled El Emam and Dennis R. Goldenson",
    place=FAKE,
    pp="319 - 423",
    entrytype="incollection",
    editor="Marvin V. Zelkowits",
    publisher="Elsevier",
    volume="53",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(00)80008-X",
    link="https://www.sciencedirect.com/science/article/pii/S006524580080008X",
    ID="Emam2000319",
    sciencedirect="1",
    placex="Emphasizing Distributed Systems",
))

emam2000b = DB(WorkUnrelated(
    2000, "Validating the ISO/IEC 15504 measures of software development process capability",
    display="emam b",
    authors="Khaled El Emam and Andreas Birk",
    place=JSS,
    pp="119 - 149",
    entrytype="article",
    volume="51",
    number="2",
    note="",
    issn="0164-1212",
    doi="https://doi.org/10.1016/S0164-1212(99)00117-X",
    link="https://www.sciencedirect.com/science/article/pii/S016412129900117X",
    ID="ElEmam2000119",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

järvinen2000a = DB(WorkUnrelated(
    2000, "The PROFES Improvement Methodology -- Enabling Technologies and Methodology Design",
    display="järvinen",
    authors="Järvinen, Janne and Komi-Sirviö, Seija and Ruhe, Guenther",
    place=PROFES,
    entrytype="inproceedings",
    editor="Bomarius, Frank and Oivo, Markku",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-45051-1_24",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

kautz2000a = DB(WorkSnowball(
    2000, "Applying and adjusting a software process improvement model in practice: the use of the IDEAL model in a small software enterprise",
    display="kautz",
    authors="Kautz, Karlheinz and Hansen, Henrik Westergaard and Thaysen, Kim",
    place=ICSE,
    pp="626-633",
    entrytype="inproceedings",
    note="cited By 40",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0033725301&partnerID=40&md5=8c6f800f5e9a4ca6f4d7d98c95ecdbbb",
    document_type="Conference Paper",
    source="Scopus",
    ID="Kautz2000626",
))

pfahl2000a = DB(WorkUnrelated(
    2000, "Using simulation to analyse the impact of software requirement volatility on project performance",
    display="pfahl",
    authors="D Pfahl and K Lebsanft",
    place=IST,
    pp="1001 - 1008",
    entrytype="article",
    volume="42",
    number="14",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/S0950-5849(00)00152-X",
    link="https://www.sciencedirect.com/science/article/pii/S095058490000152X",
    keyword="System dynamics",
    ID="Pfahl20001001",
    sciencedirect="1",
    placex="Information and Software Technology",
))

zelkowits2000a = DB(WorkUnrelated(
    2000, "Subject index",
    display="zelkowits",
    authors="Marvin V. Zelkowits",
    place=FAKE,
    pp="511 - 523",
    entrytype="incollection",
    editor="Marvin V. Zelkowits",
    publisher="Elsevier",
    volume="53",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(00)80012-1",
    link="https://www.sciencedirect.com/science/article/pii/S0065245800800121",
    key="tagkey2000511",
    ID="tagkey2000511",
    sciencedirect="1",
    placex="Emphasizing Distributed Systems",
))
