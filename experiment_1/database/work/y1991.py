# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

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
