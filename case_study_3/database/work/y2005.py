# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mendes2005a = DB(WorkOk(
    2005, "The Need for Web Engineering: An Introduction, Web Engineering:  An  Introduction.",
    display="mendes",
    authors="Mendes, E. and Mosley, N. and Counsell, S.",
    place=WE,
    entrytype="article",
    note="cited By 1",
    ID="Mendes2005",
))

mendes2005b = DB(WorkOk(
    2005, "Investigating Web size metrics for early Web cost estimation",
    display="mendes b",
    authors="Mendes, E. and Mosley, N. and Counsell, S.",
    place=JSS,
    pp="157-172",
    entrytype="article",
    volume="77",
    number="2",
    doi="10.1016/j.jss.2004.08.034",
    note="cited By 58",
    ID="Mendes2005157",
))
