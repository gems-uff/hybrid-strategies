# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

adams1993a = DB(WorkUnrelated(
    1993, "You Are What You Measure",
    display="adams",
    authors="Adams, C. and Roberts, P.",
    place=FAKE,
    pp="504-507",
    entrytype="article",
    note="cited By 3",
    ID="Adams1993504",
    placex="Manufacturing Europe",
))

arthur1993a = DB(WorkUnrelated(
    1993, "Improving Software Quality: An Insider's Guide to TQM",
    display="arthur",
    authors="Arthur, L.J.",
    place=FAKE,
    entrytype="article",
    note="cited By 44",
    ID="Arthur1993",
    placex="New York",
))

bandinelli1993a = DB(WorkUnrelated(
    1993, "Software Process Evolution in the SPADE Environment",
    display="bandinelli",
    authors="Bandinelli, S. A. Fuggetta , and C. Ghezzi",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Bandinelli1993",
    placex="IEEE Trans. Software Eng., Vol. 19, No. 12, Pp. 1,128-1,144",
))

basili1993a = DB(WorkUnrelated(
    1993, "The experience factory and its relationship to other improvement paradigms",
    display="basili",
    authors="Basili, V.R.",
    place=FAKE,
    pp="68-83",
    entrytype="article",
    volume="717 LNCS",
    note="cited By 43",
    ID="Basili199368",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

cederling1993a = DB(WorkUnrelated(
    1993, "Industrial software development --- a case study",
    display="cederling",
    authors="Cederling, Ulf",
    place=FAKE,
    pp="226--237",
    entrytype="inproceedings",
    editor="Sommerville, Ian and Paul, Manfred",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/3-540-57209-0_16",
    springer="1",
    placex="Software Engineering --- ESEC '93",
))

cmm1993a = DB(WorkUnrelated(
    1993, "The Capability Maturity Model (CMM)",
    display="cmm",
    authors="cmm",
    place=FAKE,
    entrytype="article",
    note="cited By 982",
    ID="cmm1993",
    placex="Carnegie-Mellon University, Pittsburgh, USA, CMU/SEI-93-TR-24 and -25",
))

comer1993a = DB(WorkUnrelated(
    1993, "A measurement maturity model",
    display="comer",
    authors="Comer, P. and Chard, J.",
    place=SQJ,
    pp="277-289",
    entrytype="article",
    volume="2",
    number="4",
    doi="10.1007/BF00403770",
    note="cited By 6",
    ID="Comer1993277",
    placex="Software Quality Journal",
))

curtis1993a = DB(WorkUnrelated(
    1993, "Creating a software process improvement program",
    display="curtis",
    authors="B Curtis and M Paulk",
    place=IST,
    pp="381 - 386",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90009-R",
    link="https://www.sciencedirect.com/science/article/pii/095058499390009R",
    keyword="capability maturity model",
    ID="Curtis1993381",
    sciencedirect="1",
    placex="Information and Software Technology",
))

dion1993a = DB(WorkUnrelated(
    1993, "Process Improvement and the Corporate Balance Sheet",
    display="dion",
    authors="Dion, R.",
    place=IEEES,
    pp="28-35",
    entrytype="article",
    volume="10",
    number="4",
    doi="10.1109/52.219618",
    note="cited By 100",
    ID="Dion199328",
    placex="IEEE Software",
))

fernstro1993a = DB(WorkUnrelated(
    1993, "Process Weaver: Adding Process Support to Unix",
    display="fernstro",
    authors="Fernstro, C. M,",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Fernstro1993",
    placex="?Proc. Second Int'l Conf. Software Process",
))

kaplan1993a = DB(WorkUnrelated(
    1993, "Putting the balanced scorecard to work",
    display="kaplan",
    authors="Kaplan, R.S. and Norton, D.P.",
    place=FAKE,
    pp="134-147",
    entrytype="article",
    number="5",
    note="cited By 1010",
    ID="Kaplan1993134",
    placex="Harvard Business Review",
))

lott1993a = DB(WorkUnrelated(
    1993, "Measurement-based guidance of software projects using explicit project plans",
    display="lott",
    authors="CM Lott and HD Rombach",
    place=IST,
    pp="407 - 419",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90012-R",
    link="https://www.sciencedirect.com/science/article/pii/095058499390012R",
    keyword="project guidance",
    ID="Lott1993407",
    sciencedirect="1",
    placex="Information and Software Technology",
))

paulk1993a = DB(WorkUnrelated(
    1993, "Capability Maturity Model for Software, Version 1.1",
    display="paulk",
    authors="Paulk, M, Curtis, B, Chrissis, M, Weber, C. V,",
    place=EBSE,
    entrytype="article",
    ID="Paulk1993",
    note="cited By 1",
    placex="Carnegie Mellon University",
))

paulk1993b = DB(WorkUnrelated(
    1993, "Capability maturity model for software",
    display="paulk b",
    authors="Paulk, M.C. and Curtis, B. and Chrissis, M.B. and Weber, C.V.",
    place=FAKE,
    entrytype="article",
    note="cited By 1004",
    ID="Paulk1993",
    placex="Capability Maturity Model for Software, Version 1.1",
))

paulk1993c = DB(WorkUnrelated(
    1993, "Capability Maturity Model, Version 1.1",
    display="paulk c",
    authors="Paulk, M.C., B. Curtis, M.B. Chrissis, and C.V. Weber",
    place=IEEES,
    entrytype="article",
    note="cited By 1",
    ID="Paulk1993",
    placex="IEEE Software, Vol. 10, No. 4, Pp. 18-27",
))

thompson1993a = DB(WorkUnrelated(
    1993, "Software process maturity (SPM) and the information systems developer",
    display="thompson",
    authors="K Thompson and P McParland",
    place=IST,
    pp="331 - 338",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90003-L",
    link="https://www.sciencedirect.com/science/article/pii/095058499390003L",
    keyword="software quality",
    ID="Thompson1993331",
    sciencedirect="1",
    placex="Information and Software Technology",
))
