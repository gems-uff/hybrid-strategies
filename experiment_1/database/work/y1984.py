# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1984a = DB(WorkUnrelated(
    1984, "A Methodology for Collecting Valid Software Engineering Data",
    display="basili",
    authors="Basili, V.R. and Weiss, D.M.",
    place=ToSE,
    pp="728-738",
    entrytype="article",
    volume="SE-10",
    number="6",
    doi="10.1109/TSE.1984.5010301",
    note="cited By 491",
    ID="Basili1984728",
))

lamb1984a = DB(WorkUnrelated(
    1984, "Competitive Strategic Management",
    display="lamb",
    authors="Lamb, R.B.",
    place=FAKE,
    entrytype="article",
    note="cited By 34",
    ID="Lamb1984",
    placex="Englewood Cliffs: Prentice-Hall",
))
