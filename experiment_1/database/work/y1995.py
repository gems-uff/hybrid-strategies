# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bukowski1995a = DB(WorkUnrelated(
    1995, "Object Associations: A Simple and Practical Approach to Virtual 3D Manipulation",
    display="bukowski",
    authors="Bukowski, Richard W. and Séquin, Carlo H.",
    place=FAKE,
    pp="131--ff.",
    entrytype="inproceedings",
    series="I3D '95",
    isbn="0-89791-736-7",
    location="Monterey, California, USA",
    ID="Bukowski:1995:OAS:199404.199427",
    acm="1",
    placex="Proceedings of the 1995 Symposium on Interactive 3D Graphics",
))

teufel1995a = DB(WorkUnrelated(
    1995, "Bridging Information Technology and Business&Mdash;Some Modelling Aspects",
    display="teufel",
    authors="Teufel, Stephanie and Teufel, Bernd",
    place=FAKE,
    pp="13--17",
    entrytype="article",
    issue_date="Aug. 1995",
    volume="16",
    number="1",
    month="aug",
    issn="0894-0819",
    ID="Teufel:1995:BIT:209891.209895",
    acm="1",
    placex="SIGOIS Bull.",
))
