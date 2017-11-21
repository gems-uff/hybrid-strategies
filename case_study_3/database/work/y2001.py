# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

jeffery2001a = DB(WorkSnowball(
    2001, "Using public domain metrics to estimate software development effort",
    display="jeffery",
    authors="Jeffery, R. and Ruhe, M. and Wieczorek, I.",
    place=ISMS,
    pp="16-27",
    entrytype="inproceedings",
    note="cited By 110",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0035023813&partnerID=40&md5=8c7929cac6f9e744842d3fb6aa5aff18",
    document_type="Conference Paper",
    source="Scopus",
    ID="Jeffery200116",
    scopus=1,
))

kitchenham2001a = DB(WorkOk(
    2001, "What accuracy statistics really measure",
    display="kitchenham",
    authors="Kitchenham, B.A. and Pickard, L.M. and MacDonell, S.G. and Shepperd, M.J.",
    place=IEEES,
    pp="81-85",
    entrytype="article",
    volume="148",
    number="3",
    doi="10.1049/ip-sen:20010506",
    note="cited By 229",
    ID="Kitchenham200181",
))

shepperd2001a = DB(WorkOk(
    2001, "Using simulation to evaluate prediction techniques",
    display="shepperd",
    authors="Shepperd, M. and Kadoda, G.",
    place=ISMS,
    pp="349-359",
    entrytype="inproceedings",
    note="cited By 60",
    ID="Shepperd2001349",
))
