# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

moore1966a = DB(WorkUnrelated(
    1966, "Interval Analysis",
    display="moore",
    authors="Moore, R.E.",
    place=FAKE,
    entrytype="article",
    note="cited By 3260",
    ID="Moore1966",
    placex="Prentice-Hall",
))
