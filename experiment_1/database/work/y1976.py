# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

fagan1976a = DB(WorkUnrelated(
    1976, "DESIGN AND CODE INSPECTIONS TO REDUCE ERRORS IN PROGRAM DEVELOPMENT",
    display="fagan",
    authors="Fagan, Michael E.",
    place=FAKE,
    pp="182--211",
    entrytype="article",
    volume="15",
    number="3",
    doi="10.1147/sj.153.0182",
    note="cited By 766",
    ID="Fagan1976182",
    placex="IBM Systems Journal",
))

fagan1976b = DB(WorkUnrelated(
    1976, "Design and code inspections to reduce errors in program development",
    display="fagan b",
    authors="M Fagan",
    place=FAKE,
    other1="15(3):182211",
    placex="IBM Syst J",
))

mccabe1976a = DB(WorkUnrelated(
    1976, "A Complexity Measure",
    display="mccabe",
    authors="Mccabe, T.J.",
    place=ToSE,
    pp="308--320",
    entrytype="article",
    volume="SE--2",
    number="4",
    doi="10.1109/TSE.1976.233837",
    note="cited By 2535",
    ID="Mccabe1976308",
    placex="IEEE Transactions on Software Engineering",
))
