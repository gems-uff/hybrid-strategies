# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bazerman1994a = DB(WorkUnrelated(
    1994, "Judgment in Managerial Decision Making",
    display="bazerman",
    authors="Bazerman, M.H.",
    place=FAKE,
    entrytype="article",
    note="cited By 1305",
    ID="Bazerman1994",
    placex="John Wiley",
))

krueger1994a = DB(WorkUnrelated(
    1994, "Focus Groups: A Practical Guide for Applied Research",
    display="krueger",
    authors="Krueger, R.A.",
    place=SAGE,
    entrytype="article",
    note="cited By 8482",
    ID="Krueger1994",
    placex="SAGE",
))

miles1994a = DB(WorkUnrelated(
    1994, "Qualitative Data Analysis",
    display="miles",
    authors="Miles, M.B. and Huberman, A.M.",
    place=SAGE,
    entrytype="article",
    note="cited By 32457",
    ID="Miles1994",
    placex="SAGE",
))

romanelli1994a = DB(WorkUnrelated(
    1994, "Organizational transformation as punctuated equilibrium: An empirical test",
    display="romanelli",
    authors="Romanelli, E. and Tushman, M.L.",
    place=FAKE,
    pp="1141--1166",
    entrytype="article",
    volume="37",
    number="5",
    note="cited By 659",
    ID="Romanelli19941141",
    placex="Academy of Management Journal",
))

yin1994a = DB(WorkUnrelated(
    1994, "Case Study Research: Design and Methods",
    display="yin",
    authors="Yin, R.K.",
    place=SAGE,
    entrytype="article",
    note="cited By 49302",
    ID="Yin1994",
    placex="SAGE",
))
