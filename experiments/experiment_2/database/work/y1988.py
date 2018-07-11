# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

boehm1988a = DB(WorkUnrelated(
    1988, "A Spiral Model of Software Development and Enhancement",
    display="boehm",
    authors="Boehm, B.W.",
    place=C,
    pp="61--72",
    entrytype="article",
    volume="21",
    number="5",
    doi="10.1109/2.59",
    note="cited By 1710",
    ID="Boehm198861",
    placex="Computer",
))

ohno1988a = DB(WorkUnrelated(
    1988, "Toyota Production System: Beyond Large-Scale Production",
    display="ohno",
    authors="Ohno, T.",
    place=FAKE,
    entrytype="article",
    note="cited By 2344",
    ID="Ohno1988",
    placex="",
))

strauss1988a = DB(WorkUnrelated(
    1988, "THE ARTICULATION OF PROJECT WORK: AN ORGANIZATIONAL PROCESS",
    display="strauss",
    authors="Strauss, A.",
    place=FAKE,
    pp="163--178",
    entrytype="article",
    volume="29",
    number="2",
    doi="10.1111/j.1533-8525.1988.tb01249.x",
    note="cited By 190",
    ID="Strauss1988163",
    placex="Sociological Quarterly",
))
