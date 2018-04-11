# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1981a = DB(WorkUnrelated(
    1981, "Data collection, validation, and analysis. In: Tutorial on models and metrics for software management and engineering,",
    display="basili",
    authors="VR Basili",
    place=FAKE,
    other1="pp 310313",
    placex="IEEE Catalog no. EHO-167-7,",
))

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
