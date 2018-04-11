# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

armbrust2010a = DB(WorkSnowball(
    2010, "Determining organization-specific process suitability",
    display="armbrust",
    authors="Armbrust, Ove",
    place=ICSE,
    pp="26--38",
    entrytype="inproceedings",
    organization="Springer",
    ID="armbrust2010determining",
    cluster_id="3542000251352756181",
    scholar="http://scholar.google.com/scholar?cites=3542000251352756181&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
    volume="6195 LNCS",
    doi="10.1007/978-3-642-14347-2_4",
    note="cited By 3",
))

armbrust2010b = DB(WorkSnowball(
    2010, "Which Processes Are Needed in Five Years? Strategic Process Portfolio Management at the Japan Aerospace Exploration Agency (JAXA)",
    display="armbrust",
    authors="Armbrust, Ove and Katahira, Masafumi and Kaneko, Tatsuya and Miyamoto, Yuko and Koishi, Yumi",
    place=FAKE,
    entrytype="article",
    ID="armbrustprocesses",
    placex="Proceedings of the International SPICE Days",
))

ast2010a = DB(WorkUnrelated(
    2010, "Driver tree - An experience simulation model for process improvement",
    display="ast",
    authors="Ast, S. and Russwurm, W. and Birkhölzer, T.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Ast2010",
    placex="SEPG North America",
))

barcellos2010a = DB(WorkUnrelated(
    2010, "A well-founded software process behavior ontology to support business goals monitoring in high maturity software organizations",
    display="barcellos",
    authors="Barcellos, Monalessa Perini and de Almeida Falbo, Ricardo and Rocha, Ana Regina",
    place=FAKE,
    pp="253--262",
    entrytype="inproceedings",
    organization="IEEE",
    ID="barcellos2010well",
    cluster_id="8525192396157377506",
    scholar="http://scholar.google.com/scholar?cites=8525192396157377506&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Enterprise Distributed Object Computing Conference Workshops (EDOCW), 2010 14th IEEE International",
    gs="1",
))

barcellos2010b = DB(WorkUnrelated(
    2010, "A Well-Founded Software Process Behavior Ontology to Support Business Goals Monitoring in High Maturity Software Organizations",
    display="barcellos b",
    authors="M. P. Barcellos and R. d. A. Falbo and A. R. Rocha",
    place=FAKE,
    pp="253-262",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="Capability Maturity Model;ontologies (artificial intelligence);software metrics;vocabulary;business goal achievement;business goal monitoring;high maturity software organization;process performance analysis;software measurement ontology;software process behavior ontology;technical goal achievement;unified foundational ontology;vocabulary;Ontologies;Organizations;Process control;Software;Software measurement;Standards organizations;Domain Ontologies;Foundational Ontology;Software Measurement;Software Measurement Ontology;Software Process Behavior Ontology",
    doi="10.1109/EDOCW.2010.15",
    issn="2325-6583",
    ID="5629052",
    ieee="1",
    placex="2010 14th IEEE International Enterprise Distributed Object Computing Conference Workshops",
))

barreto2010a = DB(WorkSnowball(
    2010, "Defining and monitoring strategically aligned software improvement goals",
    display="barreto",
    authors="Barreto, Andrea Oliveira Soares and Rocha, Ana Regina",
    place=PROFES,
    pp="380--394",
    entrytype="inproceedings",
    volume="6156 LNCS",
    doi="10.1007/978-3-642-13792-1_29",
    note="cited By 4",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955446167&doi=10.1007%2f978-3-642-13792-1_29&partnerID=40&md5=62f77861d2bc11d469e715dd6ef7c587",
    document_type="Conference Paper",
    source="Scopus",
    ID="Barreto2010380",
    elcompendex="1",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    scholar="http://scholar.google.com/scholar?cites=17460321150978889682&as_sdt=2005&sciodt=0,5&hl=en",
    organization="Springer",
    cluster_id="17460321150978889682",
    scholar_ok=True,
    gs="1",
))

barreto2010b = DB(WorkUnrelated(
    2010, "Analyzing the similarity among software projects to improve software project monitoring processes",
    display="barreto b",
    authors="Barreto, Andrea Oliveira Soares and Rocha, Ana Regina",
    place=ICQICT,
    pp="441--446",
    entrytype="inproceedings",
    organization="IEEE",
    ID="barreto2010analyzing",
    cluster_id="1505945229113365171",
    scholar="http://scholar.google.com/scholar?cites=1505945229113365171&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Quality of Information and Communications Technology (QUATIC), 2010 Seventh International Conference on the",
    ieee="1",
    gs="1",
))

basili2010a = DB(WorkSnowball(
    2010, "Linking software development and business strategy through measurement",
    display="basili",
    authors="Basili, Victor R and Lindvall, Mikael and Regardie, Myrna and Seaman, Carolyn and Heidrich, Jens and Münch, Jürgen and Rombach, Dieter and Trendowicz, Adam",
    place=C,
    pp="57--65",
    entrytype="article",
    volume="43",
    number="4",
    doi="10.1109/MC.2010.108",
    art_number="5445168",
    note="cited By 71",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-77951033625&doi=10.1109%2fMC.2010.108&partnerID=40&md5=f36e6e65d1ea856227721c90fc1ac645",
    document_type="Article",
    source="Scopus",
    ID="Basili201057",
    scholar="http://scholar.google.com/scholar?cites=8027935919137885990&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="8027935919137885990",
    publisher="IEEE",
    scholar_ok=True,
    placex="Computer",
    ieee="1",
    gs="1",
))

basili2010b = DB(WorkUnrelated(
    2010, "GQM+Strategies: A comprehensive methodology for aligning business strategies with software measurement",
    display="basili b",
    authors="Basili, V. and Heidrich, J. and Lindvall, M. and Münch, J. and Regardie, M. and Rombach, D.",
    place=FAKE,
    pp="1-14",
    entrytype="article",
    note="cited By 1",
    ID="Basili20101",
    placex="Kaiserslautern, Germany, 2007. MetriKon 2007",
))

basili2010c = DB(WorkUnrelated(
    2010, "Determining the impact of business strategies using principles from goal-oriented measurement",
    display="basili c",
    authors="Basili, V. and Heidrich, J. and Lindvall, M. and Münch, J. and Seaman, C. and Regardie, M.",
    place=FAKE,
    pp="1-10",
    entrytype="article",
    note="cited By 1",
    ID="Basili20101",
    placex="Wien, Austria, 2009. 9. Internationale Tagung Wirtschaftsinformatik 2009",
))

begum2010a = DB(WorkUnrelated(
    2010, "Software development standard and software engineering practice: A case study of Bangladesh",
    display="begum",
    authors="Begum, Zerina and Khan, Mohammed Shafiul Alam and Hafiz, Mohd and Islam, Md and Shoyaib, MD and others",
    place=FAKE,
    entrytype="article",
    ID="begum2010software",
    cluster_id="7106924149308145684",
    scholar="http://scholar.google.com/scholar?cites=7106924149308145684&as_sdt=2005&sciodt=0,5&hl=en",
    placex="arXiv preprint arXiv:1008.3321",
))

boehm2010a = DB(WorkUnrelated(
    2010, "A risk-driven decision table for software process selection",
    display="boehm",
    authors="Boehm, B.W.",
    place=FAKE,
    pp="1",
    entrytype="article",
    note="cited By 3",
    ID="Boehm20101",
    placex="Lecture Notes in Computer Science",
))

buehrer2010a = DB(WorkUnrelated(
    2010, "A Distributed Placement Service for Graph-structured and Tree-structured Data",
    display="buehrer",
    authors="Buehrer, Gregory and Parthasarathy, Srinivasan and Tatikonda, Shirish",
    place=FAKE,
    pp="355--356",
    entrytype="article",
    issue_date="May 2010",
    volume="45",
    number="5",
    month="jan",
    issn="0362-1340",
    ID="Buehrer:2010:DPS:1837853.1693511",
    acm="1",
    placex="SIGPLAN Not.",
))

burlton2010a = DB(WorkUnrelated(
    2010, "Delivering business strategy through process management.",
    display="burlton",
    authors="R Burlton",
    place=FAKE,
    other1="pp 537",
    placex="vom Brocke J, Rosemann M (eds) Handbook on business process management 2. Springer, Berlin,",
))

carvalho2010a = DB(WorkUnrelated(
    2010, "Management Function Deployment: um Método para o Alinhamento Estratégico da Melhoria dos Processos de Gerenciamento de Projetos de Software",
    display="carvalho",
    authors="Carvalho, Gustavo HP and da Silva, Fabio QB and Fran{ç}a, A César C",
    place=FAKE,
    pp="135--149",
    entrytype="article",
    ID="carvalho2010management",
    cluster_id="1413388519633656976",
    scholar="http://scholar.google.com/scholar?cites=1413388519633656976&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Proceedings do IX Simpósio Brasileiro de Qualidade de Software. Belém, PA, Brasil: SBQS",
))

chiprout2010a = DB(WorkUnrelated(
    2010, "On-die Power Grids: The Missing Link",
    display="chiprout",
    authors="Chiprout, Eli",
    place=FAKE,
    pp="940--945",
    entrytype="inproceedings",
    series="DAC '10",
    isbn="978-1-4503-0002-5",
    location="Anaheim, California",
    ID="Chiprout:2010:OPG:1837274.1837511",
    acm="1",
    placex="Proceedings of the 47th Design Automation Conference",
))

cmmi2010a = DB(WorkUnrelated(
    2010, "CMMI for development, version 1.3",
    display="cmmi",
    authors="cmmi",
    place=FAKE,
    entrytype="article",
    note="cited By 189",
    ID="cmmi2010",
    placex="CMMI Product Team, CMU/SEI-2010-TR-033, Tech. Rep.",
    other1="Carnegie Mellon University, Pittsburgh, PA",
))

cmusei2010a = DB(WorkUnrelated(
    2010, "Capability Maturity Model Integration (CMMI) for Development",
    display="cmusei",
    authors="cmusei",
    place=FAKE,
    entrytype="article",
    note="cited By 3",
    ID="CMUSEI2010",
    placex="Technical Report CMU/SEI-2010-TR-033, Software Engineering Institute",
))

code2010a = DB(WorkUnrelated(
    2010, "Sarbanes-Oxley",
    display="code",
    authors="US Code",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="US2002",
    placex="Public Law No. 107-204",
))

conaldi2010a = DB(WorkUnrelated(
    2010, "The Meso-level Structure of F/OSS Collaboration Network: Local Communities and Their Innovativeness",
    display="conaldi",
    authors="Conaldi, Guido and Rullani, Francesco",
    place=FAKE,
    pp="42--52",
    entrytype="inproceedings",
    editor="Ågerfalk, Pär and Boldyreff, Cornelia and González-Barahona, Jesús M. and Madey, Gregory R. and Noll, John",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-642-13244-5_4",
    springer="1",
    placex="Open Source Software: New Horizons",
))

daramola2010a = DB(WorkUnrelated(
    2010, "A Process Framework for Semantics-Aware Tourism Information Systems",
    display="daramola",
    authors="Daramola, Olawande J.",
    place=FAKE,
    pp="521--532",
    entrytype="inproceedings",
    editor="Daniel, Florian and Facca, Federico Michele",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-642-16985-4_50",
    springer="1",
    placex="Current Trends in Web Engineering",
))

dounos2010a = DB(WorkUnrelated(
    2010, "Factors for the design of CMMI-based software process improvement initiatives",
    display="dounos",
    authors="Dounos, Petros and Bohoris, George",
    place=FAKE,
    pp="43--47",
    entrytype="inproceedings",
    organization="IEEE",
    ID="dounos2010factors",
    cluster_id="9521064757940340749",
    scholar="http://scholar.google.com/scholar?cites=9521064757940340749&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Informatics (PCI), 2010 14th Panhellenic Conference on",
    ieee="1",
    gs="1",
))

du2010a = DB(WorkUnrelated(
    2010, "a case study on usage of a software process management tool in china",
    display="du",
    authors="Du, Jing and Yang, Ye and Lin, Zhongpeng and Wang, Qing and Li, Mingshu and Yuan, Feng",
    place=SEC,
    pp="443--452",
    entrytype="inproceedings",
    organization="IEEE",
    ID="du2010case",
    cluster_id="5599657959749411000",
    scholar="http://scholar.google.com/scholar?cites=5599657959749411000&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Engineering Conference (APSEC), 2010 17th Asia Pacific",
))

détienne2010a = DB(WorkUnrelated(
    2010, "Why Do Users Communicate via Such or Such Media?: Some Insights from Users' Daily Experiences",
    display="détienne",
    authors="Détienne, Françoise and Cahour, Béatrice and Lefebvre, Liv",
    place=FAKE,
    pp="627--630",
    entrytype="inproceedings",
    series="NordiCHI '10",
    isbn="978-1-60558-934-3",
    location="Reykjavik, Iceland",
    ID="Detienne:2010:WUC:1868914.1868990",
    acm="1",
    placex="Proceedings of the 6th Nordic Conference on Human-Computer Interaction: Extending Boundaries",
))

díazley2010a = DB(WorkUnrelated(
    2010, "MIS-PyME software measurement capability maturity model  Supporting the definition of software measurement programs and capability determination",
    display="díazley",
    authors="María Díaz-Ley and Félix García and Mario Piattini",
    place=FAKE,
    pp="1223 - 1237",
    entrytype="article",
    volume="41",
    number="1011",
    note="",
    issn="0965-9978",
    doi="https://doi.org/10.1016/j.advengsoft.2010.06.007",
    link="https://www.sciencedirect.com/science/article/pii/S0965997810000682",
    keyword="Software process maturity",
    ID="DíazLey20101223",
    sciencedirect="1",
    placex="Advances in Engineering Software",
))

egorova2010a = DB(WorkUnrelated(
    2010, "Actual vs. perceived effect of software engineering practices in the Italian industry",
    display="egorova",
    authors="Evgenia Egorova and Marco Torchiano and Maurizio Morisio",
    place=JSS,
    pp="1907 - 1916",
    entrytype="article",
    volume="83",
    number="10",
    note="",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2010.05.077",
    link="https://www.sciencedirect.com/science/article/pii/S016412121000155X",
    keyword="Casecontrol Study",
    ID="Egorova20101907",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

escofet2010a = DB(WorkUnrelated(
    2010, "Strategic E-Business/IT Alignment for SME Competitiveness",
    display="escofet",
    authors="Escofet, Eduardo and Rodríguez-Fórtiz, María José and Garrido, José Luis and Chung, Lawrence",
    place=FAKE,
    pp="23",
    entrytype="article",
    publisher="IGI Global",
    ID="escofet2010strategic",
    cluster_id="15929686017158318957",
    scholar="http://scholar.google.com/scholar?cites=15929686017158318957&as_sdt=2005&sciodt=0,5&hl=en",
    placex="E-Business Managerial Aspects, Solutions and Case Studies",
))

esfahani2010a = DB(WorkUnrelated(
    2010, "A repository of agile method fragments",
    display="esfahani",
    authors="Esfahani, H.C. and Yu, E.",
    place=FAKE,
    pp="163-174",
    entrytype="article",
    volume="6195 LNCS",
    doi="10.1007/978-3-642-14347-2_15",
    note="cited By 14",
    ID="Esfahani2010163",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

faegri2010a = DB(WorkUnrelated(
    2010, "Introducing knowledge redundancy practice in software development: Experiences with job rotation in support work",
    display="faegri",
    authors="Tor Erlend Faegri and Tore Dybå and Torgeir Dingsøyr",
    place=IST,
    pp="1118 - 1132",
    entrytype="article",
    volume="52",
    number="10",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.06.002",
    link="https://www.sciencedirect.com/science/article/pii/S0950584910001011",
    keyword="Software development",
    ID="Fægri20101118",
    sciencedirect="1",
    placex="Information and Software Technology",
))

faulk2010a = DB(WorkUnrelated(
    2010, "Value-based software engineering (vbse): A value-driven approach to product-line engineering",
    display="faulk",
    authors="Faulk, S. and Harmon, R. and Raffo, D.",
    place=FAKE,
    pp="1-13",
    entrytype="article",
    note="cited By 1",
    ID="Faulk20101",
    placex="Denver, Colorado, 2000. The First International Conference on Software Product-Line Engineering",
))

ferrari2010a = DB(WorkUnrelated(
    2010, "A controlled experiment to assess the impact of system architectures on new system requirements",
    display="ferrari",
    authors="Ferrari, Remo and Miller, James A. and Madhavji, Nazim H.",
    place=FAKE,
    pp="215--233",
    entrytype="article",
    month="Jun",
    day="01",
    volume="15",
    number="2",
    ID="Ferrari2010",
    springer="1",
    placex="Requirements Engineering",
))

gartner2010a = DB(WorkUnrelated(
    2010, "Gartner executive programs CIO survey.",
    display="gartner",
    authors="Gartner",
    place=FAKE,
    placex="Press release, Gartner, Inc.",
))

goyal2010a = DB(WorkUnrelated(
    2010, "ROI for SPI: Lessons from Initiatives at IBM Global Services India",
    display="goyal",
    authors="Goyal, A. and Kanungo, S. and Muthu, V. and Jayadevan, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Goyal2010",
    placex="SEPG 2001 (2001)",
))

guzmán2010a = DB(WorkSnowball(
    2010, "Integration of strategic management, process improvement and quantitative measurement for managing the competitiveness of software engineering organizations",
    display="guzmán",
    authors="Guzmán, Javier García and Mitre, Hugo A and Amescua, Antonio and Velasco, Manuel",
    place=SQJ,
    pp="341--359",
    entrytype="article",
    volume="18",
    number="3",
    doi="10.1007/s11219-010-9094-7",
    note="cited By 7",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-77953479945&doi=10.1007%2fs11219-010-9094-7&partnerID=40&md5=ff201293071e1123dedf8e2ad949d4c5",
    document_type="Article",
    source="Scopus",
    ID="Guzmán2010341",
    scopus="1",
    webofscience="1",
    placex="Software Quality Journal",
    elcompendex="1",
    scholar="http://scholar.google.com/scholar?cites=17385845424469103121&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="17385845424469103121",
    publisher="Springer",
    scholar_ok=True,
))

haigh2010a = DB(WorkUnrelated(
    2010, "Software quality, non-functional software requirements and IT-business alignment",
    display="haigh",
    authors="Haigh, Maria",
    place=SQJ,
    pp="361--385",
    entrytype="article",
    volume="18",
    number="3",
    publisher="Springer",
    ID="haigh2010software",
    cluster_id="12894759810750422661",
    scholar="http://scholar.google.com/scholar?cites=12894759810750422661&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Quality Journal",
))

hammer2010a = DB(WorkUnrelated(
    2010, "What is business process management?",
    display="hammer",
    authors="M Hammer",
    place=FAKE,
    placex="vom Brocke J, Rosemann M (eds) Handbook on business process management, vol 1. Springer, Heidelberg",
))

hauge2010a = DB(WorkUnrelated(
    2010, "Adoption of open source software in software-intensive organizations  A systematic literature review",
    display="hauge",
    authors="Øyvind Hauge and Claudia Ayala and Reidar Conradi",
    place=IST,
    pp="1133 - 1154",
    entrytype="article",
    volume="52",
    number="11",
    note="Special Section on Best Papers \{PROMISE\} 2009",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.05.008",
    link="https://www.sciencedirect.com/science/article/pii/S0950584910000972",
    keyword="Systematic literature review",
    ID="Hauge20101133",
    sciencedirect="1",
    placex="Information and Software Technology",
))

hauge2010b = DB(WorkUnrelated(
    2010, "Risks and Risk Mitigation in Open Source Software Adoption: Bridging the Gap between Literature and Practice",
    display="hauge b",
    authors="Hauge, Øyvind and Cruzes, Daniela Soares and Conradi, Reidar and Velle, Ketil Sandanger and Skarpenes, Tron André",
    place=FAKE,
    pp="105--118",
    entrytype="inproceedings",
    editor="Ågerfalk, Pär and Boldyreff, Cornelia and González-Barahona, Jesús M. and Madey, Gregory R. and Noll, John",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-642-13244-5_9",
    springer="1",
    placex="Open Source Software: New Horizons",
))

hernández2010a = DB(WorkUnrelated(
    2010, "Alineación de la gestión estratégica con la medición de productos y procesos para organizaciones de ingeniería del software",
    display="hernández",
    authors="Mitre Hernández, Hugo Arnoldo",
    place=FAKE,
    entrytype="article",
    ID="mitre2010alineacion",
    cluster_id="14076163248140744138",
    scholar="http://scholar.google.com/scholar?cites=14076163248140744138&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

hinz2010a = DB(WorkUnrelated(
    2010, "Exploring the localization requirements for Kashubian Linux: Opening new markets for open-source development projects",
    display="hinz",
    authors="Hinz, Yurek K",
    place=Thesis,
    entrytype="phdthesis",
    ID="hinz2010exploring",
    cluster_id="10207225523023467263",
    scholar="http://scholar.google.com/scholar?cites=10207225523023467263&as_sdt=2005&sciodt=0,5&hl=en",
    local="Northcentral University",
    placex="",
))

immorlica2010a = DB(WorkUnrelated(
    2010, "Cooperation in Anonymous Dynamic Social Networks",
    display="immorlica",
    authors="Immorlica, Nicole and Lucier, Brendan and Rogers, Brian",
    place=FAKE,
    pp="241--242",
    entrytype="inproceedings",
    series="EC '10",
    isbn="978-1-60558-822-3",
    location="Cambridge, Massachusetts, USA",
    ID="Immorlica:2010:CAD:1807342.1807381",
    acm="1",
    placex="Proceedings of the 11th ACM Conference on Electronic Commerce",
))

institute2010a = DB(WorkUnrelated(
    2010, "The Strategic Management Maturity Model",
    display="institute",
    authors="BSI Balanced Scorecard Institute",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="BSI2010",
    placex="Smg, Strategy Managemetn Group",
))

itgi2010a = DB(WorkUnrelated(
    2010, "Control Objectives for Information and Related Technology",
    display="itgi",
    authors="ITGI",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="ITGI2010",
    placex="IT Governance Institute",
))

khoshkbarforoushha2010a = DB(WorkUnrelated(
    2010, "Towards a Metrics Suite for Measuring Composite Service Granularity Level Appropriateness",
    display="khoshkbarforoushha",
    authors="A. Khoshkbarforoushha and R. Tabein and P. Jamshidi and F. Shams",
    place=FAKE,
    pp="245-252",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="business data processing;software metrics;software reusability;abstract service;business value;composite service granularity level appropriateness measurement;context-independency;granular service;granularity appropriateness analysis;metrics suite;quantitative model;reusability;service granularity level evaluation;service-oriented analysis;service-oriented solution development;weighted granularity level appropriateness;Analytical models;Business;Complexity theory;Measurement;Service oriented architecture;Software;Measuring Composite Service Granularity Level;Metric;SOA Metric Suite;Web service Metrics",
    doi="10.1109/SERVICES.2010.68",
    issn="2378-3818",
    ID="5575839",
    ieee="1",
    placex="2010 6th World Congress on Services",
))

kim2010a = DB(WorkUnrelated(
    2010, "The Role of IT in Business Ecosystems",
    display="kim",
    authors="Kim, Hyeyoung and Lee, Jae-Nam and Han, Jaemin",
    place=FAKE,
    pp="151--156",
    entrytype="article",
    issue_date="May 2010",
    volume="53",
    number="5",
    month="may",
    issn="0001-0782",
    ID="Kim:2010:RBE:1735223.1735260",
    acm="1",
    placex="Commun. ACM",
))

klöckner2010a = DB(WorkUnrelated(
    2010, "Aligning Business Goals and User Goals by Engineering Hedonic Quality",
    display="klöckner",
    authors="Klöckner, Kerstin and Kohler, Kirstin and Kerkow, Daniel and Niebuhr, Sabine and Nass, Claudia",
    place=FAKE,
    pp="241--250",
    entrytype="inproceedings",
    series="EICS '10",
    isbn="978-1-4503-0083-4",
    location="Berlin, Germany",
    ID="Klockner:2010:ABG:1822018.1822056",
    acm="1",
    placex="Proceedings of the 2Nd ACM SIGCHI Symposium on Engineering Interactive Computing Systems",
))

kowalczyk2010a = DB(WorkSnowball(
    2010, "Aligning software-related strategies in multi- organizational settings",
    display="kowalczyk",
    authors="Kowalczyk, M. and Münch, J. and Katahira, M. and Kaneko, T. and Miyamoto, Y. and Koishi, Y.",
    place=ICSPPM,
    entrytype="article",
    note="cited By 2",
    ID="Kowalczyk2010",
    placex="Proceedings of the International Conference on Software Process and Product Measurement (IWSM/MetriKon/Mensura 2010)",
))

krasteva2010a = DB(WorkUnrelated(
    2010, "Experience-based approach for adoption of agile practices in software development projects",
    display="krasteva",
    authors="Krasteva, I. and Ilieva, S. and Dimov, A.",
    place=FAKE,
    pp="266-280",
    entrytype="article",
    volume="6051 LNCS",
    doi="10.1007/978-3-642-13094-6_22",
    note="cited By 7",
    ID="Krasteva2010266",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

kremmel2010a = DB(WorkUnrelated(
    2010, "Multiobjective Evolutionary Algorithm for Software Project Portfolio Optimization",
    display="kremmel",
    authors="Kremmel, Thomas and Kubalik, Ji?í and Biffl, Stefan",
    place=FAKE,
    pp="1389--1390",
    entrytype="inproceedings",
    series="GECCO '10",
    isbn="978-1-4503-0072-8",
    location="Portland, Oregon, USA",
    ID="Kremmel:2010:MEA:1830483.1830738",
    acm="1",
    placex="Proceedings of the 12th Annual Conference on Genetic and Evolutionary Computation",
))

lee2010a = DB(WorkUnrelated(
    2010, "A Requirements Elicitation Framework and Tool for Sourcing business-IT Aligned e-Services",
    display="lee",
    authors="Lee-Klenz, Soonhwa and Sampaio, Pedro and Wood-Harper, Trevor",
    place=FAKE,
    pp="111--117",
    entrytype="inproceedings",
    series="SAC '10",
    isbn="978-1-60558-639-7",
    location="Sierre, Switzerland",
    ID="Lee-Klenz:2010:REF:1774088.1774112",
    acm="1",
    placex="Proceedings of the 2010 ACM Symposium on Applied Computing",
))

leite2010a = DB(WorkUnrelated(
    2010, "ProMeProS: UM PROCESSO DE MELHORIA DE PROCESSOS DE SOFTWARE",
    display="leite",
    authors="Leite, Cássia Rodrigues de Carvalho Ferreira",
    place=FAKE,
    entrytype="article",
    ID="leite2010promepros",
    placex="",
))

lester2010a = DB(WorkUnrelated(
    2010, "Investigating the role of CMMI with expanding company size for small-to medium-sized enterprises",
    display="lester",
    authors="Lester, NG and Wilkie, F George and McFall, Donald and Ware, MP",
    place=JSEP,
    pp="17--31",
    entrytype="article",
    volume="22",
    number="1",
    publisher="Wiley Online Library",
    ID="lester2010investigating",
    cluster_id="10505469713876022799",
    scholar="http://scholar.google.com/scholar?cites=10505469713876022799&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Journal of Software: Evolution and Process",
))

malik2010a = DB(WorkUnrelated(
    2010, "Quantitative and qualitative analyses of requirements elaboration for early software size estimation",
    display="malik",
    authors="Malik, Ali Afzal",
    place=Book,
    entrytype="book",
    publisher="University of Southern California",
    ID="malik2010quantitative",
    cluster_id="18380665794697140974",
    scholar="http://scholar.google.com/scholar?cites=18380665794697140974&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

malik2010b = DB(WorkUnrelated(
    2010, "Comparative analysis of requirements elaboration of an industrial product",
    display="malik b",
    authors="Malik, Ali Afzal and Boehm, Barry and Ku, Yan and Yang, Ye",
    place=FAKE,
    pp="V1--46",
    entrytype="inproceedings",
    volume="1",
    organization="IEEE",
    ID="malik2010comparative",
    cluster_id="2813919223280174213",
    scholar="http://scholar.google.com/scholar?cites=2813919223280174213&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Technology and Engineering (ICSTE), 2010 2nd International Conference on",
))

mandić2010a = DB(WorkSnowball(
    2010, "Utilizing GQM+ Strategies for an organization-wide earned value analysis",
    display="mandić",
    authors="Mandic, Vladimir and Basili, Victor and Oivo, Markku and Harjumaa, Lasse and Markkula, Jouni",
    place=SEAA,
    pp="255--258",
    entrytype="inproceedings",
    doi="10.1109/SEAA.2010.33",
    art_number="5598105",
    note="cited By 2",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-78449277207&doi=10.1109%2fSEAA.2010.33&partnerID=40&md5=67093fe92c5dafae3a7c4c3674ac4f05",
    document_type="Conference Paper",
    source="Scopus",
    ID="Mandić2010255",
    scholar="http://scholar.google.com/scholar?cites=3108184027401056441&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE",
    cluster_id="3108184027401056441",
    scholar_ok=True,
    other1="pp 255258",
    placex="In: Proceedings of the 36th EUROMICRO conference on software engineering and advanced applications, 13 Sept 2010,",
))

mandić2010b = DB(WorkSnowball(
    2010, "Utilizing GQM+ Strategies for business value analysis: An approach for evaluating business goals",
    display="mandić b",
    authors="Mandić, Vladimir and Basili, Victor and Harjumaa, Lasse and Oivo, Markku and Markkula, Jouni",
    place=ESEM,
    entrytype="inproceedings",
    doi="10.1145/1852786.1852813",
    art_number="1852813",
    note="cited By 13",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-78149253973&doi=10.1145%2f1852786.1852813&partnerID=40&md5=26fcb1b5696be7437beaca23b4fb11fa",
    document_type="Conference Paper",
    source="Scopus",
    ID="Mandić2010",
    acm="1",
    placex="Proceedings of the 2010 ACM-IEEE International Symposium on Empirical Software Engineering and Measurement",
    pp="20",
    scholar="http://scholar.google.com/scholar?cites=341082888541335242&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    cluster_id="341082888541335242",
    scholar_ok=True,
    gs="1",
    other1="Italy, pp 110",
))

mandić2010c = DB(WorkUnrelated(
    2010, "Early empirical assessment of the practical value of GQM +strategies",
    display="mandić c",
    authors="Mandić, V. and Harjumaa, L. and Markkula, J. and Oivo, M.",
    pp="14-25",
    place=FAKE,
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    entrytype="article",
    volume="6195 LNCS",
    doi="10.1007/978-3-642-14347-2_3",
    note="cited By 7",
    ID="Mandi?201014",
    scholar="http://scholar.google.com/scholar?cites=7638361024929094617&as_sdt=2005&sciodt=0,5&hl=en",
))

mandić2010d = DB(WorkSnowball(
    2010, "SAS: A tool for the GQM+strategies grid derivation process",
    display="mandić d",
    authors="Mandić, V. and Oivo, M.",
    pp="291-305",
    place=FAKE,
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    entrytype="article",
    volume="6156 LNCS",
    doi="10.1007/978-3-642-13792-1_23",
    note="cited By 5",
    ID="Mandić2010291",
    scholar="http://scholar.google.com/scholar?cites=8738894608367720961&as_sdt=2005&sciodt=0,5&hl=en",
))

mandić2010e = DB(WorkUnrelated(
    2010, "An approach for evaluating business goals. Technical Report TR TR-TOL-2010-2802, University of Oulu",
    display="mandic e",
    authors="Mandic, V. and Basili, V.",
    place=FAKE,
    placex="Department of Information Processing Science",
    entrytype="article",
    note="cited By 1",
    ID="Mandic2010",
))

mandić2010f = DB(WorkUnrelated(
    2010, "An approach for evaluating business goals",
    display="mandic f",
    authors="Mandic, Vladimir and Basili, Victor",
    place=TechReport,
    entrytype="techreport",
    institution="Technical report, Technical Report TR TR-TOL-2010-2802, University of Oulu, Department of Information Processing Science",
    ID="mandic2010approach",
    cluster_id="1906476414681462280",
    scholar="http://scholar.google.com/scholar?cites=1906476414681462280&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

mandić2010g = DB(WorkUnrelated(
    2010, "What is flowing in lean software development?",
    display="mandić2010 g",
    authors="Mandić, Vladimir and Oivo, Markku and Rodríguez, Pilar and Kuvaja, Pasi and Kaikkonen, Harri and Turhan, Burak",
    place=FAKE,
    pp="72--84",
    entrytype="incollection",
    publisher="Springer",
    ID="mandic2010gflowing",
    cluster_id="1085662620234471522",
    scholar="http://scholar.google.com/scholar?cites=1085662620234471522&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Lean enterprise software and systems",
))

marca2010a = DB(WorkUnrelated(
    2010, "E-Business and Social Networks: Tapping Dynamic Niche Markets Using Language-Action and Artificial Intelligence",
    display="marca",
    authors="Marca, David A",
    place=FAKE,
    pp="3--23",
    entrytype="inproceedings",
    organization="Springer",
    ID="marca2010business",
    cluster_id="3029816640265494237",
    scholar="http://scholar.google.com/scholar?cites=3029816640265494237&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software and Data Technologies",
))

mashapa2010a = DB(WorkUnrelated(
    2010, "User Experience Evaluation Metrics for Usable Accounting Tools",
    display="mashapa",
    authors="Mashapa, Job and van Greunen, Darelle",
    place=FAKE,
    pp="170--181",
    entrytype="inproceedings",
    series="SAICSIT '10",
    isbn="978-1-60558-950-3",
    location="Bela Bela, South Africa",
    ID="Mashapa:2010:UEE:1899503.1899522",
    acm="1",
    placex="Proceedings of the 2010 Annual Research Conference of the South African Institute of Computer Scientists and Information Technologists",
))

mcloughlin2010a = DB(WorkSnowball(
    2010, "The Rosetta stone methodology - A benefits driven approach to software process improvement",
    display="mcloughlin",
    authors="McLoughlin, F. and Richardson, I.",
    pp="366-379",
    place=FAKE,
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    entrytype="article",
    volume="6156 LNCS",
    doi="10.1007/978-3-642-13792-1_28",
    note="cited By 0",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955436790&doi=10.1007%2f978-3-642-13792-1_28&partnerID=40&md5=dafacaf1767cfd1d3e7c9bdc4d3618f1",
    document_type="Conference Paper",
    source="Scopus",
    ID="McLoughlin2010366",
))

mcloughlin2010b = DB(WorkSnowball(
    2010, "The Rosetta Stone Methodology - A benefits-driven approach to SPI",
    display="mcloughlin b",
    authors="McLoughlin, F. and Richardson, I.",
    place=CCIS,
    pp="201-212",
    entrytype="article",
    volume="99 CCIS",
    doi="10.1007/978-3-642-15666-3_18",
    note="cited By 1",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-77957590654&doi=10.1007%2f978-3-642-15666-3_18&partnerID=40&md5=e06aaac5f23d90fcb4473a90273c06b2",
    document_type="Conference Paper",
    source="Scopus",
    ID="McLoughlin2010201",
))

mcloughlin2010c = DB(WorkUnrelated(
    2010, "The Rosetta Stone Methodology - A Benefits Driven Approach To Software Process Improvement",
    display="mcloughlin c",
    authors="McLoughlin, F. and Richardson, I.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="McLoughlin2010",
    placex="Profes 2010",
))

mellado2010a = DB(WorkUnrelated(
    2010, "A systematic review of security requirements engineering",
    display="mellado",
    authors="Daniel Mellado and Carlos Blanco and Luis E. Sánchez and Eduardo Fernández-Medina",
    place=CSI,
    pp="153 - 165",
    entrytype="article",
    volume="32",
    number="4",
    note="",
    issn="0920-5489",
    doi="https://doi.org/10.1016/j.csi.2010.01.006",
    link="https://www.sciencedirect.com/science/article/pii/S0920548910000255",
    keyword="Systematic review",
    ID="Mellado2010153",
    sciencedirect="1",
    placex="Computer Standards & Interfaces",
))

monteiro2010a = DB(WorkUnrelated(
    2010, "Defining a catalog of indicators to support process performance analysis",
    display="monteiro",
    authors="Monteiro, Luis Felipe Salin and de Oliveira, Kathia Mar{ç}al",
    place=JSEP,
    entrytype="article",
    publisher="Wiley Online Library",
    ID="monteiro2010defining",
    cluster_id="13701762143396136253",
    scholar="http://scholar.google.com/scholar?cites=13701762143396136253&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Journal of Software: Evolution and Process",
))

mäkiö2010a = DB(WorkUnrelated(
    2010, "OUTSHORE maturity model: Assistance for software offshore outsourcing decisions",
    display="mäkiö",
    authors="Mäkiö, Juho and Betz, Stafanie and Oberweis, Andreas",
    place=FAKE,
    pp="329--341",
    entrytype="incollection",
    publisher="Springer",
    ID="makio2010outshore",
    cluster_id="11450166452914102618",
    scholar="http://scholar.google.com/scholar?cites=11450166452914102618&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Collaborative Software Engineering",
))

müller2010a = DB(WorkUnrelated(
    2010, "Software Process Improvement as organizational change: A metaphorical analysis of the literature",
    display="müller",
    authors="Sune Dueholm Müller and Lars Mathiassen and Hans Henrik Balshøj",
    place=JSS,
    pp="2128 - 2146",
    entrytype="article",
    volume="83",
    number="11",
    note="Interplay between Usability Evaluation and Software Development",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2010.06.017",
    link="https://www.sciencedirect.com/science/article/pii/S0164121210001664",
    keyword="Literature review",
    ID="Müller20102128",
    sciencedirect="1",
    placex="Journal of Systems and Software",
    scholar="http://scholar.google.com/scholar?cites=17503453247437113979&as_sdt=2005&sciodt=0,5&hl=en",
))

nikula2010a = DB(WorkUnrelated(
    2010, "Empirical validation of the Classic Change Curve on a software technology change project",
    display="nikula",
    authors="Uolevi Nikula and Christian Jurvanen and Orlena Gotel and Donald C Gause",
    place=IST,
    pp="680 - 696",
    entrytype="article",
    volume="52",
    number="6",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.02.004",
    link="https://www.sciencedirect.com/science/article/pii/S0950584910000170",
    keyword="Organisational performance",
    ID="Nikula2010680",
    sciencedirect="1",
    placex="Information and Software Technology",
))

oliveira2010a = DB(WorkUnrelated(
    2010, "A comparative analysis of CMMI software project management by Brazilian, Indian and Chinese companies",
    display="oliveira",
    authors="de Oliveira, Saulo Barbará and Valle, Rogerio and Mahler, Cláudio Fernando",
    place=SQJ,
    pp="177--194",
    entrytype="article",
    volume="18",
    number="2",
    publisher="Springer",
    ID="de2010comparative",
    cluster_id="6043457506987012415",
    scholar="http://scholar.google.com/scholar?cites=6043457506987012415&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Quality Journal",
))

omg2010a = DB(WorkUnrelated(
    2010, "The business motivation model (BMM) V. 1.1. Object",
    display="omg",
    authors="OMG",
    place=FAKE,
    placex="Management Group (Object Management Group)",
))

parkinson2010a = DB(WorkUnrelated(
    2010, "Practitioner-based measurement: A collaborative approach",
    display="parkinson",
    authors="Parkinson, S.T. and Hierons, R.M. and Lycett, M. and Norman, M.",
    place=CACM,
    pp="142-147",
    entrytype="article",
    volume="53",
    number="3",
    doi="10.1145/1666420.1666456",
    note="cited By 1",
    ID="Parkinson2010142",
    placex="Communications of the ACM",
))

patanakul2010a = DB(WorkUnrelated(
    2010, "Exploring the concept of value creation in program planning and systems engineering processes",
    display="patanakul",
    authors="Patanakul, P. and Shenhar, A.",
    place=FAKE,
    pp="340-352",
    entrytype="article",
    volume="13",
    number="4",
    doi="10.1002/sys.20155",
    note="cited By 10",
    ID="Patanakul2010340",
    placex="Systems Engineering",
))

petersen2010a = DB(WorkUnrelated(
    2010, "The effect of moving from a plan-driven to an incremental software development approach with agile practices: An industrial case study",
    display="petersen",
    authors="Petersen, K. and Wohlin, C.",
    place=ESE,
    pp="654-693",
    entrytype="article",
    volume="15",
    number="6",
    doi="10.1007/s10664-010-9136-6",
    note="cited By 51",
    ID="Petersen2010654",
))

petersen2010b = DB(WorkUnrelated(
    2010, "Software process improvement through the Lean Measurement (SPI-LEAM) method",
    display="petersen b",
    authors="Petersen, K. and Wohlin, C.",
    place=JSS,
    pp="1275-1287",
    entrytype="article",
    volume="83",
    number="7",
    doi="10.1016/j.jss.2010.02.005",
    note="cited By 46",
    ID="Petersen20101275",
))

pino2010a = DB(WorkUnrelated(
    2010, "Assessment methodology for software process improvement in small organizations",
    display="pino",
    authors="Francisco J. Pino and César Pardo and Félix García and Mario Piattini",
    place=IST,
    pp="1044 - 1061",
    entrytype="article",
    volume="52",
    number="10",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.04.004",
    link="https://www.sciencedirect.com/science/article/pii/S0950584910000777",
    keyword="SPI",
    ID="Pino20101044",
    sciencedirect="1",
    placex="Information and Software Technology",
))

pino2010b = DB(WorkUnrelated(
    2010, "Using Scrum to guide the execution of software process improvement in small organizations",
    display="pino b",
    authors="Pino, Francisco J and Pedreira, Oscar and García, Félix and Luaces, Miguel Rodríguez and Piattini, Mario",
    place=JSS,
    pp="1662--1677",
    entrytype="article",
    volume="83",
    number="10",
    publisher="Elsevier",
    ID="pino2010using",
    cluster_id="1428035976173142851",
    scholar="http://scholar.google.com/scholar?cites=1428035976173142851&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Journal of systems and software",
))

riel2010a = DB(WorkUnrelated(
    2010, "Qualification and certification for the competitive edge in Integrated Design",
    display="riel",
    authors="A. Riel and S. Tichkiewitch and R. Messnarz",
    place=FAKE,
    pp="279 - 289",
    entrytype="article",
    volume="2",
    number="4",
    note="Competitive Design: \{CIRP\} Design Conference, Cranfield, United KingdomCIRP Design Conference",
    issn="1755-5817",
    doi="https://doi.org/10.1016/j.cirpj.2010.04.005",
    link="https://www.sciencedirect.com/science/article/pii/S1755581710000404",
    keyword="Certification",
    ID="Riel2010279",
    sciencedirect="1",
    placex="\{CIRP\} Journal of Manufacturing Science and Technology",
))

rodríguez2010a = DB(WorkUnrelated(
    2010, "Software Process Improvement for SMEs using OMM",
    display="rodríguez",
    authors="Rodríguez, Jessica",
    place=FAKE,
    entrytype="misc",
    ID="rodriguez2010software",
    placex="",
))

rolland2010a = DB(WorkUnrelated(
    2010, "Business Process Lines to Deal with the Variability",
    display="rolland",
    authors="C. Rolland and S. Nurcan",
    place=FAKE,
    pp="1-10",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="business data processing;organisational aspects;Map;business process lines;business process variability;electricity supply industry;organizational level model;organizational settings;representation system;software development;Business process re-engineering;Companies;Electricity supply industry;Environmental management;Kernel;Knowledge engineering;Management information systems;Manufacturing processes;Portfolios;Programming",
    doi="10.1109/HICSS.2010.88",
    issn="1530-1605",
    ID="5428532",
    ieee="1",
    placex="2010 43rd Hawaii International Conference on System Sciences",
    organization="IEEE",
    gs="1",
))

romero2010a = DB(WorkUnrelated(
    2010, "ERP: Drilling for Profit in the Oil and Gas Industry",
    display="romero",
    authors="Romero, Jorge A. and Menon, Nirup and Banker, Rajiv D. and Anderson, Mark",
    place=FAKE,
    pp="118--121",
    entrytype="article",
    issue_date="July 2010",
    volume="53",
    number="7",
    month="jul",
    issn="0001-0782",
    ID="Romero:2010:EDP:1785414.1785448",
    acm="1",
    placex="Commun. ACM",
))

rosemann2010a = DB(WorkUnrelated(
    2010, "The six core elements of business process management.",
    display="rosemann",
    authors="M Rosemann, vom Brocke J",
    place=FAKE,
    placex="vom Brocke J, Rosemann M (eds) Handbook on business process management, vol 1. Springer, Heidelberg",
))

sarcia2010a = DB(WorkUnrelated(
    2010, "Is GQM+strategies really applicable as is to non-software development domains?",
    display="sarcia",
    authors="Sarcia', S.A.",
    place=ESEM,
    entrytype="article",
    doi="10.1145/1852786.1852844",
    art_number="1852844",
    note="cited By 10",
    ID="Sarcia'2010",
    scholar="http://scholar.google.com/scholar?cites=18340962611795161582&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Proceedings of the 2010 ACM-IEEE International Symposium on Empirical Software Engineering and Measurement",
    other1="software engineering and measurement, Bolzano-Bozen, Italy,",
    other2="pp 14",
))

shu2010a = DB(WorkUnrelated(
    2010, "Measurement and analysis of process audit: A case study",
    display="shu",
    authors="Shu, Fengdi and Li, Qi and Wang, Qing and Zhang, Haopeng",
    place=ICSE,
    pp="285--296",
    entrytype="inproceedings",
    organization="Springer",
    ID="shu2010measurement",
    cluster_id="1972877809701793784",
    scholar="http://scholar.google.com/scholar?cites=1972877809701793784&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
))

softex2010a = DB(WorkUnrelated(
    2010, "MPS.BR",
    journal= "softex",
    display="softex",
    authors="SOFTEX",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="SOFTEX2010",
    placex="",
))

sun2010a = DB(WorkSnowball(
    2010, "Business-oriented software process improvement based on \CMMI\ using \QFD",
    display="sun",
    authors="Yan Sun and Xiaoqing (Frank) Liu",
    place=IST,
    pp="79 - 91",
    entrytype="article",
    volume="52",
    number="1",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2009.08.003",
    link="https://www.sciencedirect.com/science/article/pii/S0950584909001220",
    keyword="Relationship matrix",
    ID="Sun201079",
    sciencedirect="1",
    placex="Information and Software Technology",
    scholar="http://scholar.google.com/scholar?cites=4881529965332269987&as_sdt=2005&sciodt=0,5&hl=en",
))

tisselli2010a = DB(WorkUnrelated(
    2010, "Thinkflickrthink: A Case Study on Strategic Tagging",
    display="tisselli",
    authors="Tisselli, Eugenio",
    place=FAKE,
    pp="141--145",
    entrytype="article",
    issue_date="August 2010",
    volume="53",
    number="8",
    month="aug",
    issn="0001-0782",
    ID="Tisselli:2010:TCS:1787234.1787270",
    acm="1",
    placex="Commun. ACM",
))

tjørnehøj2010a = DB(WorkUnrelated(
    2010, "Improvisation during process-technology adoption: a longitudinal study of a software firm",
    display="tjørnehøj",
    authors="Tjørnehøj, Gitte and Mathiassen, Lars",
    place=FAKE,
    pp="20--34",
    entrytype="article",
    volume="25",
    number="1",
    publisher="Springer",
    ID="tjornehoj2010improvisation",
    cluster_id="18374028747705230951",
    scholar="http://scholar.google.com/scholar?cites=18374028747705230951&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Journal of Information Technology",
))

unterkalmsteiner2010a = DB(WorkUnrelated(
    2010, "Extended Material to Evaluation and Measurement of Software Process ImprovementA Systematic Literature Review",
    display="unterkalmsteiner",
    authors="Unterkalmsteiner, M and Gorschek, Tony and Islam, AKMM and Cheng, Chow Kian and Permadi, Rahadian Bayu and Feldt, Robert",
    place=FAKE,
    entrytype="misc",
    ID="unterkalmsteiner2010extended",
    cluster_id="7059711458164801125",
    scholar="http://scholar.google.com/scholar?cites=7059711458164801125&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

vanut2010a = DB(WorkUnrelated(
    2010, "A tool for IT process construction",
    display="vanut",
    authors="{}vanut, Bo{}tjan and Bajec, Marko",
    place=IST,
    pp="397--410",
    entrytype="article",
    volume="52",
    number="4",
    publisher="Elsevier",
    ID="vzvanut2010tool",
    cluster_id="9532085647863335493",
    scholar="http://scholar.google.com/scholar?cites=9532085647863335493&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information and Software Technology",
))

vuk2010a = DB(WorkUnrelated(
    2010, "Adoption of business process orientation practices: Slovenian and Croatian survey",
    display="vuk",
    authors="Vuk{}i{c?}, Vesna and {}temberger, Mojca and others",
    place=FAKE,
    pp="5--19",
    entrytype="article",
    volume="1",
    number="1-2",
    publisher="Versita",
    ID="vukvsic2010adoption",
    cluster_id="10815219668476755713",
    scholar="http://scholar.google.com/scholar?cites=10815219668476755713&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Business Systems Research",
))

wangenheim2010a = DB(WorkUnrelated(
    2010, "Best practice fusion of CMMI-DEV v1.2 (PP, PMC, SAM) and \PMBOK\ 2008",
    display="wangenheim",
    authors="Christiane Gresse von Wangenheim and Djoni Antonio da Silva and Luigi Buglione and Rafael Scheidt and Rafael Prikladnicki",
    place=IST,
    pp="749 - 757",
    entrytype="article",
    volume="52",
    number="7",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.03.008",
    link="https://www.sciencedirect.com/science/article/pii/S0950584910000480",
    keyword="Basic process areas",
    ID="vonWangenheim2010749",
    sciencedirect="1",
    placex="Information and Software Technology",
))

weerd2010a = DB(WorkUnrelated(
    2010, "Incremental method evolution in global software product management: A retrospective case study",
    display="weerd",
    authors="Inge van de Weerd and Sjaak Brinkkemper and Johan Versendaal",
    place=IST,
    pp="720 - 732",
    entrytype="article",
    volume="52",
    number="7",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2010.03.002",
    link="https://www.sciencedirect.com/science/article/pii/S095058491000042X",
    keyword="Distributed development",
    ID="vandeWeerd2010720",
    sciencedirect="1",
    placex="Information and Software Technology",
))

winter2010a = DB(WorkUnrelated(
    2010, "\SPI\ success factors within product usability evaluation",
    display="winter",
    authors="Jeff Winter and Kari Rönkkö",
    place=JSS,
    pp="2059 - 2072",
    entrytype="article",
    volume="83",
    number="11",
    note="Interplay between Usability Evaluation and Software Development",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2010.04.066",
    link="https://www.sciencedirect.com/science/article/pii/S0164121210001408",
    keyword="User experience",
    ID="Winter20102059",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

ye2010a = DB(WorkUnrelated(
    2010, "A Fast Variable Precision Template Matching Algorithm Based on Hybrid Genetic Algorithm",
    display="ye",
    authors="Ye, Mao-yi and You, Fu-cheng",
    place=FAKE,
    pp="1--3",
    entrytype="inproceedings",
    organization="IEEE",
    ID="ye2010fast",
    placex="Multimedia Technology (ICMT), 2010 International Conference on",
))

zahran2010a = DB(WorkUnrelated(
    2010, "Business and Cost Justification of Software Process Improvement - ROI from SPI",
    display="zahran",
    authors="Zahran, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Zahran2010",
    placex="International Software Process Association Conference, Brighton, England (1996)",
))

zalzala2010a = DB(WorkUnrelated(
    2010, "Software process improvement for the airline industry",
    display="zalzala",
    authors="Zalzala, A. and Udaipurwala, A.",
    place=ECIME,
    pp="397-408",
    entrytype="inproceedings",
    note="cited By 0",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84900804698&partnerID=40&md5=1ae1d1be9212fc154b5144d9e22088ae",
    document_type="Conference Paper",
    source="Scopus",
    ID="Zalzala2010397",
    scopus="1",
    isbn="978-1-906638-72-6",
    webofscience="1",
    placex="PROCEEDINGS OF THE 4TH EUROPEAN CONFERENCE ON INFORMATION MANAGEMENT AND EVALUATION",
    elcompendex="1",
))

zhang2010a = DB(WorkUnrelated(
    2010, "Capturing Antagonistic Stakeholder Value Propositions in Value-Based Software Development.",
    display="zhang",
    authors="Zhang, Du",
    place=FAKE,
    pp="12--18",
    entrytype="inproceedings",
    ID="zhang2010capturing",
    cluster_id="1097166577944984033",
    scholar="http://scholar.google.com/scholar?cites=1097166577944984033&as_sdt=2005&sciodt=0,5&hl=en",
    placex="SEKE",
))

zhang2010b = DB(WorkUnrelated(
    2010, "A fuzzy-based method for evaluating the trustworthiness of software processes",
    display="zhang b",
    authors="Zhang, Haopeng and Shu, Fengdi and Yang, Ye and Wang, Xu and Wang, Qing",
    place=ICSE,
    pp="297--308",
    entrytype="inproceedings",
    organization="Springer",
    ID="zhang2010fuzzy",
    cluster_id="9419717857347968417",
    scholar="http://scholar.google.com/scholar?cites=9419717857347968417&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
))

zowghi2010a = DB(WorkUnrelated(
    2010, "A Framework for the Elicitation and Analysis of Information Technology Service Requirements and Their Alignment with Enterprise Business Goals",
    display="zowghi",
    authors="D. Zowghi and Z. Jin",
    place=FAKE,
    pp="269-272",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="Web services;business data processing;information technology;knowledge acquisition;service industries;Web service;co-value creation;enterprise business goal;information technology service requirement;service oriented computing;systematic identification;alignment;analysise;elicitation;service requirements",
    doi="10.1109/COMPSACW.2010.54",
    issn="",
    ID="5615805",
    ieee="1",
    placex="2010 IEEE 34th Annual Computer Software and Applications Conference Workshops",
    organization="IEEE",
    gs="1",
))
