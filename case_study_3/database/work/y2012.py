# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

ferrucci2012a = DB(WorkSnowball(
    2012, "Web effort estimation: The value of cross-company data set compared to single-company data set",
    display="ferrucci",
    authors="Ferrucci, Filomena and Mendes, Emilia and Sarro, Federica",
    pp="29--38",
    place=ACMICPS,
    entrytype="inproceedings",
    doi="10.1145/2365324.2365330",
    note="cited By 7",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84867703659&doi=10.1145%2f2365324.2365330&partnerID=40&md5=ea1a26076f6603ca8dffbee099870e11",
    document_type="Conference Paper",
    source="Scopus",
    ID="Ferrucci201229",
    scopus=1,
    cluster_id="18250519131212182515",
    scholar="http://scholar.google.com/scholar?cites=18250519131212182515&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    scholar_ok=True,
))

kocaguneli2012a = DB(WorkOk(
    2012, "Exploiting the essential assumptions of analogy-based effort estimation",
    display="kocaguneli",
    authors="Kocaguneli, Ekrem and Menzies, Tim and Bener, Ayse and Keung, Jacky W",
    place=ToSE,
    pp="425--438",
    entrytype="article",
    volume="38",
    number="2",
    doi="10.1109/TSE.2011.27",
    art_number="5728833",
    note="cited By 79",
    ID="Kocaguneli2012425",
    cluster_id="7026699471245301107",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=7026699471245301107&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

shepperd2012a = DB(WorkUnrelated(
    2012, "Evaluating prediction systems in software project estimation",
    display="shepperd",
    authors="Shepperd, Martin and MacDonell, Steve",
    place=IST,
    pp="820--827",
    entrytype="article",
    volume="54",
    number="8",
    publisher="Elsevier",
    ID="shepperd2012evaluating",
    cluster_id="1730979205044074335",
    scholar="http://scholar.google.com/scholar?cites=1730979205044074335&as_sdt=2005&sciodt=0,5&hl=en",
))

wen2012a = DB(WorkUnrelated(
    2012, "Systematic literature review of machine learning based software development effort estimation models",
    display="wen",
    authors="Wen, Jianfeng and Li, Shixian and Lin, Zhiyong and Hu, Yong and Huang, Changqin",
    place=IST,
    pp="41--59",
    entrytype="article",
    volume="54",
    number="1",
    publisher="Elsevier",
    ID="wen2012systematic",
    cluster_id="13194848204925514356",
    scholar="http://scholar.google.com/scholar?cites=13194848204925514356&as_sdt=2005&sciodt=0,5&hl=en",
))
