# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

checkland1981a = DB(WorkUnrelated(
    1981, "Systems Thinking, Systems Practice",
    display="checkland",
    authors="Checkland, P.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Checkland1981",
    placex="John Wiley & Sons",
))

ieee1981a = DB(WorkUnrelated(
    1981, "Evaluation of a Software Requirements Document by Analysis of Change Data",
    display="ieee",
    authors="IEEE",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="IEEE1981",
    placex="IEEE Press",
))
