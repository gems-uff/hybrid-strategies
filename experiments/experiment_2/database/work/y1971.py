# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

rawls1971a = DB(WorkUnrelated(
    1971, "A Theory of Justice",
    display="rawls",
    authors="Rawls, J.",
    place=FAKE,
    entrytype="article",
    note="cited By 21405",
    ID="Rawls1971",
    placex="Harvard University Press",
))
