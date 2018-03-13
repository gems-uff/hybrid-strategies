# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

haikala1992a = DB(WorkUnrelated(
    1992, "(Continuing) education of software professionals",
    display="haikala",
    authors="Haikala, Ilkka J. and Marijarvi, Jukka",
    place=FAKE,
    pp="180--193",
    entrytype="inproceedings",
    editor="Sledge, Carol",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/3-540-55963-9_50",
    springer="1",
    placex="Software Engineering Education",
))

kaplan1992a = DB(WorkOk(
    1992, "The balanced scorecard--measures that drive performance.",
    display="kaplan",
    authors="Kaplan, R.S. and Norton, D.P.",
    pp="71-79",
    place=FAKE,
    placex="Harvard Business Review",
    entrytype="article",
    volume="70",
    number="1",
    note="cited By 5432",
    ID="Kaplan199271",
))
