# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

curtis1992a = DB(WorkUnrelated(
    1992, "Process modeling",
    display="curtis",
    authors="Curtis, B., Kellner, M., Over, J.:",
    place=FAKE,
    placex="ACM 35, 75–90",
))

floyd1992a = DB(WorkUnrelated(
    1992, "Software development as reality construction",
    display="floyd",
    authors="Floyd, Christiane",
    place=FAKE,
    pp="86--100",
    entrytype="incollection",
    publisher="Springer",
    ID="floyd1992software",
    scholar2016="1",
    placex="Software development and reality construction",
))
