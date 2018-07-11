# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

denison1991a = DB(WorkUnrelated(
    1991, "Research in organizational change and development",
    display="denison",
    authors="Denison, D.R. and Spreitzer, G.M.",
    place=FAKE,
    pp="1--21",
    entrytype="article",
    volume="5",
    note="cited By 2",
    ID="Denison19911",
    placex="Organizational culture and organizational development: A competing values approach",
))

gersick1991a = DB(WorkUnrelated(
    1991, "Revolutionary change theories: A multilevel exploration of the punctuated equilibrium paradigm",
    display="gersick",
    authors="Gersick, C.J.G.",
    place=FAKE,
    pp="10--36",
    entrytype="article",
    volume="16",
    number="1",
    note="cited By 1024",
    ID="Gersick199110",
    placex="Academy of Management Review",
))

schwaber1991a = DB(WorkUnrelated(
    1991, "The Scrum Guide: The Official Rulebook",
    display="schwaber",
    authors="Schwaber, K. and Sutherland, J.",
    place=TechReport,
    entrytype="article",
    note="cited By 1",
    ID="Schwaber1991",
    placex="Tech. Rep",
))
