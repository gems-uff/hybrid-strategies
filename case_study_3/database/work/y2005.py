# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

mendes2005a = DB(WorkOk(
    2005, "The need for web engineering: An introduction",
    display="mendes",
    authors="Mendes, Emilia and Mosley, Nile and Counsell, Steve",
    place=WE,
    entrytype="article",
    note="cited By 1",
    ID="Mendes2005",
    cluster_id="17676254389768766098",
    publisher="Springer",
    pp="1--27",
    scholar="http://scholar.google.com/scholar?cites=17676254389768766098&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

mendes2005b = DB(WorkOk(
    2005, "Investigating Web size metrics for early Web cost estimation",
    display="mendes b",
    authors="Mendes, Emilia and Mosley, Nile and Counsell, Steve",
    place=JSS,
    pp="157--172",
    entrytype="article",
    volume="77",
    number="2",
    doi="10.1016/j.jss.2004.08.034",
    note="cited By 58",
    ID="Mendes2005157",
    cluster_id="17043276553242750479",
    publisher="Elsevier",
    scholar="http://scholar.google.com/scholar?cites=17043276553242750479&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
