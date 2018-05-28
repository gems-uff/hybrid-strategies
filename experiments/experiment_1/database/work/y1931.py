# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

shewhart1931a = DB(WorkUnrelated(
    1931, "Economic Control of Quality of Manufactured Product",
    display="shewhart",
    authors="Shewhart, W.A.",
    place=FAKE,
    entrytype="article",
    note="cited By 2168",
    ID="Shewhart1931",
    placex="D.Van Nostrand Company",
))
