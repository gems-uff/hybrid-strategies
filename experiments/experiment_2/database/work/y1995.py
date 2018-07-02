# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

schwaber1995a = DB(WorkUnrelated(
    1995, "Scrum development process",
    display="schwaber",
    authors="Schwaber, K.",
    place=FAKE,
    pp="117-134",
    entrytype="article",
    note="cited By 162",
    ID="Schwaber1995117",
    placex="Proceedings of the 10th Annual ACM Conference on Object Oriented Programming Systems, Languages, and Applications (OOPSLA)",
))

stacey1995a = DB(WorkUnrelated(
    1995, "The science of complexity: An alternative perspective for strategic change processes",
    display="stacey",
    authors="Stacey, R.D.",
    place=FAKE,
    pp="477-495",
    entrytype="article",
    volume="16",
    number="6",
    doi="10.1002/smj.4250160606",
    note="cited By 457",
    ID="Stacey1995477",
    placex="Strategic Management Journal",
))

walsham1995a = DB(WorkUnrelated(
    1995, "Interpretive case studies in IS research: Nature and method",
    display="walsham",
    authors="Walsham, G.",
    place=FAKE,
    pp="74-81",
    entrytype="article",
    volume="4",
    number="2",
    doi="10.1057/ejis.1995.9",
    note="cited By 1677",
    ID="Walsham199574",
    placex="European Journal of Information Systems",
))

walsham1995b = DB(WorkUnrelated(
    1995, "The emergence of interpretivism in IS research",
    display="walsham b",
    authors="Walsham, G.",
    place=FAKE,
    pp="376-394",
    entrytype="article",
    volume="6",
    number="4",
    doi="10.1287/isre.6.4.376",
    note="cited By 512",
    ID="Walsham1995376",
    placex="Information Systems Research",
))
