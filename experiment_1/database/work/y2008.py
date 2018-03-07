# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

becker2008a = DB(WorkSnowball(
    2008, "An approach to support the strategic alignment of software process improvement programs",
    display="becker b",
    authors="Becker, A.L. and Audy, J.L.N. and Prikladnicki, R.",
    place=ICEIS,
    pp="66-73",
    entrytype="inproceedings",
    volume="1 ISAS",
    note="cited By 1",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-55849097328&partnerID=40&md5=eff87517025c0276626e85fb6d97617e",
    document_type="Conference Paper",
    source="Scopus",
    ID="Becker200866",
    scopus="1",
))

becker2008b = DB(WorkSnowball(
    2008, "Strategic Alignment of Software Process Improvement Programs Using QFD",
    display="becker",
    authors="Becker, André Luiz and Prikladnicki, Rafael and Audy, Jorge Luis Nicolas",
    place=IWBIPI,
    pp="9--14",
    entrytype="inproceedings",
    series="BiPi '08",
    isbn="978-1-60558-032-6",
    location="Leipzig, Germany",
    numpages="6",
    link="http://doi.acm.org/10.1145/1370837.1370840",
    doi="10.1145/1370837.1370840",
    acmid="1370840",
    publisher="ACM",
    address="New York, NY, USA",
    keyword="cmmi, software process improvement, strategic alignment, strategic planning",
    ID="Becker:2008:SAS:1370837.1370840",
))

becker2008c = DB(WorkUnrelated(
    2008, "AN APPROACH TO SUPPORT THE STRATEGIC ALIGNMENT OF SOFTWARE PROCESS IMPROVEMENT PROGRAMS",
    display="becker c",
    authors="Becker, Andre Luiz and Audy, Jorge Luis Nicolas and Prikladnicki, Rafael",
    place=FAKE,
    pp="66-73",
    entrytype="inproceedings",
    editor="Cordeiro, J and Filipe, J",
    note="10th International Conference on Enterprise Information Systems, Barcelona, SPAIN, JUN 12-16, 2008",
    organization="Inst Syst & Technologies Informat, Control & Commun; Workflow Management Coalit; Assoc Adv Artificial Intelligence",
    isbn="978-989-8111-38-8",
    ID="ISI:000259605700012",
    webofscience="1",
    placex="ICEIS 2008: PROCEEDINGS OF THE TENTH INTERNATIONAL CONFERENCE ON ENTERPRISE INFORMATION SYSTEMS, VOL ISAS-1: INFORMATION SYSTEMS ANALYSIS AND SPECIFICATION, VOL 1",
))

martins2008a = DB(WorkSnowball(
    2008, "Propamet: A metric for process and project alignment",
    display="martins",
    authors="Martins, P.V. and Silva, A.R.D.",
    place=CCIS,
    pp="201-212",
    entrytype="inproceedings",
    volume="16",
    note="cited By 6",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84988021263&partnerID=40&md5=8694c8d89616268270d27a35ded7dda9",
    document_type="Conference Paper",
    source="Scopus",
    ID="Martins2008201",
    scopus="1",
))
