# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

baskerville1999a = DB(WorkUnrelated(
    1999, "Investigating information systems with action research",
    display="baskerville",
    authors="Baskerville, R.",
    place=FAKE,
    pp="1--32",
    entrytype="article",
    volume="2",
    number="19",
    note="cited By 670",
    ID="Baskerville19991",
    placex="Communications of the Association for Information Systems",
))

weich1999a = DB(WorkUnrelated(
    1999, "Organizational change and development",
    display="weich",
    authors="Weich, K.E. and Quinn, R.E.",
    place=FAKE,
    pp="361--386",
    entrytype="article",
    volume="50",
    note="cited By 963",
    ID="Weich1999361",
    placex="Annual Review of Psychology",
))

yusuf1999a = DB(WorkUnrelated(
    1999, "Agile manufacturing:: The drivers, concepts and attributes",
    display="yusuf",
    authors="Yusuf, Yahaya Y and Sarhadi, Mansoor and Gunasekaran, Angappa",
    place=FAKE,
    pp="33--43",
    entrytype="article",
    volume="62",
    number="1-2",
    publisher="Elsevier",
    ID="yusuf1999agile",
    scholar2016="1",
    placex="International Journal of production economics",
))
