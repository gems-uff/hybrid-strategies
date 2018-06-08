# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

april2009a = DB(WorkUnrelated(
    2009, "An overview of software engineering process and its improvement",
    display="april",
    authors="April, Alain and Laporte, Claude",
    place=FAKE,
    pp="2984--2989",
    entrytype="incollection",
    publisher="IGI Global",
    ID="april2009overview",
    cluster_id="9168568441027548415",
    scholar="http://scholar.google.com/scholar?cites=9168568441027548415&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="Encyclopedia of Information Science and Technology, Second Edition",
))

bermón2009a = DB(WorkUnrelated(
    2009, "Software Process Asset Libraries Using Knowledge Repositories",
    display="bermón",
    authors="Bermón-Angarita, Leonardo and Amescua-Seco, Antonio and Sánchez-Segura, Maria Isabel and García-Guzmán, Javier",
    place=FAKE,
    pp="465--475",
    entrytype="incollection",
    publisher="IGI Global",
    ID="bermon2009software",
    gs2016="1",
    placex="Handbook of Research on Digital Libraries: Design, Development, and Impact",
))

bonazzi2009a = DB(WorkUnrelated(
    2009, "Compliance management is becoming a major issue in IS design",
    display="bonazzi",
    authors="Bonazzi, Riccardo and Hussami, Lotfi and Pigneur, Yves",
    place=FAKE,
    pp="391--398",
    entrytype="incollection",
    publisher="Springer",
    ID="bonazzi2009compliance",
    gs2016="1",
    placex="Information systems: People, organizations, institutions, and technologies",
))

falbo2009a = DB(WorkUnrelated(
    2009, "A software process ontology as a common vocabulary about software processes",
    display="falbo",
    authors="Falbo, Ricardo De Almeida and Bertollo, Gleidson",
    place=FAKE,
    pp="239--250",
    entrytype="article",
    volume="4",
    number="4",
    publisher="Inderscience Publishers",
    ID="falbo2009software",
    cluster_id="13554592707241944376",
    scholar="http://scholar.google.com/scholar?cites=13554592707241944376&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="International Journal of Business Process Integration and Management",
))

gazel2009a = DB(WorkSnowball(
    2009, "A CMMI Ontology for An Ontology-Based Software Process Assessment Tool",
    display="gazel",
    authors="Gazel, Sema and Tarhan, Ay{ç}a and Sezer, Ebru",
    place=FAKE,
    entrytype="inproceedings",
    volume="9",
    ID="gazel2009cmmi",
    cluster_id="6833681226443800582",
    scholar="http://scholar.google.com/scholar?cites=6833681226443800582&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="11",
    final_selected="1",
    scopus2016="1",
    placex="proceedings of the 16th EuroSPI2 Conference",
    gs2016="1",
))

kim2009a = DB(WorkUnrelated(
    2009, "Guideline-based Process Management Environment",
    display="kim",
    authors="Kim, Jeong-Ah",
    place=FAKE,
    pp="47--56",
    entrytype="article",
    volume="6",
    number="1",
    ID="kim2009guideline",
    gs2016="1",
    placex="보안공학연구논문지",
))

lee2009a = DB(WorkSnowball(
    2009, "Ontology-based computational intelligent multi-agent and its application to CMMI assessment",
    display="lee",
    authors="Lee, Chang-Shing and Wang, Mei-Hui",
    place=FAKE,
    pp="203--219",
    entrytype="article",
    volume="30",
    number="3",
    publisher="Springer",
    ID="lee2009ontology",
    cluster_id="15934008590346441714",
    scholar="http://scholar.google.com/scholar?cites=15934008590346441714&as_sdt=2005&sciodt=0,5&hl=en",
    selected_snowballing="1",
    selected_order="13",
    final_selected="1",    
    placex="Applied Intelligence",
))

rodríguez2009a = DB(WorkUnrelated(
    2009, "Defining spem 2 process constraints with semantic rules using swrl",
    display="rodríguez",
    authors="Rodríguez, Daniel and Sicilia, Miguel-Ángel",
    place=FAKE,
    pp="96",
    entrytype="article",
    ID="rodriguez2009defining",
    cluster_id="6294738835291260114",
    scholar="http://scholar.google.com/scholar?cites=6294738835291260114&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="Proceedings of ONTOSE",
))

tuffley2009a = DB(WorkUnrelated(
    2009, "Applying Design Research in Software Engineering to Develop a Process Reference Model",
    display="tuffley",
    authors="Tuffley, David",
    place=ICSE,
    entrytype="article",
    ID="tuffleyapplying",
    gs2016="1",
    placex="ICSE",
))
