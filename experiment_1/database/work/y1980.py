# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

lientz1980a = DB(WorkUnrelated(
    1980, "Software Maintenance Management",
    display="lientz",
    authors="Lientz, B.P., Swanson, E.B.",
    place=FAKE,
    placex="Addison-Wesley,",
))

saaty1980a = DB(WorkUnrelated(
    1980, "The Analytic Hierarchy Process",
    display="saaty",
    authors="Saaty, T.L.",
    place=FAKE,
    entrytype="article",
    note="cited By 16737",
    ID="Saaty1980",
    placex="McGraw-Hill, New York",
))
