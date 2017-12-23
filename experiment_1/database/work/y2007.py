# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

martins2007a = DB(WorkUnrelated(
    2007, "A comparative study of SPI approaches with ProPAM",
    display="martins",
    authors="Martins, P.V. and Da Silva, A.R.",
    place=ICQICT,
    pp="100-109",
    entrytype="inproceedings",
    doi="10.1109/QUATIC.2007.5",
    art_number="4335238",
    note="cited By 1",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-48449096217&doi=10.1109%2fQUATIC.2007.5&partnerID=40&md5=9fb0c5ff8da45f592132501a9427140c",
    document_type="Conference Paper",
    source="Scopus",
    ID="Martins2007100",
    scopus="1",
))

wilkie2007a = DB(WorkSnowball(
    2007, "A low-overhead method for software process appraisal",
    display="wilkie",
    authors="Wilkie, F.G. and Mc Caffery, F. and McFall, D. and Lester, N. and Wilkinson, E.",
    place=SPIP,
    pp="339-349",
    entrytype="inproceedings",
    volume="12",
    number="4",
    doi="10.1002/spip.321",
    note="cited By 4",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-34547949093&doi=10.1002%2fspip.321&partnerID=40&md5=49a3ce14341a74f0d3f55e44512992ce",
    document_type="Conference Paper",
    source="Scopus",
    ID="Wilkie2007339",
    scopus="1",
))
