# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mendes2014a = DB(WorkUnrelated(
    2014, "Cross-vs. within-company cost estimation studies revisited: an extended systematic review",
    display="mendes",
    authors="Mendes, Emilia and Kalinowski, Marcos and Martins, Daves and Ferrucci, Filomena and Sarro, Federica",
    place=EASE,
    pp="12",
    entrytype="inproceedings",
    organization="ACM",
    ID="mendes2014cross",
    cluster_id="9119025274604461618",
    scholar="http://scholar.google.com/scholar?cites=9119025274604461618&as_sdt=2005&sciodt=0,5&hl=en",
))

menzies2014a = DB(WorkUnrelated(
    2014, "Sharing data and models in software engineering",
    display="menzies",
    authors="Menzies, Tim and Kocaguneli, Ekrem and Turhan, Burak and Minku, Leandro and Peters, Fayola",
    place=Book,
    entrytype="book",
    publisher="Morgan Kaufmann",
    ID="menzies2014sharing",
    cluster_id="13951839833884318073",
    scholar="http://scholar.google.com/scholar?cites=13951839833884318073&as_sdt=2005&sciodt=0,5&hl=en",
))

turhan2014a = DB(WorkUnrelated(
    2014, "A comparison of cross-versus single-company effort prediction models for web projects",
    display="turhan",
    authors="Turhan, Burak and Mendes, Emilia",
    place=SEAA,
    pp="285--292",
    entrytype="inproceedings",
    organization="IEEE",
    ID="turhan2014comparison",
    cluster_id="5147500092362979043",
    scholar="http://scholar.google.com/scholar?cites=5147500092362979043&as_sdt=2005&sciodt=0,5&hl=en",
))
