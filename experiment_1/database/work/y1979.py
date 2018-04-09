# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

dijkstra1979a = DB(WorkUnrelated(
    1979, "Go to statement considered harmful",
    display="dijkstra",
    authors="Dijkstra, E.",
    place=FAKE,
    pp="27-33",
    entrytype="article",
    note="cited By 3",
    ID="Dijkstra197927",
    placex="Classics in Software Engineering",
))

mullery1979a = DB(WorkUnrelated(
    1979, "CORE - A Method for Controlled Requirements Specification",
    display="mullery",
    authors="Mullery, G.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Mullery1979",
    placex="Proc. Fourth Int'l Conf. Software Eng., Pp. 126-35, IEEE CS Press",
))

porter1979a = DB(WorkUnrelated(
    1979, "How competitive forces shape strategy",
    display="porter",
    authors="Porter, M. E.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Porter1979",
    placex="Harvard Business Review",
))
