# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


hill1999a = DB(WorkOk(
    1999, "Software Project Estimation: a Workbook for Macro-Estimation of Software Development Effort and Duration",
    display="hill",
    authors="Hill, P",
    place=ISBSG,
    entrytype="article",
    note="cited By 1",
    ID="Hill1999",
))

lokan1999a = DB(WorkOk(
    1999, "Empirical study of the correlations between function point elements",
    display="lokan",
    authors="Lokan, Chris J.",
    place=ISMS,
    pp="200-206",
    entrytype="inproceedings",
    note="cited By 20",
    ID="Lokan1999200",
))

maxwell1999a = DB(WorkSnowball(
    1999, "Performance evaluation of general and company specific models in software development effort estimation",
    display="maxwell",
    authors="Maxwell, Katrina and Van Wassenhove, Luk and Dutta, Soumitra",
    place=MS,
    pp="787--803",
    entrytype="article",
    volume="45",
    number="6",
    note="cited By 45",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0032664427&partnerID=40&md5=c8eee9556fd65e8a2368d9e0c790a94c",
    document_type="Article",
    source="Scopus",
    ID="Maxwell1999787",
    scopus="1",
    cluster_id="12175590154798452669",
    publisher="INFORMS",
    scholar="http://scholar.google.com/scholar?cites=12175590154798452669&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

briand1999a = DB(WorkOk(
    1999, "Assessment and comparison of common software cost estimation modeling techniques",
    display="briand",
    authors="Briand, Lionel C. and El Emam, Khaled and Maxwell, Katrina D. and Surmann, Dagmar and Wieczorek, Isabella",
    place=ICSE,
    pp="313--323",
    entrytype="inproceedings",
    note="cited By 124",
    ID="Briand1999313",
    cluster_id="6960886206194742586",
    scholar="https://scholar.google.com.br/scholar?cites=11135653044424553421&as_sdt=2005&sciodt=0,5&hl=pt-BR",
    organization="ACM",
    scholar_ok=True,
))

walkerden1999a = DB(WorkOk(
    1999, "Empirical study of analogy-based software effort estimation",
    display="walkerden",
    authors="Walkerden, F. and Jeffery, R.",
    place=ESE,
    pp="135-158",
    entrytype="article",
    volume="4",
    number="2",
    doi="10.1023/A:1009872202035",
    note="cited By 142",
    ID="Walkerden1999135",
))
