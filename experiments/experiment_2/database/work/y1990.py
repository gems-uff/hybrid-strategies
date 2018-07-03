# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

locke1990a = DB(WorkUnrelated(
    1990, "A theory of goal setting and task performance",
    display="locke",
    authors="Locke, E.A. and Latham, G.P.",
    place=FAKE,
    entrytype="article",
    note="cited By 4116",
    ID="Locke1990",
    placex="A Theory of Goal Setting and Task Performance",
))

malone1990a = DB(WorkUnrelated(
    1990, "What is coordination theory and how can it help design cooperative work systems?",
    display="malone",
    authors="Malone, T.W. and Crowston, K.",
    place=FAKE,
    pp="357-370",
    entrytype="article",
    note="cited By 341",
    ID="Malone1990357",
    placex="CSCW Proceedings",
))
