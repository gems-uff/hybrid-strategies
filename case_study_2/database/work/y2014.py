# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

wohlin2014a = DB(WorkSnowball(
    2014, "Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering",
    display="wohlin",
    authors="C. Wohlin",
    place=EASE,
    other1="321-330",
    scholar	= "http://scholar.google.com/scholar?cites=8727281463705144333&as_sdt=2005&sciodt=0,5&hl=en",
    dglibrary = "Scopus",
    references = 21, 
    citations = 200,
    snowball=datetime(2017, 9, 18),
    scopus="1",
    acm="1",
))

wohlin2014b = DB(WorkOk(
    2014, "Writing for synthesis of evidence in empirical software engineering",
    display="wohlin b",
    authors="Wohlin, Claes",
    pp="46",
    place=ESEM,
    entrytype="inproceedings",
    organization="ACM",
    ID="wohlin2014writing",
    cluster_id="8450698508367773593",
    scholar="http://scholar.google.com/scholar?cites=8450698508367773593&as_sdt=2005&sciodt=0,5&hl=en",
))
