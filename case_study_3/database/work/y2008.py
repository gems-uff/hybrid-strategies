# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mendes2008a = DB(WorkOk(
    2008, "Web Cost Estimation and Productivity Benchmarking",
    display="mendes",
    authors="Mendes, E.",
    place=IEEES,
    pp="194-222",
    entrytype="article",
    note="cited By 1",
    ID="Mendes2008194",
))

mendes2008b = DB(WorkOk(
    2008, "Cross-company vs. single-company web effort models using the Tukutuku database: An extended study",
    display="mendes b",
    authors="Mendes, E. and Di Martino, S. and Ferrucci, F. and Gravino, C.",
    place=JSS,
    pp="673-690",
    entrytype="article",
    volume="81",
    number="5",
    doi="10.1016/j.jss.2007.07.044",
    note="cited By 21",
    ID="Mendes2008673",
))
