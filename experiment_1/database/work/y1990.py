# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

akao1990a = DB(WorkUnrelated(
    1990, "The book, QFD: Integrating customer requirements into product design",
    display="akao",
    authors="Akao, Y.",
    place=FAKE,
    placex="Productivity Press",
    entrytype="article",
    note="cited By 62",
    ID="Akao1990",
))

checkland1990a = DB(WorkUnrelated(
    1990, "Soft Systems Methodology in Action",
    display="checkland",
    authors="Checkland, P. and J. Scholes",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Checkland1990",
    placex="John Wiley & Sons",
))

hammer1990a = DB(WorkUnrelated(
    1990, "Reengineering Work: Don't Automate",
    display="hammer",
    authors="Hammer, M.,",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Hammer1990",
    placex="Obliterate, Harvard Business Review",
))

mcnair1990a = DB(WorkUnrelated(
    1990, "Do financial and nonfinancial performance measures have to agree?",
    display="mcnair",
    authors="McNair, C.J. and Lynch, R.L. and Cross, K.F.",
    place=FAKE,
    pp="28-36",
    entrytype="article",
    number="5",
    note="cited By 104",
    ID="McNair199028",
    placex="Management Accounting",
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

rifkin1990a = DB(WorkUnrelated(
    1990, "Software engineering process group guide",
    display="rifkin",
    authors="Rifkin, S. and Fowler, P.",
    place=FAKE,
    placex="CMU/SEI-90-TR-24",
    entrytype="article",
    note="cited By 1",
    ID="Rifkin1990",
))
