# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kitchenham2004a = DB(WorkSnowball(
    2004, "A comparison of cross-company and within-company effort estimation models for web applications",
    display="kitchenham",
    authors="Kitchenham, B. and Mendes, E.",
    place=ESEM,
    pp="47-55",
    entrytype="inproceedings",
    note="cited By 41",
    ID="Kitchenham200447",
    scholar="https://scholar.google.com/scholar?cites=14741492553228492661&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="14741492553228492661",
    scholar_ok=True,
))

mendes2004a = DB(WorkSnowball(
    2004, "Further comparison of cross-company and within-company effort estimation models for web applications",
    display="mendes",
    authors="Mendes, Emilia and Kitchenham, Barbara",
    place=ISMS,
    pp="348--357",
    entrytype="inproceedings",
    doi="10.1109/METRIC.2004.1357920",
    note="cited By 76",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-14844320530&doi=10.1109%2fMETRIC.2004.1357920&partnerID=40&md5=21ac53c036518230cf33aa00cee788f0",
    document_type="Conference Paper",
    source="Scopus",
    ID="Mendes2004348",
    scopus=1,
    acm=1,
    cluster_id="13719283821229655348",
    scholar="http://scholar.google.com/scholar?cites=13719283821229655348&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE",
    scholar_ok=True,
))
