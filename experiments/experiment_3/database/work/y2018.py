# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

cadavid2018a = DB(WorkUnrelated(
    2018, "International Journal of Modern Education and Computer Science (IJMECS)",
    display="cadavid",
    authors="Cadavid, Héctor F",
    place=FAKE,
    entrytype="article",
    ID="cadavidinternational",
    placex="",
))

vukovic2018a = DB(WorkUnrelated(
    2018, "A Business Software Testing Process-Based Model Design",
    display="vukovic",
    authors="Vukovic, Vuk and Djurkovic, Jovica and Trninic, Jelica",
    place=FAKE,
    pp="701--749",
    entrytype="article",
    volume="28",
    number="05",
    publisher="World Scientific",
    ID="vukovic2018business",
    placex="International Journal of Software Engineering and Knowledge Engineering",
))
