# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

accenture2004a = DB(WorkUnrelated(
    2004, "Managing IT investments in the high-performance business",
    display="accenture",
    authors="accenture",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="accenture2004",
    placex="Strategic Information Technology Effectiveness (SITE)",
))

anacleto2004a = DB(WorkUnrelated(
    2004, "A method for process assessment in small software companies",
    display="anacleto",
    authors="Anacleto, A. and Von Wangenheim, C.G. and Salviano, C.F. and Savi, R.",
    pp="69--76",
    place=FAKE,
    placex="4th International SPICE Conference on Process Assessment and Improvement",
    entrytype="article",
    note="cited By 15",
    ID="Anacleto200469",
))

anacleto2004b = DB(WorkUnrelated(
    2004, "Experiences gained from applying ISO/IEC 15504 to small software companies in Brazil",
    display="anacleto b",
    authors="Anacleto, A. and Von Wangenheim, C.G. and Salviano, C.F. and Savi, R.",
    pp="33--37",
    place=FAKE,
    placex="4th International SPICE Conference on Process Assessment and Improvement",
    entrytype="article",
    note="cited By 28",
    ID="Anacleto200433",
))

ardimento2004a = DB(WorkUnrelated(
    2004, "Multiview Framework for Goal Oriented Measurement Plan Design",
    display="ardimento",
    authors="Ardimento, Pasquale and Baldassarre, Maria Teresa and Caivano, Danilo and Visaggio, Giuseppe",
    place=PROFES,
    pp="159--173",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_12",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

aversano2004a = DB(WorkUnrelated(
    2004, "Introducing Quality System in Small and Medium Enterprises: An Experience Report",
    display="aversano",
    authors="Aversano, Lerina and Canfora, Gerardo and Capasso, Giovanni and Di Lucca, Giuseppe A. and Visaggio, Corrado A.",
    place=PROFES,
    pp="131--145",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_10",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

beck2004a = DB(WorkUnrelated(
    2004, "Extreme programming explained: embrace change",
    display="beck",
    authors="K Beck, C Andres",
    place=FAKE,
    other1="Boston, MA",
    placex="Addison-Wesley,",
))

boehm2004a = DB(WorkUnrelated(
    2004, "Bala",
    display="boehm",
    authors="Boehm, B. and Turner, R.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Boehm2004",
    placex="Bala",
))

böckle2004a = DB(WorkUnrelated(
    2004, "Calculating ROI for software product lines",
    display="böckle",
    authors="Böckle, G. and Clements, P. and McGregor, J.D. and Muthig, D. and Schmid, K.",
    place=IEEES,
    pp="23--31",
    entrytype="article",
    volume="21",
    number="3",
    doi="10.1109/MS.2004.1293069",
    note="cited By 110",
    ID="Böckle200423",
    placex="IEEE Software",
))

caffery2004a = DB(WorkUnrelated(
    2004, "Northern Ireland Software Industry Survey",
    display="caffery",
    authors="Mc Caffery, F. and Wilkie, F.G. and McFall, D. and Lester, N.",
    pp="159--161",
    place=FAKE,
    placex="Proceedings of Fourth International SPICE Conference on Process Assessment and Improvement",
    entrytype="article",
    note="cited By 1",
    ID="McCaffery2004",
))

capell2004a = DB(WorkUnrelated(
    2004, "Benefits of improvement efforts",
    display="capell",
    authors="Capell, P",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Capell2004",
    placex="SEI SPECIAL REPORT CMU",
))

card2004a = DB(WorkUnrelated(
    2004, "Research directions in software process improvement",
    display="card",
    authors="Card, D.N.",
    place=FAKE,
    pp="238",
    entrytype="article",
    volume="1",
    note="cited By 18",
    ID="Card2004238",
    placex="Proceedings - International Computer Software and Applications Conference",
))

casey2004a = DB(WorkUnrelated(
    2004, "A practical application of the IDEAL model",
    display="casey",
    authors="Casey, Valentine and Richardson, Ita",
    place=SPIP,
    pp="123--132",
    entrytype="article",
    volume="9",
    number="3",
    publisher="Wiley Online Library",
    ID="casey2004practical",
    cluster_id="14240618123670173976",
    scholar="http://scholar.google.com/scholar?cites=14240618123670173976&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process: Improvement and Practice",
))

cater2004a = DB(WorkUnrelated(
    2004, "Low-rigour, rapid software process assessments for small software development firms",
    display="cater",
    authors="Cater-Steel, A.P.",
    place=SEC,
    pp="368--377",
    entrytype="article",
    volume="2004",
    doi="10.1109/ASWEC.2004.1290490",
    note="cited By 23",
    ID="Cater-Steel2004368",
    placex="Proceedings of the Australian Software Engineering Conference, ASWEC",
))

cater2004b = DB(WorkUnrelated(
    2004, "An evaluation of software development practice and assessment-based process improvement in small software development firms",
    display="cater b",
    authors="Cater-Steel, Aileen",
    place=Thesis,
    entrytype="phdthesis",
    ID="cater2004evaluation",
    cluster_id="8322987274008536048",
    scholar="http://scholar.google.com/scholar?cites=8322987274008536048&as_sdt=2005&sciodt=0,5&hl=en",
    local="Griffith University",
    placex="",
))

cater2004c = DB(WorkUnrelated(
    2004, "After the assessment: actions and reactions of 22 small Australian firms",
    display="cater c",
    authors="Cater-Steel, Aileen and Toleman, Mark and Rout, Terry",
    place=FAKE,
    pp="54--63",
    entrytype="inproceedings",
    organization="Critical Software SA/SPICE User Group",
    ID="cater2004after",
    cluster_id="2238618385588393664",
    scholar="http://scholar.google.com/scholar?cites=2238618385588393664&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Proceedings of the 4th International SPICE Conference on Process Assessment and ImprovementSPICE 2004",
))

chrissis2004a = DB(WorkUnrelated(
    2004, "CMMI: Guidelines for Process Integration and Product Improvement",
    display="chrissis",
    authors="Chrissis, M.B. and Konrad, M. and Shrum, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 687",
    ID="Chrissis2004",
    placex="Addison-Wesley Publishing Company",
))

davis2004a = DB(WorkUnrelated(
    2004, "Using Measurement Data in a TSPSM Project",
    display="davis",
    authors="Davis, Noopur and Mullaney, Julia and Carrington, David",
    place=SPIP,
    pp="91--101",
    entrytype="inproceedings",
    editor="Dingsøyr, Torgeir",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-30181-3_9",
    springer="1",
    placex="Software Process Improvement",
))

erdogmus2004a = DB(WorkUnrelated(
    2004, "Guest editors' introduction: Return on investment",
    display="erdogmus",
    authors="Erdogmus, H. and Favaro, J. and Strigel, W.",
    place=IEEES,
    pp="18--22",
    entrytype="article",
    volume="21",
    number="3",
    doi="10.1109/MS.2004.1293068",
    note="cited By 28",
    ID="Erdogmus200418",
    placex="IEEE Software",
))

fernandes2004a = DB(WorkUnrelated(
    2004, "Using RUP for Process-Oriented Organisations",
    display="fernandes",
    authors="Fernandes, João M. and Duarte, Francisco J.",
    place=PROFES,
    pp="348--362",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_25",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

goethert2004a = DB(WorkUnrelated(
    2004, "Applications of the Indicator Template for Measurement and Analys",
    display="goethert",
    authors="Goethert, W. and Siviy, J.",
    place=FAKE,
    entrytype="article",
    note="cited By 5",
    ID="Goethert2004",
    placex="Carnegie Mellon University, Software Eng",
))

gorschek2004a = DB(WorkUnrelated(
    2004, "Packaging software process improvement issues: a method and a case study",
    display="gorschek",
    authors="Gorschek, Tony and Wohlin, Claes",
    place=FAKE,
    pp="1311--1344",
    entrytype="article",
    volume="34",
    number="14",
    publisher="Wiley Online Library",
    ID="gorschek2004packaging",
    cluster_id="13434671154375543572",
    scholar="http://scholar.google.com/scholar?cites=13434671154375543572&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software: Practice and Experience",
    doi="10.1002/spe.615",
    note="cited By 32",
))

grant2004a = DB(WorkUnrelated(
    2004, "Special section",
    display="grant",
    authors="Kevin Grant and David Edgar and Mike Jordan",
    place=FAKE,
    pp="449 -- 456",
    entrytype="article",
    volume="24",
    number="6",
    note="",
    issn="0268-4012",
    doi="https://doi.org/10.1016/j.ijinfomgt.2004.08.005",
    link="https://www.sciencedirect.com/science/article/pii/S0268401204000921",
    ID="Grant2004449",
    sciencedirect="1",
    placex="International Journal of Information Management",
))

guerrero2004a = DB(WorkUnrelated(
    2004, "Adopting the SW-CMM in a Small IT Organization",
    display="guerrero",
    authors="Guerrero, Felipe and Eterovic, Yadran",
    place=IEEES,
    pp="29--35",
    entrytype="article",
    volume="21",
    number="4",
    publisher="IEEE",
    ID="guerrero2004adopting",
    cluster_id="11640469187417357474",
    scholar="http://scholar.google.com/scholar?cites=11640469187417357474&as_sdt=2005&sciodt=0,5&hl=en",
    placex="IEEE software",
))

haaker2004a = DB(WorkUnrelated(
    2004, "Balancing Strategic Interests and Technological Requirements for Mobile Services",
    display="haaker",
    authors="Haaker, Timber and Faber, Edward and Bouwman, Harry",
    place=FAKE,
    pp="609--618",
    entrytype="inproceedings",
    series="ICEC '04",
    isbn="1-58113-930-6",
    location="Delft, The Netherlands",
    ID="Haaker:2004:BSI:1052220.1052298",
    acm="1",
    placex="Proceedings of the 6th International Conference on Electronic Commerce",
))

hansen2004a = DB(WorkUnrelated(
    2004, "Prescription, description, reflection: the shape of the software process improvement field",
    display="hansen",
    authors="Bo Hansen and Jeremy Rose and Gitte Tjørnehøj",
    place=FAKE,
    pp="457 -- 472",
    entrytype="article",
    volume="24",
    number="6",
    note="",
    issn="0268-4012",
    doi="https://doi.org/10.1016/j.ijinfomgt.2004.08.007",
    link="https://www.sciencedirect.com/science/article/pii/S0268401204000945",
    keyword="Literature review",
    ID="Hansen2004457",
    sciencedirect="1",
    placex="International Journal of Information Management",
    scholar="http://scholar.google.com/scholar?cites=10770119955145613305&as_sdt=2005&sciodt=0,5&hl=en",
))

hansen2004b = DB(WorkUnrelated(
    2004, "Knowledge Mapping: A Technique for Identifying Knowledge Flows in Software Organisations",
    display="hansen b",
    authors="Hansen, Bo Hansen and Kautz, Karlheinz",
    place=SPIP,
    pp="126--137",
    entrytype="inproceedings",
    editor="Dingsøyr, Torgeir",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-30181-3_12",
    springer="1",
    placex="Software Process Improvement",
))

hjalmarsson2004a = DB(WorkUnrelated(
    2004, "Att etablera och vidmakthålla förbättringsverksamhet: Behovet av koordination och interaktion vid förändring av systemutvecklingsverksamheter",
    display="hjalmarsson",
    authors="Hjalmarsson, Anders",
    place=Thesis,
    entrytype="phdthesis",
    ID="hjalmarsson2004att",
    cluster_id="3890780300222766365",
    scholar="http://scholar.google.com/scholar?cites=3890780300222766365&as_sdt=2005&sciodt=0,5&hl=en",
    local="Institutionen för datavetenskap",
    placex="",
))

hjalmarsson2004b = DB(WorkUnrelated(
    2004, "Att etablera och vidmakthålla förbättringsverksamhet",
    display="hjalmarsson b",
    authors="Hjalmarsson, Anders",
    place=FAKE,
    entrytype="article",
    ID="hjalmarsson2004att",
    cluster_id="12903822031910392999",
    scholar="http://scholar.google.com/scholar?cites=12903822031910392999&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Behovet av koordination och interaktion vid förändring av systemutvecklingsverksamheter, lic. avhandling, IDA, Linköpings universitet",
))

holz2004a = DB(WorkUnrelated(
    2004, "Research on Learning Software Organizations -- Past, Present, and Future",
    display="holz",
    authors="Holz, Harald and Melnik, Grigori",
    place=FAKE,
    pp="1--6",
    entrytype="inproceedings",
    editor="Melnik, Grigori and Holz, Harald",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-25983-1_1",
    springer="1",
    placex="Advances in Learning Software Organizations",
))

hyde2004a = DB(WorkUnrelated(
    2004, "Intangible benefits of CMM-based software process improvement",
    display="hyde",
    authors="Hyde, K. and Wilson, D.",
    place=SPIP,
    pp="217--228",
    entrytype="article",
    volume="9",
    number="4",
    doi="10.1002/spip.205",
    note="cited By 21",
    ID="Hyde2004217",
    placex="Software Process Improvement and Practice",
))

isoiec2004a = DB(WorkUnrelated(
    2004, "Information technologyprocess assessmentPart 4: Guidance on use for process improvement and process capability determination",
    display="isoiec",
    authors="ISOIEC",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="ISOIEC2004",
    placex="ISO/IEC 15504-4:2004",
))

isoiec2004b = DB(WorkUnrelated(
    2004, "Information Technology - Amendment 2 to ISO/IEC 12207",
    display="isoiec b",
    authors="isoiec",
    place=FAKE,
    entrytype="article",
    note="cited By 2",
    ID="isoiec2004",
    placex="ISO/IEC PDAM 12207",
))

iversen2004a = DB(WorkUnrelated(
    2004, "Managing risk in software process improvement: AN action research approach",
    display="iversen",
    authors="Iversen, J.H. and Mathiassen, L. and Nielsen, P.A.",
    pp="395--434",
    place=FAKE,
    placex="MIS Quarterly: Management Information Systems",
    entrytype="article",
    volume="28",
    number="3",
    note="cited By 146",
    ID="Iversen2004395",
))

jaufman2004a = DB(WorkUnrelated(
    2004, "Suitability of state of the art methods for interdisciplinary system development in automotive industry",
    display="jaufman",
    authors="Jaufman, O. and Przewoznik, S.",
    place=FAKE,
    pp="78--82",
    entrytype="article",
    note="cited By 4",
    ID="Jaufman200478",
    placex="WISER 2004 - ACM Workshop on Interdisciplinary Software Engineering Research",
))

jedlitschka2004a = DB(WorkUnrelated(
    2004, "Towards Comprehensive Experience-Based Decision Support",
    display="jedlitschka",
    authors="Jedlitschka, Andreas and Pfahl, Dietmar",
    place=SPIP,
    pp="34--45",
    entrytype="inproceedings",
    editor="Dingsøyr, Torgeir",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-30181-3_4",
    springer="1",
    placex="Software Process Improvement",
    volume="3281",
    note="cited By 2",
    other1="November 10-12, 2004 Trondheim, Norway, Lecture Notes in Computer Science 3281,",
    other2="pp. 34-45",
))

jokela2004a = DB(WorkUnrelated(
    2004, "Evaluating the user-centredness of development organisations: conclusions and implications from empirical usability capability maturity assessments",
    display="jokela",
    authors="Timo Jokela",
    place=FAKE,
    pp="1095 -- 1132",
    entrytype="article",
    volume="16",
    number="6",
    note="",
    issn="0953-5438",
    doi="https://doi.org/10.1016/j.intcom.2004.07.006",
    link="https://www.sciencedirect.com/science/article/pii/S0953543804000815",
    keyword="Usability capability",
    ID="Jokela20041095",
    sciencedirect="1",
    placex="Interacting with Computers",
))

kaplan2004a = DB(WorkUnrelated(
    2004, "Strategy Maps: Converting Intangible Assets Into Tangible Outcomes",
    display="kaplan",
    authors="Kaplan, R.S. and Norton, D.P.",
    place=FAKE,
    entrytype="article",
    note="cited By 1050",
    ID="Kaplan2004",
    placex="Boston, Harvard Business School",
))

kaplan2004b = DB(WorkUnrelated(
    2004, "Strategy maps: converting intangible assets into tangible outcomes",
    display="kaplan b",
    authors="RS Kaplan, DP Norton",
    place=FAKE,
    placex="Harvard Business School Press, Boston, MA",
))

karinsalo2004a = DB(WorkUnrelated(
    2004, "Software Reuse and the Test Development Process: A Combined Approach",
    display="karinsalo",
    authors="Karinsalo, Mikko and Abrahamsson, Pekka",
    place=FAKE,
    pp="59--68",
    entrytype="inproceedings",
    editor="Bosch, Jan and Krueger, Charles",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-27799-6_6",
    springer="1",
    placex="Software Reuse: Methods, Techniques, and Tools",
))

katz2004a = DB(WorkUnrelated(
    2004, "From aspectual requirements to proof obligations for aspect-oriented systems",
    display="katz",
    authors="Katz, Shmuel and Rashid, Awais",
    place=FAKE,
    pp="48--57",
    entrytype="inproceedings",
    organization="IEEE",
    ID="katz2004aspectual",
    cluster_id="11419762633775007925",
    scholar="http://scholar.google.com/scholar?cites=11419762633775007925&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Requirements Engineering Conference, 2004. Proceedings. 12th IEEE International",
))

katz2004b = DB(WorkUnrelated(
    2004, "PROBE: From Requirements and Design to Proof Obligations for Aspect-Oriented Systems",
    display="katz b",
    authors="Katz, Shmuel and Rashid, Awais",
    place=FAKE,
    entrytype="article",
    publisher="Citeseer",
    ID="katz2004probe",
    cluster_id="1975009324973387269",
    scholar="http://scholar.google.com/scholar?cites=1975009324973387269&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Computing Department, Lancaster University, Lancaster COMP-002-2004",
))

kauppinen2004a = DB(WorkUnrelated(
    2004, "Implementing requirements engineering processes throughout organizations: success factors and challenges",
    display="kauppinen",
    authors="Marjo Kauppinen and Matti Vartiainen and Jyrki Kontio and Sari Kujala and Reijo Sulonen",
    place=IST,
    pp="937 -- 953",
    entrytype="article",
    volume="46",
    number="14",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2004.04.002",
    link="https://www.sciencedirect.com/science/article/pii/S0950584904000692",
    keyword="Action research",
    ID="Kauppinen2004937",
    sciencedirect="1",
    placex="Information and Software Technology",
    scholar="http://scholar.google.com/scholar?cites=5784926019705824565&as_sdt=2005&sciodt=0,5&hl=en",
))

kautz2004a = DB(WorkUnrelated(
    2004, "Understanding the implementation of software process improvement innovations in software organizations",
    display="kautz",
    authors="Kautz, Karlheinz and Nielsen, Peter Axel",
    place=FAKE,
    pp="3--22",
    entrytype="article",
    volume="14",
    number="1",
    publisher="Wiley Online Library",
    ID="kautz2004understanding",
    cluster_id="15073932125956591546",
    scholar="http://scholar.google.com/scholar?cites=15073932125956591546&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information Systems Journal",
))

komi2004a = DB(WorkUnrelated(
    2004, "Development and Evaluation of Software Process Improvement Methods",
    display="komi",
    authors="Komi-Sirvio, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Komi2004",
    placex="Espoo 2004, p. 535. VTT Publications",
))

larsson2004a = DB(WorkUnrelated(
    2004, "Selecting CMMI Appraisal Classes Based on Maturity and Openness",
    display="larsson",
    authors="Larsson, Stig and Ekdahl, Fredrik",
    place=PROFES,
    pp="457--470",
    entrytype="inproceedings",
    editor="Bomarius, Frankan d Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_33",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

lehtola2004a = DB(WorkUnrelated(
    2004, "Requirements Prioritization Challenges in Practice",
    display="lehtola",
    authors="Lehtola, Laura and Kauppinen, Marjo and Kujala, Sari",
    place=PROFES,
    pp="497--508",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_36",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

letier2004a = DB(WorkUnrelated(
    2004, "Reasoning About Partial Goal Satisfaction for Requirements and Design Engineering",
    display="letier",
    authors="Letier, Emmanuel and van Lamsweerde, Axel",
    place=FAKE,
    pp="53--62",
    entrytype="article",
    issue_date="November 2004",
    volume="29",
    number="6",
    month="oct",
    issn="0163-5948",
    ID="Letier:2004:RPG:1041685.1029905",
    acm="1",
    placex="SIGSOFT Softw. Eng. Notes",
))

linden2004a = DB(WorkUnrelated(
    2004, "Software Product Family Evaluation",
    display="linden",
    authors="van der Linden, Frank and Bosch, Jan and Kamsties, Erik and Känsälä, Kari and Krzanik, Lech and Obbink, Henk",
    place=FAKE,
    pp="352--369",
    entrytype="inproceedings",
    editor="van der Linden, Frank J.",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24667-1_27",
    springer="1",
    placex="Software Product-Family Engineering",
))

little2004a = DB(WorkUnrelated(
    2004, "Value creation and capture: A model of the software development process",
    display="little",
    authors="Little, T.",
    place=IEEES,
    pp="48--53",
    entrytype="article",
    volume="21",
    number="3",
    doi="10.1109/MS.2004.1293072",
    note="cited By 17",
    ID="Little200448",
    placex="IEEE Software",
))

lowy2004a = DB(WorkUnrelated(
    2004, "The Power of the 2â×â2 Matrix",
    display="lowy",
    authors="Lowy, A. and Hood, P.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Lowy2004",
    placex="Jossey-Bass: San Francisco",
))

makipaa2004a = DB(WorkUnrelated(
    2004, "Mass Customization and Beyond in Software Engineering--Developing a Framework for Mass Customized Adaptive Software",
    display="makipaa",
    authors="Makipaa, Marko and Mattila, Jussi",
    place=FAKE,
    entrytype="inproceedings",
    volume="12",
    organization="Citeseer",
    ID="makipaa2004mass",
    cluster_id="7324433790968449270",
    scholar="http://scholar.google.com/scholar?cites=7324433790968449270&as_sdt=2005&sciodt=0,5&hl=en",
    placex="The First Finnish Mass Customization and Personalization",
))

malotaux2004a = DB(WorkUnrelated(
    2004, "Chapter 6 - Evolutionary Development: How to deliver Quality On Time in Software Development and Systems Engineering Projects",
    display="malotaux",
    authors="Niels Malotaux",
    place=FAKE,
    pp="77 -- 100",
    entrytype="incollection",
    editor="Ganssle, Jack",
    publisher="Newnes",
    edition="",
    address="Burlington",
    series="Embedded Technology",
    isbn="978-0-7506-7606-9",
    doi="https://doi.org/10.1016/B978-075067606-9/50010-2",
    link="https://www.sciencedirect.com/science/article/pii/B9780750676069500102",
    ID="Malotaux200477",
    sciencedirect="1",
    placex="The Firmware Handbook",
))

mcgrath2004a = DB(WorkUnrelated(
    2004, "Next Generation Product Development: How to Increase Productivity",
    display="mcgrath",
    authors="McGrath, M.E.",
    place=FAKE,
    entrytype="article",
    note="cited By 39",
    ID="McGrath2004",
    placex="Cut Costs, and Reduce Cycle Times",
))

mcgrath2004b = DB(WorkUnrelated(
    2004, "Next Generation Product Development: How to IncreaseProductivity, Cut Costs, and Reduce Cycle Times",
    display="mcgrath b",
    authors="Michael E McGrath",
    place=Book,
    other1="McGraw-Hill",
    placex="Book",
))

mehra2004a = DB(WorkUnrelated(
    2004, "Purchasing management and business competitiveness in the coming decade",
    display="mehra",
    authors="Mehra, S. and Inman, R.A.",
    place=FAKE,
    pp="710--718",
    entrytype="article",
    volume="15",
    number="7",
    doi="10.1080/09537280412331298247",
    note="cited By 20",
    ID="Mehra2004710",
    placex="Production Planning and Control",
))

nch2004a = DB(WorkUnrelated(
    2004, "Software project control centers: concepts and approaches. J Syst",
    display="nch",
    authors="J Mu¨nch, J Heidrich",
    place=FAKE,
    placex="Software 70(1):319",
))

nguyen2004a = DB(WorkUnrelated(
    2004, "A formalism for conformance analysis and its applications",
    display="nguyen",
    authors="Nguyen, Tien Nhut and Munson, Ethan V",
    place=ICSE,
    pp="330--339",
    entrytype="inproceedings",
    organization="IEEE",
    ID="nguyen2004formalism",
    cluster_id="14786983970671137879",
    scholar="http://scholar.google.com/scholar?cites=14786983970671137879&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Engineering and Formal Methods, 2004. SEFM 2004. Proceedings of the Second International Conference on",
))

oecd2004a = DB(WorkUnrelated(
    2004, "Organization for Economic Cooperation and Development: OECD Information Technology Outlook",
    display="oecd",
    authors="OECD",
    place=FAKE,
    entrytype="article",
    note="cited By 442",
    ID="OECD2004",
    placex="Organization for Economic Cooperation and Development",
))

pedersen2004a = DB(WorkUnrelated(
    2004, "Software Thinking Improvement Learning Performance Improving Lessons",
    display="pedersen",
    authors="Pedersen, Keld",
    place=SPIP,
    pp="102--113",
    entrytype="inproceedings",
    editor="Dingsøyr, Torgeir",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-30181-3_10",
    springer="1",
    placex="Software Process Improvement",
))

pmi2004a = DB(WorkUnrelated(
    2004, "PMBOK - A Guide to the Project Management Body of Knowledge",
    display="pmi",
    authors="PMI",
    place=FAKE,
    entrytype="article",
    note="cited By 17",
    ID="PMI2004",
    placex="Project Management Institute: 3rd edn",
))

rittinghouse2004a = DB(WorkUnrelated(
    2004, "1 - Understanding the \SPMO",
    display="rittinghouse",
    authors="John W. Rittinghouse",
    place=FAKE,
    pp="1 -- 30",
    entrytype="incollection",
    editor="Rittinghouse, John W.",
    publisher="Digital Press",
    edition="",
    address="Burlington",
    isbn="978-1-55558-313-2",
    doi="https://doi.org/10.1016/B978-155558313-2/50004-2",
    link="https://www.sciencedirect.com/science/article/pii/B9781555583132500042",
    ID="Rittinghouse20041",
    sciencedirect="1",
    placex="Managing Software Deliverables",
))

rodr2004a = DB(WorkUnrelated(
    2004, "Effective Software Project Management Education through Simulation Models: An Externally Replicated Experiment",
    display="rodr",
    authors="Rodr{i?}guez, D. and Satpathy, M. and Pfahl, D.",
    place=PROFES,
    pp="287--301",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_21",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

ruhe2004a = DB(WorkUnrelated(
    2004, "Intelligent Support for Software Release Planning",
    display="ruhe",
    authors="Amandeep and Ruhe, Günther and Stanford, Mark",
    place=PROFES,
    pp="248--262",
    entrytype="inproceedings",
    editor="Bomarius, Frank and Iida, Hajimu",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-24659-6_18",
    springer="1",
    placex="Product Focused Software Process Improvement",
))

schwaber2004a = DB(WorkUnrelated(
    2004, "Agile project management with scrum",
    display="schwaber",
    authors="K Schwaber",
    place=FAKE,
    placex="Microsoft Press, Redmond, WA",
))

sei2004a = DB(WorkUnrelated(
    2004, "Process Maturity Profile: CMMI® v1.1, SCAMPI SM v1.1 Class A Appraisal Results",
    display="sei",
    authors="SEI",
    place=FAKE,
    placex="Process Maturity Profile",
    entrytype="article",
    note="cited By 17",
    ID="SEI2004",
))

serrano2004a = DB(WorkUnrelated(
    2004, "State of the art and future of research in software process improvement",
    display="serrano",
    authors="M. Serrano",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Serrano2004",
    placex="Proceedings of the 28th Annual International Computer Software and Applications Conference COMPSAC'04, Hong Kong, September 28-30, 2004",
))

solingen2004a = DB(WorkUnrelated(
    2004, "Measuring the ROI of software process improvement",
    display="solingen",
    authors="Van Solingen, R.",
    place=IEEES,
    pp="32--38",
    entrytype="article",
    volume="21",
    number="3",
    doi="10.1109/MS.2004.1293070",
    note="cited By 57",
    ID="VanSolingen200432",
    placex="IEEE Software",
    publisher="IEEE",
))

sommerville2004a = DB(WorkUnrelated(
    2004, "Software Engineering 7th Edition",
    display="sommerville",
    authors="Sommerville, I.",
    place=FAKE,
    entrytype="article",
    note="cited By 22",
    ID="Sommerville2004",
    placex="Addison Wesley Publishing Company",
))

stalhane2004a = DB(WorkUnrelated(
    2004, "Root Cause Analysis and Gap Analysis - A Tale of Two Methods",
    display="stalhane",
    authors="Stalhane, T.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Stalhane2004",
    placex="Springer",
))

stålhane2004a = DB(WorkUnrelated(
    2004, "Root cause analysis and gap analysis a tale of two methods",
    display="stålhane",
    authors="Stålhane, T.",
    place=FAKE,
    pp="150--160",
    entrytype="article",
    volume="3281",
    note="cited By 5",
    ID="Stålhane2004150",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

trienekens2004a = DB(WorkSnowball(
    2004, "Business objectives as drivers for process improvement: Practices and experiences at Thales Naval the Netherlands (TNNL)",
    display="trienekens",
    authors="Trienekens, Jos JM and Kusters, Rob J and Rendering, Ben and Stokla, Kees",
    pp="33--48",
    place= FAKE,
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    entrytype="inproceedings",
    volume="3080",
    note="cited By 0",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-35048900944&partnerID=40&md5=2652625f0089eb261045aefcf83026c2",
    document_type="Article",
    source="Scopus",
    ID="Trienekens200433",
    scholar="http://scholar.google.com/scholar?cites=8937266215208447980&as_sdt=2005&sciodt=0,5&hl=en",
    organization="Springer",
    cluster_id="8937266215208447980",
    scholar_ok=True,
))

wilkie2004a = DB(WorkUnrelated(
    2004, "The centre for software process technologies: A model for process improvement in geographical regions with small software industries",
    display="wilkie",
    authors="Wilkie, F.G. and McFall, D. and McCaffery, F.",
    pp="5",
    place=FAKE,
    placex="Proceedings of 16th Software Engineering Process Group Conference",
    entrytype="article",
    note="cited By 4",
    ID="Wilkie2004",
))
