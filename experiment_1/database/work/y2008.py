# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

asokan2008a = DB(WorkUnrelated(
    2008, "Healthy Technology",
    display="asokan",
    authors="Asokan, Ashwini and Payne, Michael .J.",
    place=FAKE,
    pp="2053--2066",
    entrytype="inproceedings",
    series="CHI EA '08",
    isbn="978-1-60558-012-8",
    location="Florence, Italy",
    ID="Asokan:2008:HT:1358628.1358637",
    acm="1",
    placex="CHI '08 Extended Abstracts on Human Factors in Computing Systems",
))

babar2008a = DB(WorkUnrelated(
    2008, "Problem Frames and Business Strategy Modelling",
    display="babar",
    authors="Babar, Abdul R. and Zowghi, Didar and Cox, Karl and Tosic, Vladimir and Bleistein, Steven and Verner, June",
    place=FAKE,
    pp="48--51",
    entrytype="inproceedings",
    series="IWAAPF '08",
    isbn="978-1-60558-020-3",
    location="Leipzig, Germany",
    ID="Babar:2008:PFB:1370811.1370821",
    acm="1",
    placex="Proceedings of the 3rd International Workshop on Applications and Advances of Problem Frames",
))

babar2008b = DB(WorkUnrelated(
    2008, "Three Integration Approaches for Map and B-SCP Requirements Engineering Techniques",
    display="babar b",
    authors="Babar, Abdul and Zowghi, Didar and Cox, Karl and Tosic, Vladimir",
    place=FAKE,
    pp="650--655",
    entrytype="inproceedings",
    series="SAC '08",
    isbn="978-1-59593-753-7",
    location="Fortaleza, Ceara, Brazil",
    ID="Babar:2008:TIA:1363686.1363841",
    acm="1",
    placex="Proceedings of the 2008 ACM Symposium on Applied Computing",
))

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
    webofscience="1",
    elcompendex="1",
    placex="ICEIS 2008 - Proceedings of the 10th International Conference on Enterprise Information Systems",
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

cheng2008a = DB(WorkUnrelated(
    2008, "Semi-supervised Learning with Data Calibration for Long-term Time Series Forecasting",
    display="cheng",
    authors="Cheng, Haibin and Tan, Pang-Ning",
    place=FAKE,
    pp="133--141",
    entrytype="inproceedings",
    series="KDD '08",
    isbn="978-1-60558-193-4",
    location="Las Vegas, Nevada, USA",
    ID="Cheng:2008:SLD:1401890.1401911",
    acm="1",
    placex="Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining",
))

fairweather2008a = DB(WorkUnrelated(
    2008, "How Older and Younger Adults Differ in Their Approach to Problem Solving on a Complex Website",
    display="fairweather",
    authors="Fairweather, Peter G.",
    place=FAKE,
    pp="67--72",
    entrytype="inproceedings",
    series="Assets '08",
    isbn="978-1-59593-976-0",
    location="Halifax, Nova Scotia, Canada",
    ID="Fairweather:2008:OYA:1414471.1414485",
    acm="1",
    placex="Proceedings of the 10th International ACM SIGACCESS Conference on Computers and Accessibility",
))

hornbæk2008a = DB(WorkUnrelated(
    2008, "Making Use of Business Goals in Usability Evaluation: An Experiment with Novice Evaluators",
    display="hornbæk",
    authors="Hornbæk, Kasper and Frøkjær, Erik",
    place=FAKE,
    pp="903--912",
    entrytype="inproceedings",
    series="CHI '08",
    isbn="978-1-60558-011-1",
    location="Florence, Italy",
    ID="Hornbaek:2008:MUB:1357054.1357197",
    acm="1",
    placex="Proceedings of the SIGCHI Conference on Human Factors in Computing Systems",
))

janssen2008a = DB(WorkUnrelated(
    2008, "Transformational Government: Basics and Key Issues",
    display="janssen",
    authors="Janssen, Marijn and Shu, William S.",
    place=FAKE,
    pp="117--122",
    entrytype="inproceedings",
    series="ICEGOV '08",
    isbn="978-1-60558-386-0",
    location="Cairo, Egypt",
    ID="Janssen:2008:TGB:1509096.1509120",
    acm="1",
    placex="Proceedings of the 2Nd International Conference on Theory and Practice of Electronic Governance",
))

kleinberg2008a = DB(WorkUnrelated(
    2008, "Strategic Network Formation with Structural Holes",
    display="kleinberg",
    authors="Kleinberg, Jon and Suri, Siddharth and Tardos, Éva and Wexler, Tom",
    place=FAKE,
    pp="284--293",
    entrytype="inproceedings",
    series="EC '08",
    isbn="978-1-60558-169-9",
    location="Chicago, Il, USA",
    numpages="10",
    ID="Kleinberg:2008:SNF:1386790.1386835",
    acm="1",
    placex="Proceedings of the 9th ACM Conference on Electronic Commerce",
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
    webofscience="1",
    elcompendex="1",
    placex="Communications in Computer and Information Science",
))

pijpers2008a = DB(WorkUnrelated(
    2008, "Business strategy-IT Alignment in a Multi-actor Setting: A Mobile e-Service Case",
    display="pijpers",
    authors="Pijpers, Vincent and Gordijn, Jaap and Akkermans, Hans",
    place=FAKE,
    pp="8:1--8:10",
    entrytype="inproceedings",
    series="ICEC '08",
    isbn="978-1-60558-075-3",
    location="Innsbruck, Austria",
    ID="Pijpers:2008:BSA:1409540.1409551",
    acm="1",
    placex="Proceedings of the 10th International Conference on Electronic Commerce",
))

punyabukkana2008a = DB(WorkUnrelated(
    2008, "Thailand's National Digital Divide Strategic Framework",
    display="punyabukkana",
    authors="Punyabukkana, Proadpran and Thanawastien, Suchai and Jirachiefpattana, Ajin",
    place=FAKE,
    pp="97--100",
    entrytype="inproceedings",
    series="W4A '08",
    isbn="978-1-60558-153-8",
    location="Beijing, China",
    ID="Punyabukkana:2008:TND:1368044.1368065",
    acm="1",
    placex="Proceedings of the 2008 International Cross-disciplinary Conference on Web Accessibility (W4A)",
))

reitbauer2008a = DB(WorkUnrelated(
    2008, "Redesigning Business Networks: Reference Process, Network and Service Map",
    display="reitbauer",
    authors="Reitbauer, Stefan and Kohlmann, Falk and Eckert, Clemens and Mansfeldt, Ken and Alt, Rainer",
    place=FAKE,
    pp="540--547",
    entrytype="inproceedings",
    series="SAC '08",
    isbn="978-1-59593-753-7",
    location="Fortaleza, Ceara, Brazil",
    ID="Reitbauer:2008:RBN:1363686.1363819",
    acm="1",
    placex="Proceedings of the 2008 ACM Symposium on Applied Computing",
))

stafford2008a = DB(WorkUnrelated(
    2008, "Letter from the Editors",
    display="stafford",
    authors="Stafford, Tom and Chau, Patrick Y.K.",
    place=FAKE,
    pp="4--5",
    entrytype="article",
    issue_date="May 2008",
    volume="39",
    number="2",
    month="apr",
    issn="0095-0033",
    ID="Stafford:2008:LE:1364636.1364637",
    acm="1",
    placex="SIGMIS Database",
))

vähäniitty2008a = DB(WorkUnrelated(
    2008, "Towards a Conceptual Framework and Tool Support for Linking Long-term Product and Business Planning with Agile Software Development",
    display="vähäniitty",
    authors="Vähäniitty, Jarno and Rautiainen, Kristian T.",
    place=FAKE,
    pp="25--28",
    entrytype="inproceedings",
    series="SDG '08",
    isbn="978-1-60558-035-7",
    location="Leipzig, Germany",
    ID="Vahaniitty:2008:TCF:1370720.1370730",
    acm="1",
    placex="Proceedings of the 1st International Workshop on Software Development Governance",
))
