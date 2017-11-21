# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

maxwell2002a = DB(WorkOk(
    2002, "Applied statistics for software managers",
    display="maxwell",
    authors="Maxwell, Katrina",
    place=ASSM,
    entrytype="book",
    note="cited By 134",
    ID="Maxwell2002",
    cluster_id="17874005737648766452",
    publisher="Prentice Hall",
    scholar="http://scholar.google.com/scholar?cites=17874005737648766452&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

mendes2002a = DB(WorkOk(
    2002, "Comparison of Web size measures for predicting Web design and authoring effort",
    display="mendes",
    authors="Mendes, Emilia and Mosley, Nile and Counsell, Steve",
    place=IEEES,
    pp="86--92",
    entrytype="article",
    volume="149",
    number="3",
    doi="10.1049/ip-sen:20020337",
    note="cited By 48",
    ID="Mendes200286",
    cluster_id="2241920511533537917",
    publisher="IET",
    scholar="http://scholar.google.com/scholar?cites=2241920511533537917&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

wieczorek2002a = DB(WorkOk(
    2002, "How valuable is company-specific data compared to multi-company data for software cost estimation?",
    display="wieczorek",
    authors="Wieczorek, Isabella and Ruhe, Melanie",
    place=ISMS,
    pp="237--246",
    entrytype="inproceedings",
    volume="2002-January",
    doi="10.1109/METRIC.2002.1011342",
    art_number="1011342",
    note="cited By 29",
    ID="Wieczorek2002237",
    cluster_id="14969089639125944958",
    scholar="http://scholar.google.com/scholar?cites=14969089639125944958&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE",
    scholar_ok=True,
))
