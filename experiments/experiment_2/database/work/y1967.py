# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

glaser1967a = DB(WorkUnrelated(
    1967, "The Discovery of Grounded Theory: Strategies for Qualitative Research",
    display="glaser",
    authors="Glaser, B.G. and Strauss, A.L.",
    place=FAKE,
    entrytype="article",
    note="cited By 37985",
    ID="Glaser1967",
    placex="",
))

glaser1967b = DB(WorkUnrelated(
    1967, "The Discovery of Grounded Theory",
    display="glaser b",
    authors="Glaser, B.G. and Strauss, A.L.",
    place=FAKE,
    entrytype="article",
    volume="20",
    number="2",
    note="cited By 20",
    ID="Glaser1967",
    placex="Aldine",
))
