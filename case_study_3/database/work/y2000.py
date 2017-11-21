# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

briand2000a = DB(WorkOk(
    2000, "Replicated assessment and comparison of common software cost modeling techniques",
    display="briand",
    authors="Briand, Lionel C. and Langley, Tristen and Wieczorek, Isabella",
    place=ICSE,
    pp="377-386",
    entrytype="inproceedings",
    note="cited By 137",
    ID="Briand2000377",
))

christodoulou2000a = DB(Work(
    2000, "WWW2000: The developer's view and a practitioner's approach to web engineering",
    display="christodoulou",
    authors="Christodoulou, S.P. and Zafiris, P.A. and Papatheodorou, T.S.",
    place=ICSE,
    pp="75-92",
    entrytype="article",
    note="cited By 30",
    ID="Christodoulou200075",
))

jeffery2000a = DB(WorkSnowball(
    2000, "Comparative study of two software development cost modeling techniques using multi-organizational and company-specific data",
    display="jeffery",
    authors="Jeffery, R. and Ruhe, M. and Wieczorek, I.",
    place=IST,
    pp="1009-1016",
    entrytype="article",
    volume="42",
    number="14",
    doi="10.1016/S0950-5849(00)00153-1",
    note="cited By 111",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0034319879&doi=10.1016%2fS0950-5849%2800%2900153-1&partnerID=40&md5=86488c0314b34fd4b99ed5e35987c52f",
    document_type="Article",
    source="Scopus",
    ID="Jeffery20001009",
    scopus=1,
))
