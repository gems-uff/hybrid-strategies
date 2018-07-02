# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

cockburn2002a = DB(WorkUnrelated(
    2002, "Agile Software Development",
    display="cockburn",
    authors="Cockburn, A.",
    place=FAKE,
    entrytype="article",
    note="cited By 1123",
    ID="Cockburn2002agile",
    placex="1st ed. Addison-Wesley Professional",
))

morgan2002a = DB(WorkUnrelated(
    2002, "Hearing children's voices: Methodological issues in conducting focus groups with children aged 7-11 years",
    display="morgan",
    authors="Morgan, M. and Gibbs, S. and Maxwell, K. and Britten, N.",
    place=FAKE,
    pp="5-20",
    entrytype="article",
    volume="2",
    number="1",
    doi="10.1177/1468794102002001636",
    note="cited By 142",
    ID="Morgan20025",
    placex="Qualitative Research",
))

ohara2002a = DB(WorkUnrelated(
    2002, "The critical aspects of emerging virtual factory profile in Japan: IT innovation in a project management context",
    display="ohara",
    authors="Ohara, Shigenobu",
    place=FAKE,
    pp="461--477",
    entrytype="article",
    volume="9",
    number="4",
    publisher="Wiley Online Library",
    ID="ohara2002critical",
    wiley2016="1",
    placex="International Transactions in Operational Research",
))

schwaber2002a = DB(WorkUnrelated(
    2002, "Agile Software Development with Scrum",
    display="schwaber",
    authors="Schwaber, K. and Beedle, M.",
    place=FAKE,
    entrytype="article",
    note="cited By 1487",
    ID="Schwaber2002",
    placex="Prentice Hall",
))

webster2002a = DB(WorkUnrelated(
    2002, "Supply system structure, management and performance: a conceptual model",
    display="webster",
    authors="Webster, Margaret",
    place=FAKE,
    pp="353--369",
    entrytype="article",
    volume="4",
    number="4",
    publisher="Wiley Online Library",
    ID="webster2002supply",
    wiley2016="1",
    placex="International Journal of Management Reviews",
))

worren2002a = DB(WorkUnrelated(
    2002, "Modularity, strategic flexibility, and firm performance: a study of the home appliance industry",
    display="worren",
    authors="Worren, Nicolay and Moore, Karl and Cardona, Pablo",
    place=FAKE,
    pp="1123--1140",
    entrytype="article",
    volume="23",
    number="12",
    publisher="Wiley Online Library",
    ID="worren2002modularity",
    wiley2016="1",
    placex="Strategic management journal",
))
