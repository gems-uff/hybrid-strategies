# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kontio1998a = DB(WorkUnrelated(
    1998, "A Software Process Engineering Framework",
    display="kontio",
    authors="Jyrki Kontio",
    place=FAKE,
    pp="35 - 108",
    entrytype="incollection",
    editor="Marvin V. Zelkowitz",
    publisher="Elsevier",
    volume="46",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(08)60203-X",
    link="https://www.sciencedirect.com/science/article/pii/S006524580860203X",
    ID="Kontio199835",
    sciencedirect="1",
    placex="",
))

paulk1998a = DB(WorkUnrelated(
    1998, "Software Process Appraisal and Improvement: Models and Standards",
    display="paulk",
    authors="Mark C. Paulk",
    place=FAKE,
    pp="1 - 33",
    entrytype="incollection",
    editor="Marvin V. Zelkowitz",
    publisher="Elsevier",
    volume="46",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(08)60202-8",
    link="https://www.sciencedirect.com/science/article/pii/S0065245808602028",
    ID="Paulk19981",
    sciencedirect="1",
    placex="",
))

veryard1998a = DB(WorkUnrelated(
    1998, "Demanding change: How to remain in business despite IT",
    display="veryard",
    authors="Veryard, Richard",
    place=IEECD,
    pp="1/1-1/3",
    entrytype="inproceedings",
    number="312",
    note="cited By 0",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0031642518&partnerID=40&md5=ea169a56529d5260a5b77acdef316450",
    document_type="Conference Paper",
    source="Scopus",
    ID="Veryard19981/1",
    scopus="1",
))
