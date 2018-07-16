# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

alliance2001a = DB(WorkUnrelated(
    2001, "Manifesto for Agile Software",
    display="alliance",
    authors="Agile Alliance",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="AgileAlliance2001",
    placex="",
))

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

beck2001b = DB(WorkUnrelated(
    2001, "Principles behind the Agile Manifesto",
    display="beck b",
    authors="Beck, K.",
    place=FAKE,
    entrytype="article",
    note="cited By 99",
    ID="Beck2001",
    placex="Principles behind the Agile Manifesto",
))

cockburn2001a = DB(WorkUnrelated(
    2001, "Agile software development: The people factor",
    display="cockburn",
    authors="Cockburn, A. and Highsmith, J.",
    place=C,
    pp="131--133",
    entrytype="article",
    volume="34",
    number="11",
    doi="10.1109/2.963450",
    note="cited By 418",
    ID="Cockburn2001131",
    placex="Computer",
))

cockburn2001b = DB(WorkUnrelated(
    2001, "Agile Software Development",
    display="cockburn b",
    authors="Cockburn, A.",
    place=FAKE,
    entrytype="article",
    note="cited By 1122",
    ID="Cockburn2001",
    placex="Addison-Wesley",
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
    pp="22--29",
    entrytype="article",
    volume="18",
    number="1",
    doi="10.1109/52.903160",
    note="cited By 77",
    ID="Ferré200122",
    placex="IEEE Software",
))

highsmith2001a = DB(WorkUnrelated(
    2001, "The agile manifesto",
    display="highsmith",
    authors="Highsmith, J. and Fowler, M.",
    place=FAKE,
    pp="29--30",
    entrytype="article",
    volume="9",
    number="8",
    note="cited By 27",
    ID="Highsmith200129",
    placex="Software Development Magazine",
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

knight2001a = DB(WorkUnrelated(
    2001, "Casper: Space Exploration through Continuous Planning",
    display="knight",
    authors="Knight, R. and Rabideau, G. and Chien, S. and Engelhardt, B. and Sherwood, R.",
    place=FAKE,
    pp="70--75",
    entrytype="article",
    volume="16",
    number="5",
    doi="10.1109/MIS.2001.956084",
    note="cited By 55",
    ID="Knight200170",
    placex="IEEE Intelligent Systems",
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
    planilha_springer2016="1",
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

mentzer2001a = DB(WorkUnrelated(
    2001, "Defining supply chain management",
    display="mentzer",
    authors="Mentzer, J.T. and Dewitt, W. and Keebler, J.S. and Min, S. and Nix, N.W. and Smith, C.D. and Zacharia, Z.G.",
    place=FAKE,
    pp="1--25",
    entrytype="article",
    volume="22",
    number="2",
    note="cited By 1407",
    ID="Mentzer20011",
    placex="Journal of Business Logistics",
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
    planilha_wiley2016="1",
    placex="INCOSE International Symposium",
))

sutherland2001a = DB(WorkUnrelated(
    2001, "Agile Can Scale: Inventing and Reinventing SCRUM in Five Companies",
    display="sutherland",
    authors="Sutherland, J.",
    place=FAKE,
    pp="5--11",
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
    pp="125--138",
    entrytype="article",
    note="cited By 35",
    ID="DeWin2001125",
    placex="Advances in Network and Distributed Systems Security",
))
