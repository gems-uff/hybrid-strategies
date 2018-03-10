# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

dahlberg1997a = DB(WorkUnrelated(
    1997, "Challenges to \IS\ quality",
    display="dahlberg",
    authors="Tomi Dahlberg and Janne Jarvinen",
    place=IST,
    pp="809 - 818",
    entrytype="article",
    volume="39",
    number="12",
    note="Information System Quality",
    issn="0950-5849",
    doi="https://doi.org/10.1016/S0950-5849(97)00039-6",
    link="https://www.sciencedirect.com/science/article/pii/S0950584997000396",
    keyword="Software process",
    ID="Dahlberg1997809",
    sciencedirect="1",
    placex="Information and Software Technology",
))

fowler1997a = DB(WorkUnrelated(
    1997, "An expert system in the domain of software technology transfer",
    display="fowler",
    authors="P. Fowler and I. García Martín and N. Juristo and L. Levine and J.L. Morant",
    place=FAKE,
    pp="275 - 300",
    entrytype="article",
    volume="12",
    number="3",
    note="",
    issn="0957-4174",
    doi="https://doi.org/10.1016/S0957-4174(96)00100-5",
    link="https://www.sciencedirect.com/science/article/pii/S0957417496001005",
    ID="Fowler1997275",
    sciencedirect="1",
    placex="Expert Systems with Applications",
))

king1997a = DB(WorkUnrelated(
    1997, "Tool support for systems emergence: A multimedia \CASE\ tool",
    display="king",
    authors="Stephen King",
    place=IST,
    pp="323 - 330",
    entrytype="article",
    volume="39",
    number="5",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/S0950-5849(96)01153-6",
    link="https://www.sciencedirect.com/science/article/pii/S0950584996011536",
    keyword="Computer-based learning",
    ID="King1997323",
    sciencedirect="1",
    placex="Information and Software Technology",
))

reiblein1997a = DB(WorkSnowball(
    1997, "SPI: 'I can't get no satisfaction' - Directing process improvement to meet business needs",
    display="reiblein",
    authors="Reiblein, S. and Symons, A.",
    place=SQJ,
    pp="89-98",
    entrytype="inproceedings",
    volume="6",
    number="2",
    note="cited By 3",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0642363922&partnerID=40&md5=0f4fad949ad46a78811b5c9349aa559a",
    document_type="Article",
    source="Scopus",
    ID="Reiblein199789",
    scopus="1",
))
