# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kerzazi2015a = DB(WorkUnrelated(
        2015, "Conceptual Alignment Between SPEM-Based Processes and CMMI",
        display="kerzazi",
        authors="Kerzazi, Noureddine",
        place=SITA,
        entrytype="inproceedings",
        organization="IEEE",
        isbn="978-1-5090-0220-7",
        uniqueid="ISI:000380409500017",
        ID="ISI:000380409500017",
        webofscience="1",
))

oConnor2015a = DB(WorkSnowball(
    2015, "Exploring the use of the cynefin framework to inform software development approach decisions",
    display="oConnor",
    authors="O'Connor, R.V. and Lepmets, M.",
    place=ACMICPS,
    pp="97-101",
    entrytype="inproceedings",
    volume="24-26-August-2015",
    doi="10.1145/2785592.2785608",
    note="cited By 1",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84958538253&doi=10.1145%2f2785592.2785608&partnerID=40&md5=69f4570281d159270659261c0d50408c",
    document_type="Conference Paper",
    source="Scopus",
    ID="O'Connor201597",
))

petersen2015a = DB(WorkSnowball(
    2015, "An elicitation instrument for operationalising GQM+Strategies (GQM+S-EI)",
    display="petersen",
    authors="Petersen, K. and Gencel, C. and Asghari, N. and Betz, S.",
    place=ESE,
    pp="968-1005",
    entrytype="inproceedings",
    volume="20",
    number="4",
    doi="10.1007/s10664-014-9306-z",
    note="cited By 3",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84930477271&doi=10.1007%2fs10664-014-9306-z&partnerID=40&md5=3c0ee587416354cc911b2d5e7b32c115",
    document_type="Article",
    source="Scopus",
    ID="Petersen2015968",
))
