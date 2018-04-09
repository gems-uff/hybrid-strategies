# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1989a = DB(WorkUnrelated(
    1989, "Software development: A paradigm for the future",
    display="basili",
    authors="Basili, Victor R.",
    place=FAKE,
    pp="471-485",
    entrytype="conference",
    note="cited By 40",
    ID="Basili1989471",
    placex="Proceedings - IEEE Computer Society's International Computer Software & Applications Conference",
))

humphrey1989a = DB(WorkUnrelated(
    1989, "Managing the software process",
    display="humphrey",
    authors="Humphrey, W.S.",
    place=FAKE,
    placex="Managing the Software Process",
    entrytype="article",
    note="cited By 1289",
    ID="Humphrey1989",
))

humphrey1989b = DB(WorkUnrelated(
    1989, "The book",
    display="humphrey b",
    authors="Humphrey, W.S.",
    place=FAKE,
    placex="Managing the Software Process",
    entrytype="article",
    note="cited By 1",
    ID="Humphrey1989",
))

itil1989a = DB(WorkUnrelated(
    1989, "ITIL - The Information Technology Infrastructure Library",
    display="itil",
    authors="itil",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="itil1989",
    placex="HMSO",
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
