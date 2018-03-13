# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

akao1990a = DB(WorkOk(
    1990, "The book, QFD: Integrating customer requirements into product design",
    display="akao",
    authors="Akao, Y.",
    place=FAKE,
    placex="Productivity Press",
    entrytype="article",
    note="cited By 62",
    ID="Akao1990",
))

ram1990a = DB(WorkUnrelated(
    1990, "HyperIntelligence: The Next Frontier",
    display="ram",
    authors="Ram, Sudha and Carlson, David A.",
    place=FAKE,
    pp="311--321",
    entrytype="article",
    issue_date="March 1990",
    volume="33",
    number="3",
    month="mar",
    issn="0001-0782",
    ID="Ram:1990:HNF:77481.77484",
    acm="1",
    placex="Commun. ACM",
))

rifkin1990a = DB(WorkOk(
    1990, "Software engineering process group guide",
    display="rifkin",
    authors="Rifkin, S. and Fowler, P.",
    place=FAKE,
    placex="CMU/SEI-90-TR-24",
    entrytype="article",
    note="cited By 1",
    ID="Rifkin1990",
))
