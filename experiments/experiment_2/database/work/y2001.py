# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

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
