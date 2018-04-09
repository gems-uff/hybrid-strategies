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

akao1990b = DB(WorkUnrelated(
    1990, "QFD: Integrating Customer Requirements into Product Design",
    display="akao b",
    authors="Akao, Y.",
    place=FAKE,
    entrytype="article",
    note="cited By 62",
    ID="Akao1990",
    placex="Productivity Press",
))

akao1990c = DB(WorkUnrelated(
    1990, "Quality Function Deployment: Integrating Customer Requirements into Product Design",
    display="akao c",
    authors="Akao, Y.",
    place=FAKE,
    entrytype="article",
    note="cited By 1475",
    ID="Akao1990",
    placex="Productivity Press, Cambridge, MA",
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

daskalaivtonakis1990a = DB(WorkUnrelated(
    1990, "A method for assessing software measurement technology",
    display="daskalaivtonakis",
    authors="Daskalaivtonakis, M.K. and Basili, V.R.",
    place=FAKE,
    pp="27-40",
    entrytype="article",
    volume="3",
    number="1",
    doi="10.1080/08982119008918835",
    note="cited By 15",
    ID="Daskalaivtonakis199027",
    placex="Quality Engineering",
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

knapp1990a = DB(WorkUnrelated(
    1990, "Treating ordinal scales as interval scales: an attempt to resolve the controversy",
    display="knapp",
    authors="Knapp, Thomas R",
    place=FAKE,
    pp="121--123",
    entrytype="article",
    volume="39",
    number="2",
    ID="knapp1990treating",
    placex="Nursing research",
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

senge1990a = DB(WorkUnrelated(
    1990, "The Fifth Discipline: The Art and Practice of the Learning Organization",
    display="senge",
    authors="Senge, P.M.",
    place=FAKE,
    entrytype="article",
    note="cited By 12010",
    ID="Senge1990",
    placex="London: Random House",
))
