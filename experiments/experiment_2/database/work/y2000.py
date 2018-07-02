# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

denny2000a = DB(WorkUnrelated(
    2000, "8.4. 1 One Engineering Process--Integrated!",
    display="denny",
    authors="Denny, Barbara and Bennett, Richard",
    place=FAKE,
    pp="557--564",
    entrytype="inproceedings",
    volume="10",
    number="1",
    organization="Wiley Online Library",
    ID="denny20008",
    wiley2016="1",
    placex="INCOSE International Symposium",
))

mathieu2000a = DB(WorkUnrelated(
    2000, "The influence of shared mental models on team process and performance",
    display="mathieu",
    authors="Mathieu, J.E. and Goodwin, G.F. and Heffner, T.S. and Salas, E. and Cannon-Bowers, J.A.",
    place=FAKE,
    pp="273-283",
    entrytype="article",
    volume="85",
    number="2",
    doi="10.1037/0021-9010.85.2.273",
    note="cited By 1103",
    ID="Mathieu2000273",
    placex="Journal of Applied Psychology",
))

rising2000a = DB(WorkUnrelated(
    2000, "Scrum software development process for small teams",
    display="rising",
    authors="Rising, L. and Janoff, N.S.",
    place=IEEES,
    pp="26-32",
    entrytype="article",
    volume="17",
    number="4",
    doi="10.1109/52.854065",
    note="cited By 222",
    ID="Rising200026",
    placex="IEEE Software",
))

robertson2000a = DB(WorkUnrelated(
    2000, "Volere requirements specification template",
    display="robertson",
    authors="Robertson, J. and Robertson, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 41",
    ID="Robertson2000",
    placex="Volere Requirements Specification Template",
))
