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
