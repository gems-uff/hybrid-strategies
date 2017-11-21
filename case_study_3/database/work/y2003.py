# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mendes2003a = DB(WorkOk(
    2003, "Investigating early web size measures for web cost estimation",
    display="mendes",
    authors="Mendes, E. and Mosley, N. and Counsell, S.",
    place=EASE,
    pp="1-22",
    entrytype="article",
    note="cited By 26",
    ID="Mendes20031",
))

mendes2003b = DB(WorkOk(
    2003, "A replicated assessment of the use of adaptation rules to improve Web cost estimation",
    display="mendes b",
    authors="Mendes, E. and Mosley, N. and Counsell, S.",
    place=ESEM,
    pp="100-109",
    entrytype="inproceedings",
    doi="10.1109/ISESE.2003.1237969",
    art_number="1237969",
    note="cited By 36",
    ID="Mendes2003100",
))
