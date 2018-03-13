# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

humphrey1989a = DB(WorkOk(
    1989, "Managing the software process",
    display="humphrey",
    authors="Humphrey, W.S.",
    place=FAKE,
    placex="Managing the Software Process",
    entrytype="article",
    note="cited By 1289",
    ID="Humphrey1989",
))

marques1989a = DB(WorkUnrelated(
    1989, "Extending the Operating System to Support an Object-oriented Environment",
    display="marques",
    authors="Marques, J. A. and Guedes, P.",
    place=FAKE,
    pp="113--122",
    entrytype="article",
    issue_date="Oct. 1989",
    volume="24",
    number="10",
    month="sep",
    issn="0362-1340",
    ID="Marques:1989:EOS:74878.74890",
    acm="1",
    placex="SIGPLAN Not.",
))
