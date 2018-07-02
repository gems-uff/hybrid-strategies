# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

beck2001a = DB(WorkUnrelated(
    2001, "Manifesto for Agile Software Development",
    display="beck",
    authors="Beck, K.",
    place=FAKE,
    entrytype="article",
    note="cited By 938",
    ID="Beck2001",
    placex="Manifesto for Agile Software Development",
))

eoyang2001a = DB(WorkUnrelated(
    2001, "Conditions for self-Organisation in human systems",
    display="eoyang",
    authors="Eoyang, G.",
    place=FAKE,
    entrytype="article",
    note="cited By 20",
    ID="Eoyang2001",
    placex="Conditions for Self-Organizing in Human Systems",
))

ferré2001a = DB(WorkUnrelated(
    2001, "Usability basics for software developers",
    display="ferré",
    authors="Ferré, X. and Juristo, N. and Windl, H. and Constantine, L.",
    place=IEEES,
    pp="22-29",
    entrytype="article",
    volume="18",
    number="1",
    doi="10.1109/52.903160",
    note="cited By 77",
    ID="Ferré200122",
    placex="IEEE Software",
))

hoyle2001a = DB(WorkUnrelated(
    2001, "ISO 9000 Quality Systems Handbook",
    display="hoyle",
    authors="Hoyle, D.",
    place=FAKE,
    entrytype="article",
    note="cited By 200",
    ID="Hoyle2001",
    placex="ISO",
))

kerth2001a = DB(WorkUnrelated(
    2001, "Project Retrospectives: A Handbook for Team Reviews",
    display="kerth",
    authors="Kerth, N.L.",
    place=FAKE,
    entrytype="article",
    note="cited By 116",
    ID="Kerth2001",
    placex="",
))

kroemer2001a = DB(WorkUnrelated(
    2001, "Keyboards and keying An annotated bibliography of the literature from 1878 to 1999",
    display="kroemer",
    authors="Kroemer, Karl HE",
    place=FAKE,
    entrytype="misc",
    publisher="Springer",
    ID="kroemer2001keyboards",
    cluster_id="830220169728379893",
    scholar="http://scholar.google.com/scholar?cites=830220169728379893&as_sdt=2005&sciodt=0,5&hl=en",
    springer2016="1",
))

manifesto2001a = DB(WorkUnrelated(
    2001, "Agile Alliance: Manifesto for Agile Software",
    display="manifesto",
    authors="agile manifesto",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="agile2001agile",
    placex="accessed site",
))

olson2001a = DB(WorkUnrelated(
    2001, "Facilitating Organization Change: Lessons from Complexity Science",
    display="olson",
    authors="Olson, E.E. and Eoyang, G.H.",
    place=FAKE,
    entrytype="article",
    note="cited By 135",
    ID="Olson2001",
    placex="",
))

ring2001a = DB(WorkUnrelated(
    2001, "3.7. 2 Discovering the Architecture for Product X",
    display="ring",
    authors="Ring, Jack",
    place=FAKE,
    pp="1053--1060",
    entrytype="inproceedings",
    volume="11",
    number="1",
    organization="Wiley Online Library",
    ID="ring20013",
    wiley2016="1",
    placex="INCOSE International Symposium",
))

sutherland2001a = DB(WorkUnrelated(
    2001, "Agile Can Scale: Inventing and Reinventing SCRUM in Five Companies",
    display="sutherland",
    authors="Sutherland, J.",
    place=FAKE,
    pp="5-11",
    entrytype="article",
    volume="14",
    number="12",
    note="cited By 42",
    ID="Sutherland20015",
    placex="Cutter IT Journal",
))

win2001a = DB(WorkUnrelated(
    2001, "Security through aspect-oriented programming",
    display="win",
    authors="De Win, B. and Vanhaute, B. and De Decker, B.",
    place=FAKE,
    pp="125-138",
    entrytype="article",
    note="cited By 35",
    ID="DeWin2001125",
    placex="Advances in Network and Distributed Systems Security",
))
