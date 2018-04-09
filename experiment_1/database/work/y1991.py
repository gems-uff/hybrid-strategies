# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

argyris1991a = DB(WorkUnrelated(
    1991, "Participatory action research and action science compared: A commentary",
    display="argyris",
    authors="Argyris, C. and Schön, D.A.",
    place=FAKE,
    pp="85-96",
    entrytype="article",
    note="cited By 122",
    ID="Argyris199185",
    placex="Participatory Action Research",
))

avison1991a = DB(WorkUnrelated(
    1991, "Information systems development research. An exploration of ideas in practice",
    display="avison",
    authors="Avison, D.E. and Wood-Harper, A.T.",
    place=FAKE,
    pp="98-112",
    entrytype="article",
    volume="34",
    number="2",
    doi="10.1093/comjnl/34.2.98",
    note="cited By 64",
    ID="Avison199198",
    placex="Computer Journal",
))

humphrey1991a = DB(WorkUnrelated(
    1991, "Software Process Improvement at Hughes Aircraft",
    display="humphrey",
    authors="Humphrey, W.S. and Snyder, T.R. and Willis, R.R.",
    place=IEEES,
    pp="11-23",
    entrytype="article",
    volume="8",
    number="4",
    doi="10.1109/52.300031",
    note="cited By 150",
    ID="Humphrey199111",
    placex="IEEE Software",
))

montgomery1991a = DB(WorkUnrelated(
    1991, "Design and Analysis of Experiments",
    display="montgomery",
    authors="Montgomery, D.C.",
    place=FAKE,
    entrytype="article",
    note="cited By 19382",
    ID="Montgomery1991",
    placex="John Wiley & Sons, Singapore",
))

rombach1991a = DB(WorkUnrelated(
    1991, "MVP-L A Language for Process Modeling In-the-Large",
    display="rombach",
    authors="Rombach, H.D.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Rombach1991",
    placex="Inst. for Advanced Computer Studies, Univ. of Maryland",
))

rook1991a = DB(WorkUnrelated(
    1991, "27 - Project planning and control",
    display="rook",
    authors="Paul Rook",
    place=FAKE,
    pp="27/1 - 27/36",
    entrytype="incollection",
    editor="McDermid, John A",
    publisher="Butterworth-Heinemann",
    edition="",
    address="",
    isbn="978-0-7506-0813-8",
    doi="https://doi.org/10.1016/B978-0-7506-0813-8.50034-4",
    link="https://www.sciencedirect.com/science/article/pii/B9780750608138500344",
    ID="Rook199127/1",
    sciencedirect="1",
    placex="Software Engineer's Reference Book",
))
