# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

david1988a = DB(WorkUnrelated(
    1988, "The Method of Paired Comparisons",
    display="david",
    authors="David, H.A.",
    place=FAKE,
    entrytype="article",
    note="cited By 791",
    ID="David1988",
    placex="Lubrecht & Cramer, Limited",
))

humphrey1988a = DB(WorkUnrelated(
    1988, "Characterizing the Software Process",
    display="humphrey",
    authors="Humphrey, W.S.,",
    place=IEEES,
    entrytype="article",
    note="cited By 1",
    ID="Humphrey1988",
    placex="IEEE Software, Vol. 5, No. 2, Pp. 73-79",
))
