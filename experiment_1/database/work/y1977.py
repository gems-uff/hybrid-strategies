# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bardin1977a = DB(WorkUnrelated(
    1977, "Content Analysis",
    display="bardin",
    authors="Bardin, L.",
    place=FAKE,
    entrytype="article",
    note="cited By 65",
    ID="Bardin1977",
    placex="Lisboa. Edições",
))
