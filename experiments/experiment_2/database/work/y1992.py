# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

eisenhardt1992a = DB(WorkUnrelated(
    1992, "Strategic decision making",
    display="eisenhardt",
    authors="Eisenhardt, K.M. and Zbaracki, M.J.",
    place=FAKE,
    pp="17-37",
    entrytype="article",
    volume="13",
    number="2 S",
    doi="10.1002/smj.4250130904",
    note="cited By 640",
    ID="Eisenhardt199217",
    placex="Strategic Management Journal",
))

glaser1992a = DB(WorkUnrelated(
    1992, "Basics of grounded theory analysis",
    display="glaser",
    authors="Glaser, B.G.",
    place=FAKE,
    entrytype="article",
    note="cited By 2455",
    ID="Glaser1992",
    placex="Basics of Grounded Theory Analysis",
))
