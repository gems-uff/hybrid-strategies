# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kitchenham2007a = DB(WorkOk(
    2007, "Cross versus within-company cost estimation studies: A systematic review",
    display="kitchenham",
    authors="Kitchenham, B.A. and Mendes, E. and Travassos, G.H.",
    place=ToSE,
    pp="316-329",
    entrytype="article",
    volume="33",
    number="5",
    doi="10.1109/TSE.2007.1001",
    note="cited By 175",
    ID="Kitchenham2007316",
))

mendes2007a = DB(WorkOk(
    2007, "Effort estimation: How valuable is it for a web company to use a cross-company data set, compared to using its own single-company data set?",
    display="mendes",
    authors="Mendes, E. and Di Martino, S. and Ferrucci, F. and Gravino, C.",
    place=WWW,
    pp="963-972",
    entrytype="inproceedings",
    doi="10.1145/1242572.1242702",
    note="cited By 19",
    ID="Mendes2007963",
))
