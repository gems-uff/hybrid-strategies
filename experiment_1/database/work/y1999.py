# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

becker1999a = DB(WorkUnrelated(
    1999, "Aligning strategic and project measurement systems",
    display="becker",
    authors="Becker, S.A. and Bostelman, M.L.",
    place=IEEES,
    pp="46-51",
    entrytype="article",
    volume="16",
    number="3",
    doi="10.1109/52.765786",
    note="cited By 19",
    ID="Becker199946",
    placex="IEEE Software",
))

biró1999a = DB(WorkUnrelated(
    1999, "The Software Process in the Context of Business Goals and Performance",
    display="biró",
    authors="Biró, M. and Tully, C.",
    pp="15-27",
    place=FAKE,
    placex="Better Software Practice for Business Benefit: Principles and Experience",
    entrytype="article",
    note="cited By 3",
    ID="Biró199915",
))

caputo1999a = DB(WorkUnrelated(
    1999, "Facilitating CMM culture change",
    display="caputo",
    authors="Caputo, K.",
    place=FAKE,
    placex="SEI SEPG Conference",
    entrytype="article",
    note="cited By 1",
    ID="Caputo1999",
))

cignoni1999a = DB(WorkUnrelated(
    1999, "Rapid software process assessment to promote innovation in SME's",
    display="cignoni",
    authors="Cignoni, G.A.",
    place=FAKE,
    placex="Proceedings of Euromicro",
    entrytype="article",
    volume="99",
    note="cited By 4",
    ID="Cignoni1999",
))

debou1999a = DB(WorkUnrelated(
    1999, "Alcatel's Experience with Process Improvement",
    display="debou",
    authors="Debou, C. and Courtel, D. and Lambert, H.-B. and Fuchs, N. and Haux, M.",
    pp="281-301",
    place=FAKE,
    placex="Better Software Practice for Business Benefit: Principles and Experience",
    entrytype="article",
    note="cited By 7",
    ID="Debou1999281",
))

dekkers1999a = DB(WorkUnrelated(
    1999, "The Secrets of Highly Successful Measurement Programs",
    display="dekkers",
    authors="Dekkers, C.A.",
    pp="29-35",
    place=FAKE,
    placex="Cutter IT Journal",
    entrytype="article",
    volume="12",
    number="4",
    note="cited By 13",
    ID="Dekkers199929",
))

eagen1999a = DB(WorkUnrelated(
    1999, "Where the rubber meets the road: Getting it done with process action teams",
    display="eagen",
    authors="Eagen, B.",
    place=FAKE,
    placex="SEI SEPG Conference",
    entrytype="article",
    note="cited By 1",
    ID="Eagen1999",
))

ebert1999a = DB(WorkUnrelated(
    1999, "Technical controlling and software process improvement",
    display="ebert",
    authors="Christof Ebert",
    place=JSS,
    pp="25 - 39",
    entrytype="article",
    volume="46",
    number="1",
    note="",
    issn="0164-1212",
    doi="https://doi.org/10.1016/S0164-1212(98)10086-9",
    link="https://www.sciencedirect.com/science/article/pii/S0164121298100869",
    keyword="Technical controlling",
    ID="Ebert199925",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

ebert1999b = DB(WorkUnrelated(
    1999, "Technical controlling in software development",
    display="ebert b",
    authors="Christof Ebert",
    place=FAKE,
    pp="17 - 28",
    entrytype="article",
    volume="17",
    number="1",
    note="",
    issn="0263-7863",
    doi="https://doi.org/10.1016/S0263-7863(97)00065-3",
    link="https://www.sciencedirect.com/science/article/pii/S0263786397000653",
    keyword="technical controlling",
    ID="Ebert199917",
    sciencedirect="1",
    placex="International Journal of Project Management",
))

florac1999a = DB(WorkUnrelated(
    1999, "Measuring the Software Process: Statistical Process Control for Software Process Improvement",
    display="florac",
    authors="Florac, W.A. and Carleton, A.D.",
    place=FAKE,
    entrytype="article",
    note="cited By 202",
    ID="Florac1999",
    placex="Addison Wesley Publishing Company",
))

garbett1999a = DB(WorkUnrelated(
    1999, "A case study in innovative process improvement: code synthesis from formal specifications",
    display="garbett",
    authors="P. Garbett and J.P. Parkes and M. Shackleton and S. Anderson",
    place=FAKE,
    pp="417 - 424",
    entrytype="article",
    volume="23",
    number="7",
    note="",
    issn="0141-9331",
    doi="https://doi.org/10.1016/S0141-9331(99)00052-6",
    link="https://www.sciencedirect.com/science/article/pii/S0141933199000526",
    keyword="Safety-critical software",
    ID="Garbett1999417",
    sciencedirect="1",
    placex="Microprocessors and Microsystems",
))

hefner1999a = DB(WorkUnrelated(
    1999, "The top ten reasons improvement efforts fail",
    display="hefner",
    authors="Hefner, R.",
    place=FAKE,
    placex="SEI SEPG Conference",
    entrytype="article",
    note="cited By 1",
    ID="Hefner1999",
))

humphrey1999a = DB(WorkUnrelated(
    1999, "Changing the software culture",
    display="humphrey",
    authors="Humphrey, W.",
    place=FAKE,
    placex="SEI SEPG Conference",
    entrytype="article",
    note="cited By 1",
    ID="Humphrey1999",
))

raffo1999a = DB(WorkUnrelated(
    1999, "Software process simulation to achieve higher \CMM\ levels",
    display="raffo",
    authors="David M Raffo and Joseph V Vandeville and Robert H Martin",
    place=JSS,
    pp="163 - 172",
    entrytype="article",
    volume="46",
    number="23",
    note="",
    issn="0164-1212",
    doi="https://doi.org/10.1016/S0164-1212(99)00009-6",
    link="https://www.sciencedirect.com/science/article/pii/S0164121299000096",
    ID="Raffo1999163",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

sommerville1999a = DB(WorkSnowball(
    1999, "Managing process inconsistency using viewpoints",
    display="sommerville",
    authors="Sommerville, Ian and Sawyer, Peter and Viller, Stephen",
    place=ToSE,
    pp="784--799",
    entrytype="article",
    volume="25",
    number="6",
    doi="10.1109/32.824395",
    note="cited By 30",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-0033345410&doi=10.1109%2f32.824395&partnerID=40&md5=047051619f9e05d42e5182681403625a",
    document_type="Article",
    source="Scopus",
    ID="Sommerville1999784",
    scholar="http://scholar.google.com/scholar?cites=3693616915823083489&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="IEEE",
    cluster_id="3693616915823083489",
    scholar_ok=True,
))

wastell1999a = DB(WorkUnrelated(
    1999, "The Human Dimension of the Software Process",
    display="wastell",
    authors="Wastell, David",
    place=FAKE,
    pp="165--199",
    entrytype="inbook",
    editor="Derniame, Jean-Claude and Kaba, Badara Ali and Wastell, David",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="Wastell1999",
    springer="1",
    placex="Software Process: Principles, Methodology, and Technology",
))

wigle1999a = DB(WorkUnrelated(
    1999, "The SEPG from level 1 to level 5",
    display="wigle",
    authors="Wigle, G.B.",
    place=FAKE,
    placex="SEI SEPG Conference",
    entrytype="article",
    note="cited By 1",
    ID="Wigle1999",
))

yamamura1999a = DB(WorkUnrelated(
    1999, "Software process satisfied employees",
    display="yamamura",
    authors="Yamamura, G.",
    place=IEEES,
    pp="83-85",
    entrytype="article",
    number="5",
    note="cited By 21",
    ID="Yamamura199983",
))
