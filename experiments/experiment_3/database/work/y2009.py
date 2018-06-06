# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

gazel2009a = DB(WorkSnowball(
    2009, "A CMMI Ontology for An Ontology-Based Software Process Assessment Tool",
    display="gazel",
    authors="Gazel, Sema and Tarhan, Ay{ç}a and Sezer, Ebru",
    place=FAKE,
    entrytype="inproceedings",
    volume="9",
    ID="gazel2009cmmi",
    cluster_id="6833681226443800582",
    scholar="http://scholar.google.com/scholar?cites=6833681226443800582&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="11",
    final_selected="1",
    scopus2016="1",
    placex="proceedings of the 16th EuroSPI2 Conference",
))

lee2009a = DB(WorkSnowball(
    2009, "Ontology-based computational intelligent multi-agent and its application to CMMI assessment",
    display="lee",
    authors="Lee, Chang-Shing and Wang, Mei-Hui",
    place=FAKE,
    pp="203--219",
    entrytype="article",
    volume="30",
    number="3",
    publisher="Springer",
    ID="lee2009ontology",
    cluster_id="15934008590346441714",
    scholar="http://scholar.google.com/scholar?cites=15934008590346441714&as_sdt=2005&sciodt=0,5&hl=en",
    selected_snowballing="1",
    selected_order="13",
    final_selected="1",    
    placex="Applied Intelligence",
))
