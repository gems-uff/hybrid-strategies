# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

ferrucci2012a = DB(WorkSnowball(
    2012, "Web effort estimation: The value of cross-company data set compared to single-company data set",
    display="ferrucci",
    authors="Ferrucci, F. and Sarro, F. and Mendes, E.",
    pp="29-38",
    place=ACMICPS,
    entrytype="inproceedings",
    doi="10.1145/2365324.2365330",
    note="cited By 7",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84867703659&doi=10.1145%2f2365324.2365330&partnerID=40&md5=ea1a26076f6603ca8dffbee099870e11",
    document_type="Conference Paper",
    source="Scopus",
    ID="Ferrucci201229",
    scopus=1,
))

kocaguneli2012a = DB(WorkOk(
    2012, "Exploiting the essential assumptions of analogy-based effort estimation",
    display="kocaguneli",
    authors="Kocaguneli, E. and Menzies, T. and Bener, A.B. and Keung, J.W.",
    place=ToSE,
    pp="425-438",
    entrytype="article",
    volume="38",
    number="2",
    doi="10.1109/TSE.2011.27",
    art_number="5728833",
    note="cited By 79",
    ID="Kocaguneli2012425",
))
