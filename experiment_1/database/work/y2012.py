# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bayona2012a = DB(WorkUnrelated(
    2012, "Critical success factors in software process improvement: A systematic review",
    display="bayona",
    authors="Bayona, S. and Calvo-Manzano, J.A. and San Feliu, T.",
    place=CCIS,
    pp="1-12",
    entrytype="article",
    volume="290 CCIS",
    doi="10.1007/978-3-642-30439-2_1",
    note="cited By 8",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84862194516&doi=10.1007%2f978-3-642-30439-2_1&partnerID=40&md5=7e84fdf0b4d3cce91cbd39ad50cb9487",
    document_type="Conference Paper",
    source="Scopus",
    ID="Bayona20121",
    scopus="1",
))

bayona2012b = DB(WorkUnrelated(
        2012, "Critical Success Factors in Software Process Improvement: A Systematic Review",
        display="bayona b",
        authors="Bayona, Sussy and Calvo-Manzano, Jose A. and San Feliu, Tomas",
        pp="1-12",
        place=SPICD,
        entrytype="inproceedings",
        editor="Mas, A and Mesquida, A and Rout, T and OConnor, RV and Dorling, A",
        series="Communications in Computer and Information Science",
        volume="290",
        organization="Univ Illes Balears; SPICE User Grp",
        issn="1865-0929",
        isbn="978-3-642-30438-5",
        uniqueid="ISI:000310938100001",
        ID="ISI:000310938100001",
        webofscience="1",
    ))
