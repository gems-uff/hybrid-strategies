# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

siegel1956a = DB(WorkUnrelated(
    1956, "Nonparametric Statistics",
    display="siegel",
    authors="Siegel, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 2622",
    ID="Siegel1956",
    placex="McGraw-Hill International, USA",
))
