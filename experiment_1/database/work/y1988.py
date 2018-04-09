# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1988a = DB(WorkUnrelated(
    1988, "The TAME Project: Towards Improvement-Oriented Software Environments",
    display="basili",
    authors="Basili, V.R. and Dieter Rombach, H.",
    place=ToSE,
    pp="758-773",
    entrytype="article",
    volume="14",
    number="6",
    doi="10.1109/32.6156",
    note="cited By 630",
    ID="Basili1988758",
    placex="IEEE Transactions on Software Engineering",
))

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
