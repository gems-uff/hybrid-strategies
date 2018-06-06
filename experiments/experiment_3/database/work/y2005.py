# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

liao2005a = DB(WorkSnowball(
    2005, "A software process ontology and its application",
    display="liao",
    authors="Liao, Li and Qu, Yuzhong and Leung, H",
    place=FAKE,
    pp="6--10",
    entrytype="inproceedings",
    ID="liao2005software",
    cluster_id="14132108578074358916",
    scholar="http://scholar.google.com/scholar?cites=14132108578074358916&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="1",
    final_selected="1",
    gs2016="1",
    placex="ISWC2005 Workshop on Semantic Web Enabled Software Engineering",
))

liao2005b = DB(WorkSnowball(
    2005, "An Ontology-based Approach to Express Software Processes",
    display="liao b",
    authors="Liao, Li and Qu, Yuzhong and Leung, H",
    place=FAKE,
    entrytype="misc",
    publisher="ISFST",
    ID="liao2005ontology",
    cluster_id="17812701283033522556",
    scholar="http://scholar.google.com/scholar?cites=17812701283033522556&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="8",
    final_selected="1",
    gs2016="1",
    placex="",
))
