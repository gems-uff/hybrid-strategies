# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

boehm1981a = DB(WorkUnrelated(
    1981, "Software Engineering Economics",
    display="boehm",
    authors="Boehm, B.W.",
    place=FAKE,
    entrytype="article",
    note="cited By 3420",
    ID="Boehm1981",
    placex="Prentice Hall",
))

doran1981a = DB(WorkUnrelated(
    1981, "There's a S.M.A.R.T. way to write management's goals and objectives",
    display="doran",
    authors="Doran, G.T.",
    place=FAKE,
    pp="35--36",
    entrytype="article",
    volume="70",
    number="11",
    note="cited By 415",
    ID="Doran198135",
    placex="Management Review",
))

yin1981a = DB(WorkUnrelated(
    1981, "The case study crisis: some answers",
    display="yin",
    authors="R.K. Yin",
    place=FAKE,
    entrytype="article",
    ID="Yin1981",
    placex="Adm. Sci. Q.",
))
