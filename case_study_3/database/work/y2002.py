# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

maxwell2002a = DB(WorkOk(
    2002, "Applied Statistics for Software Managers",
    display="maxwell",
    authors="Maxwell, K.",
    place=ASSM,
    entrytype="article",
    note="cited By 134",
    ID="Maxwell2002",
))

mendes2002a = DB(WorkOk(
    2002, "Comparison of Web size measures for predicting Web design and authoring effort",
    display="mendes",
    authors="Mendes, E. and Mosley, N. and Counsell, S.",
    place=IEEES,
    pp="86-92",
    entrytype="article",
    volume="149",
    number="3",
    doi="10.1049/ip-sen:20020337",
    note="cited By 48",
    ID="Mendes200286",
))

wieczorek2002a = DB(WorkOk(
    2002, "How valuable is company-specific data compared to multi-company data for software cost estimation?",
    display="wieczorek",
    authors="Wieczorek, I. and Ruhe, M.",
    place=ISMS,
    pp="237-246",
    entrytype="inproceedings",
    volume="2002-January",
    doi="10.1109/METRIC.2002.1011342",
    art_number="1011342",
    note="cited By 29",
    ID="Wieczorek2002237",
))
