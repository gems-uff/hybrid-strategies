# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

ISOIEC2006a = DB(WorkUnrelated(
    2006, "Information technology - Process assessment - Part 3: Guidance on performing an assessment",
    display="ISOIEC",
    authors="ISOIEC",
    place=FAKE,
    placex="Information Technology - Process Assessment",
    entrytype="article",
    note="cited By 251",
    ID="IT2004",
))

aagotnes2006a = DB(WorkUnrelated(
    2006, "On the Logic of Coalitional Games",
    display="aagotnes",
    authors="Agotnes, Thomas and van der Hoek, Wiebe and Wooldridge, Michael",
    place=FAKE,
    pp="153--160",
    entrytype="inproceedings",
    series="AAMAS '06",
    isbn="1-59593-303-4",
    location="Hakodate, Japan",
    ID="Agotnes:2006:LCG:1160633.1160659",
    acm="1",
    placex="Proceedings of the Fifth International Joint Conference on Autonomous Agents and Multiagent Systems",
))

abb2006a = DB(WorkUnrelated(
    2006, "ABB Annual Report 2006 - Sustainability Review - Power and Productivity for a Better World",
    display="abb",
    authors="ABB",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="ABB2006",
    placex="ABB",
))

andersen2006a = DB(WorkUnrelated(
    2006, "E-government maturity models: Extension of the Layne and Lee model",
    display="andersen",
    authors="Kim Viborg Andersen and Helle Zinner Henriksen",
    place=FAKE,
    pp="236 -- 248",
    entrytype="article",
    volume="23",
    number="2",
    note="",
    issn="0740-624X",
    doi="https://doi.org/10.1016/j.giq.2005.11.008",
    link="https://www.sciencedirect.com/science/article/pii/S0740624X05000973",
    ID="Andersen2006236",
    sciencedirect="1",
    placex="Government Information Quarterly",
    sciencedirect2015="1",
))

ardimento2006a = DB(WorkUnrelated(
    2006, "Assessing multiview framework (MF) comprehensibility and efficiency: A replicated experiment",
    display="ardimento",
    authors="Ardimento, P. and Baldassarre, M.T. and Caivano, D. and Visaggio, G.",
    place=IST,
    pp="313--322",
    entrytype="article",
    volume="48",
    number="5",
    doi="10.1016/j.infsof.2005.09.010",
    note="cited By 6",
    ID="Ardimento2006313",
))

asgarkhani2006a = DB(WorkUnrelated(
    2006, "Current trends in strategic management of ICTs",
    display="asgarkhani",
    authors="Asgarkhani, M.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Asgarkhani2006",
    placex="IEEE international conference on management of innovation and technology",
))

basili2006a = DB(WorkUnrelated(
    2006, "The TAME Project: Towards Improvement-Oriented Software Environments",
    display="basili",
    authors="Basili, V.R. and H.D. Rombach",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Basili1988",
    placex="IEEE Trans. Software Eng., Vol. 14, No. 6, Pp. 758-773",
))

bayer2006a = DB(WorkUnrelated(
    2006, "Improving the development of e-business systems by introducing process-based software product lines",
    display="bayer",
    authors="Bayer, J. and Kose, M. and Ocampo, A.",
    place=FAKE,
    pp="348--361",
    entrytype="article",
    volume="4034 LNCS",
    note="cited By 8",
    ID="Bayer2006348",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

bayer2006b = DB(WorkUnrelated(
    2006, "Improving the Development of e-Business Systems by Introducing",
    display="bayer b",
    authors="Bayer, J., Kose, M., Ocampo, A.",
    place=FAKE,
    other1="In: Münch, J., Vierimaa, M. (eds.).",
    other2="Proceedings of the 7th International Conference on Product-Focused Software Process Improvement (PROFES'2006),",
    other3="Amsterdam, The Netherlands, Lecture Notes in Computer Science 4034, pp. 348-361",
    placex="Process-Based Software Product Lines.",
))

bent2006a = DB(WorkUnrelated(
    2006, "A quality instrument for the enterprise architecture development process",
    display="bent",
    authors="van den Bent, Bas",
    place=IC,
    entrytype="article",
    ID="van2006quality",
    cluster_id="13423750184475062745",
    scholar="http://scholar.google.com/scholar?cites=13423750184475062745&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information Science",
))

berry2006a = DB(WorkUnrelated(
    2006, "Measurement and decision making",
    display="berry",
    authors="Berry, M. and Aurum, A.",
    place=Book,
    pp="155--177",
    entrytype="book",
    doi="10.1007/3-540-29263-2_8",
    note="cited By 4",
    ID="Berry2006155",
    placex="Value-Based Software Engineering",
))

biffl2006a = DB(WorkUnrelated(
    2006, "Value-based software engineering",
    display="biffl",
    authors="Biffl, S. and Aurum, A. and Boehm, B. and Erdogmus, H. and Grünbacher, P.",
    place=Book,
    pp="1--388",
    entrytype="book",
    doi="10.1007/3-540-29263-2",
    note="cited By 201",
    ID="Biffl20061",
    placex="Value-Based Software Engineering",
))

biró2006a = DB(WorkUnrelated(
    2006, "Special issue with selected industrial experience papers of EuroSPI22005",
    display="biró",
    authors="Biró, Miklós and Messnarz, Richard",
    place=SPIP,
    pp="215--218",
    entrytype="article",
    volume="11",
    number="3",
    publisher="Wiley Online Library",
    ID="biro2006special",
    cluster_id="16409948185301573692",
    scholar="http://scholar.google.com/scholar?cites=16409948185301573692&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process: Improvement and Practice",
))

boehm2006a = DB(WorkUnrelated(
    2006, "Value-based software engineering: Overview and agenda",
    display="boehm",
    authors="Boehm, B.W.",
    place=Book,
    pp="3--14",
    entrytype="book",
    doi="10.1007/3-540-29263-2_1",
    note="cited By 46",
    ID="Boehm20063",
    placex="Value-Based Software Engineering",
))

canfora2006a = DB(WorkUnrelated(
    2006, "Applying a framework for the improvement of software process maturity",
    display="canfora",
    authors="Canfora, G. and García, F. and Piattini, M. and Ruiz, F. and Visaggio, C.A.",
    place=FAKE,
    pp="283--304",
    entrytype="article",
    volume="36",
    number="3",
    doi="10.1002/spe.697",
    note="cited By 14",
    ID="Canfora2006283",
    placex="Software - Practice and Experience",
))

cater2006a = DB(WorkUnrelated(
    2006, "Process improvement for small firms: An evaluation of the RAPID assessment-based method",
    display="cater",
    authors="Cater-Steel, Aileen and Toleman, Mark and Rout, Terry",
    place=IST,
    pp="323--334",
    entrytype="article",
    volume="48",
    number="5",
    publisher="Elsevier",
    ID="cater2006process",
    cluster_id="16182669652479205732",
    scholar="http://scholar.google.com/scholar?cites=16182669652479205732&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information and Software Technology",
    sciencedirect2015="1",
))

cater2006b = DB(WorkUnrelated(
    2006, "SPI Program Retrospective: evaluating long-term benefits for small firms",
    display="cater b",
    authors="Cater-Steel, Aileen and Rout, Terry",
    place=FAKE,
    pp="3--5",
    entrytype="inproceedings",
    ID="cater2006spi",
    cluster_id="4512288659363388396",
    scholar="http://scholar.google.com/scholar?cites=4512288659363388396&as_sdt=2005&sciodt=0,5&hl=en",
    placex="6th International SPICE Conference, Luxembourg",
))

cater2006c = DB(WorkUnrelated(
    2006, "SPI assessment retrospective: evaluating long-term benefits for small firms",
    display="cater c",
    authors="Cater-Steel, Aileen and Rout, Terry",
    place=ICSPICD,
    pp="41--48",
    entrytype="inproceedings",
    organization="Centre de Recherche Public Henri Tudor",
    ID="cater2006spi",
    placex="6th International SPICE Conference: Software Process Improvement and Capability Determination",
))

choi2006a = DB(WorkUnrelated(
    2006, "Applying tools of Six Sigma and PSP for definition and schedule management of process",
    display="choi",
    authors="Choi, Seung-Yong and Kim, Jeong-Ah",
    place=FAKE,
    pp="923--935",
    entrytype="article",
    volume="33",
    number="11",
    publisher="Korean Institute of Information Scientists and Engineers",
    ID="choi2006applying",
    placex="Journal of KIISE: Software and Applications",
))

cmmi2006a = DB(WorkUnrelated(
    2006, "CMMI for Development",
    display="cmmi",
    authors="cmmi",
    place=FAKE,
    entrytype="article",
    note="cited By 239",
    ID="cmmi2006",
    placex="Version 1.2. Technical Report CMU/SEI-2006-TR-008. Software Engineering Institute, Carnegie Mellon University",
))

cmmi2006b = DB(WorkUnrelated(
    2006, "SEI: CMMI for Development Version 1.2 SEI",
    display="cmmi b",
    authors="CMMI",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="cmmi2006",
    placex="SEI",
))

cmusei2006a = DB(WorkUnrelated(
    2006, "CMMI for Development version 1.2",
    display="cmusei",
    authors="cmusei",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="cmusei2006",
    placex="CMU/SEI-2006-TR-008 2006",
))

cox2006a = DB(WorkUnrelated(
    2006, "A Contingency View of Organizational Infrastructure Requirements Engineering",
    display="cox",
    authors="Cox, Karl and Bleistein, Steven J. and Reynolds, Peter and Thorogood, Alan",
    place=FAKE,
    pp="1497--1504",
    entrytype="inproceedings",
    series="SAC '06",
    isbn="1-59593-108-2",
    location="Dijon, France",
    ID="Cox:2006:CVO:1141277.1141628",
    acm="1",
    placex="Proceedings of the 2006 ACM Symposium on Applied Computing",
))

damas2006a = DB(WorkUnrelated(
    2006, "Scenarios, Goals, and State Machines: A Win-win Partnership for Model Synthesis",
    display="damas",
    authors="Damas, Christophe and Lambeau, Bernard and van Lamsweerde, Axel",
    place=FAKE,
    pp="197--207",
    entrytype="inproceedings",
    series="SIGSOFT '06/FSE-14",
    isbn="1-59593-468-5",
    location="Portland, Oregon, USA",
    ID="Damas:2006:SGS:1181775.1181800",
    acm="1",
    placex="Proceedings of the 14th ACM SIGSOFT International Symposium on Foundations of Software Engineering",
))

damm2006a = DB(WorkUnrelated(
    2006, "Faults-slip-through - A concept for measuring the efficiency of the test process",
    display="damm",
    authors="Damm, L.-O. and Lundberg, L. and Wohlin, C.",
    place=SPIP,
    pp="47--59",
    entrytype="article",
    volume="11",
    number="1",
    doi="10.1002/spip.253",
    note="cited By 37",
    ID="Damm200647",
))

damm2006b = DB(WorkUnrelated(
    2006, "Results from introducing component-level test automation and Test-Driven Development",
    display="damm b",
    authors="Damm, Lars-Orla and Lundberg, Lars",
    place=FAKE,
    pp="1001-1014",
    entrytype="article",
    volume="79",
    number="7",
    month="JUL",
    unique_id="ISI:000238790300011",
    ID="ISI:000238790300011",
    placex="JOURNAL OF SYSTEMS AND SOFTWARE",
    sciencedirect2015="1",
))

davis2006a = DB(WorkUnrelated(
    2006, "Effectiveness of requirements elicitation techniques: empirical results derived from a systematic review. In: Proceedings of the 14th IEEE international conference on requirements engineering (RE 2006)",
    display="davis",
    authors="Davis, A.M. and Tubío, Ó.D. and Hickey, A.M. and Juzgado, N.J. and Moreno, A.M.",
    place=FAKE,
    placex="pp : 176185",
    entrytype="article",
    note="cited By 1",
    ID="Davis2006",
))

debarr2006a = DB(WorkUnrelated(
    2006, "Closing the Gap: Automated Screening of Tax Returns to Identify Egregious Tax Shelters",
    display="debarr",
    authors="DeBarr, Dave and Eyler-Walker, Zach",
    place=FAKE,
    pp="11--16",
    entrytype="article",
    issue_date="June 2006",
    volume="8",
    number="1",
    month="jun",
    issn="1931-0145",
    ID="DeBarr:2006:CGA:1147234.1147237",
    acm="1",
    placex="SIGKDD Explor. Newsl.",
))

denger2006a = DB(WorkUnrelated(
    2006, "A Comprehensive Framework for Customizing Quality Assurance Techniques",
    display="denger",
    authors="Denger, C. and Elberzhager, F.",
    place=FAKE,
    entrytype="article",
    note="cited By 6",
    ID="Denger2006",
    placex="IESE-Report",
))

ekdahl2006a = DB(WorkUnrelated(
    2006, "Experience report: Using internal CMMI appraisals to institutionalize software development performance improvement",
    display="ekdahl",
    authors="Ekdahl, F. and Larsson, S.",
    place=SEAA,
    pp="216--222",
    entrytype="conference",
    doi="10.1109/EUROMICRO.2006.37",
    art_number="1690143",
    note="cited By 10",
    ID="Ekdahl2006216",
    placex="Proceedings - 32nd Euromicro Conference on Software Engineering and Advanced Applications, SEAA",
))

emam2006a = DB(WorkUnrelated(
    2006, "An Overview of Process Improvement in Small Settings",
    display="emam",
    authors="El Emam, Khaled",
    place=WE,
    pp="261--275",
    entrytype="incollection",
    publisher="Springer",
    ID="el2006overview",
    cluster_id="10762984489691300881",
    scholar="http://scholar.google.com/scholar?cites=10762984489691300881&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Web Engineering",
))

fernándezmedina2006a = DB(WorkUnrelated(
    2006, "Access control and audit model for the multidimensional modeling of data warehouses",
    display="fernándezmedina",
    authors="Eduardo Fernández-Medina and Juan Trujillo and Rodolfo Villarroel and Mario Piattini",
    place=FAKE,
    pp="1270 -- 1289",
    entrytype="article",
    volume="42",
    number="3",
    note="",
    issn="0167-9236",
    doi="https://doi.org/10.1016/j.dss.2005.10.008",
    link="https://www.sciencedirect.com/science/article/pii/S0167923605001570",
    keyword="UML",
    ID="FernándezMedina20061270",
    sciencedirect="1",
    placex="Decision Support Systems",
))

genus2006a = DB(WorkUnrelated(
    2006, "Firm strategies for risk management in innovation",
    display="genus",
    authors="Genus, A. and Coles, A.-M.",
    place=FAKE,
    pp="113--126",
    entrytype="article",
    volume="10",
    number="2",
    note="cited By 10",
    ID="Genus2006113",
    placex="International Journal of Innovation Management",
))

gibson2006a = DB(WorkUnrelated(
    2006, "Performance Results of CMMI-Based Process Improvement",
    display="gibson",
    authors="Gibson, D.L. and Goldenson, D.R. and Kost, K.",
    place=FAKE,
    entrytype="article",
    note="cited By 3",
    ID="Gibson2006",
    placex="Technical Report CMU/SEI-2006-TR-004",
))

gorschek2006a = DB(WorkUnrelated(
    2006, "Requirements Abstraction Model",
    display="gorschek",
    authors="Gorschek, Tony and Wohlin, Claes",
    place=FAKE,
    pp="79--101",
    entrytype="article",
    month="Mar",
    day="01",
    volume="11",
    number="1",
    ID="Gorschek2006",
    springer="1",
    placex="Requirements Engineering",
    springer2015="1",
))

gorschek2006b = DB(WorkUnrelated(
    2006, "Requirements engineering supporting technical product management",
    display="gorschek b",
    authors="Gorschek, Tony",
    place=Thesis,
    entrytype="phdthesis",
    ID="gorschek2006requirements",
    cluster_id="11677362890625672455",
    scholar="http://scholar.google.com/scholar?cites=11677362890625672455&as_sdt=2005&sciodt=0,5&hl=en",
    local="Blekinge Institute of Technology",
    placex="",
))

gorschek2006c = DB(WorkUnrelated(
    2006, "Success Evaluation and Measures in Software Process Improvement",
    display="gorschek c",
    authors="Gorschek, Tony and Åsfält, Pär",
    place=FAKE,
    entrytype="misc",
    ID="gorschek2006success",
    placex="",
))

gorschek2006d = DB(WorkUnrelated(
    2006, "A model for technology transfer in practice",
    display="gorschek d",
    authors="Gorschek, T. and Garre, P. and Larsson, S. and Wohlin, C.",
    place=IEEES,
    pp="88--95",
    entrytype="article",
    volume="23",
    number="6",
    doi="10.1109/MS.2006.147",
    note="cited By 116",
    ID="Gorschek200688",
    placex="IEEE Software",
))

grünbacher2006a = DB(WorkUnrelated(
    2006, "Stakeholder value proposition elicitation and reconciliation",
    display="grünbacher",
    authors="Grünbacher, P. and Köszegi, S. and Biffl, S.",
    place=Book,
    pp="133--154",
    entrytype="book",
    doi="10.1007/3-540-29263-2_7",
    note="cited By 14",
    ID="Grünbacher2006133",
    placex="Value-Based Software Engineering",
))

guest2006a = DB(WorkUnrelated(
    2006, "How many interviews are enough? an experiment with data saturation and variability",
    display="guest",
    authors="Guest, G., Bunce, A., Johnson, L.",
    place=FAKE,
    placex="Field Methods, 18",
    entrytype="article",
    ID="Guest2006",
))

harrison2006a = DB(WorkUnrelated(
    2006, "Risk and the economic value of the software producer",
    display="harrison",
    authors="Harrison, W.",
    place=Book,
    pp="91--105",
    entrytype="book",
    doi="10.1007/3-540-29263-2_5",
    note="cited By 1",
    ID="Harrison200691",
    placex="Value-Based Software Engineering",
))

horkoff2006a = DB(WorkUnrelated(
    2006, "Analyzing Trust in Technology Strategies",
    display="horkoff",
    authors="Horkoff, Jennifer and Yu, Eric and Liu, Lin",
    place=FAKE,
    pp="9:1--9:12",
    entrytype="inproceedings",
    series="PST '06",
    isbn="1-59593-604-1",
    location="Markham, Ontario, Canada",
    ID="Horkoff:2006:ATT:1501434.1501446",
    acm="1",
    placex="Proceedings of the 2006 International Conference on Privacy, Security and Trust: Bridge the Gap Between PST Technologies and Business Services",
))

iso2006a = DB(WorkUnrelated(
    2006, "Information Technology - Process Assessment - Part 5: An exemplar Process Assessment Model",
    display="iso",
    authors="ISO/IEC 15504, ISO/IECJTC1/SC7",
    place=FAKE,
    placex="Information Technology - Process Assessment",
    entrytype="article",
    note="cited By 251",
    ID="IT2003",
))

isoiec2006a = DB(WorkUnrelated(
    2006, "Information technology - Process assessment - Parts 1-5",
    display="isoiec",
    authors="ISOIEC",
    place=FAKE,
    entrytype="article",
    note="cited By 251",
    ID="ISOIEC2006",
    placex="ISO/IEC 15504:2003: International Standards Organization",
))

issac2006a = DB(WorkUnrelated(
    2006, "An instrument for the measurement of customer perceptions of quality management in the software industry: An empirical study in India",
    display="issac",
    authors="Issac, G. and Rajendran, C. and Anantharaman, R.N.",
    place=SQJ,
    pp="291--308",
    entrytype="article",
    volume="14",
    number="4",
    doi="10.1007/s11219-006-0037-2",
    note="cited By 20",
    ID="Issac2006291",
    placex="Software Quality Journal",
))

iversen2006a = DB(WorkUnrelated(
    2006, "Problems in measuring effectiveness in software process improvement: A longitudinal study of organizational change at Danske Data",
    display="iversen",
    authors="Iversen, J. and Ngwenyama, O.",
    place=FAKE,
    pp="30--43",
    entrytype="article",
    volume="26",
    number="1",
    doi="10.1016/j.ijinfomgt.2005.10.006",
    note="cited By 25",
    ID="Iversen200630",
    placex="International Journal of Information Management",
))

jantunen2006a = DB(WorkUnrelated(
    2006, "Towards global market-driven software development processes: an industrial case study",
    display="jantunen",
    authors="Jantunen, Sami and Smolander, Kari",
    place=FAKE,
    pp="94--100",
    entrytype="inproceedings",
    organization="ACM",
    ID="jantunen2006towards",
    acm2015="1",
    placex="Proceedings of the 2006 international workshop on Global software development for the practitioner",
))

jha2006a = DB(WorkUnrelated(
    2006, "Problem Frames Approach to Web Services Requirements",
    display="jha",
    authors="Jha, Anju",
    place=FAKE,
    pp="33--40",
    entrytype="inproceedings",
    series="IWAAPF '06",
    isbn="1-59593-406-5",
    location="Shanghai, China",
    ID="Jha:2006:PFA:1138670.1138677",
    acm="1",
    placex="Proceedings of the 2006 International Workshop on Advances and Applications of Problem Frames",
))

jönsson2006a = DB(WorkUnrelated(
    2006, "Benchmarking k-nearest neighbour imputation with homogeneous Likert data",
    display="jönsson",
    authors="Jönsson, Per and Wohlin, Claes",
    place=ESE,
    pp="463",
    entrytype="article",
    month="May",
    day="31",
    volume="11",
    number="3",
    issn="1573-7616",
    doi="10.1007/s10664-006-9001-9",
    ID="Jönsson2006",
    springer2015="1",
    placex="Empirical Software Engineering",
))

kaplan2006a = DB(WorkUnrelated(
    2006, "Alignment: Using the Balanced Scorecard to Create Corporate Synergies",
    display="kaplan",
    authors="Kaplan, R.S. and Norton, D.P.",
    place=FAKE,
    entrytype="article",
    note="cited By 282",
    ID="Kaplan2006",
    placex="Harvard Business Press",
))

karlström2006a = DB(WorkUnrelated(
    2006, "Integrating agile software development into stage-gate managed product development",
    display="karlström",
    authors="Karlström, Daniel and Runeson, Per",
    place=ESE,
    pp="203--225",
    entrytype="article",
    month="Jun",
    day="01",
    volume="11",
    number="2",
    issn="1573-7616",
    doi="10.1007/s10664-006-6402-8",
    ID="Karlström2006",
    springer2015="1",
    placex="Empirical Software Engineering",
))

kishore2006a = DB(WorkUnrelated(
    2006, "Enterprise integration using the agent paradigm: foundations of multi-agent-based integrative business information systems",
    display="kishore",
    authors="Rajiv Kishore and Hong Zhang and R. Ramesh",
    place=FAKE,
    pp="48 -- 78",
    entrytype="article",
    volume="42",
    number="1",
    note="",
    issn="0167-9236",
    doi="https://doi.org/10.1016/j.dss.2004.09.011",
    link="https://www.sciencedirect.com/science/article/pii/S0167923604002155",
    keyword="Conceptual modeling",
    ID="Kishore200648",
    sciencedirect="1",
    placex="Decision Support Systems",
    sciencedirect2015="1",
))

komuro2006a = DB(WorkUnrelated(
    2006, "Experiences of applying SPC techniques to software development processes",
    display="komuro",
    authors="Komuro, Mutsumi",
    place=ICSE,
    pp="577--584",
    entrytype="inproceedings",
    organization="ACM",
    ID="komuro2006experiences",
    gs="1",
    placex="Proceedings of the 28th international conference on Software engineering",
    acm2015="1",
))

kwak2006a = DB(WorkUnrelated(
    2006, "Benefits, obstacles, and future of six sigma approach",
    display="kwak",
    authors="Kwak, Young Hoon and Anbari, Frank T",
    place=FAKE,
    pp="708--715",
    entrytype="article",
    volume="26",
    number="5-6",
    publisher="Elsevier",
    ID="kwak2006benefits",
    cluster_id="16961248342193391968",
    scholar="http://scholar.google.com/scholar?cites=16961248342193391968&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Technovation",
))

leih2006a = DB(WorkUnrelated(
    2006, "The impact of the Sarbanes-Oxley Act on IT project management",
    display="leih",
    authors="Leih, Michael J",
    place=FAKE,
    pp="13",
    entrytype="article",
    volume="8",
    number="3",
    publisher="Association for Information Systems",
    ID="leih2006impact",
    cluster_id="11753970966294523513",
    scholar="http://scholar.google.com/scholar?cites=11753970966294523513&as_sdt=2005&sciodt=0,5&hl=en",
    placex="JITTA: Journal of Information Technology Theory and Application",
))

li2006a = DB(WorkUnrelated(
    2006, "Assessing 3-D integrated software development processes: A new benchmark",
    display="li",
    authors="Li, Mingshu",
    place=FAKE,
    pp="15--38",
    entrytype="inproceedings",
    organization="Springer",
    ID="li2006assessing",
    cluster_id="1748080141810175497",
    scholar="http://scholar.google.com/scholar?cites=1748080141810175497&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process Workshop",
))

li2006b = DB(WorkUnrelated(
    2006, "An empirical study of variations in COTS-based software development processes in the Norwegian IT industry",
    display="li b",
    authors="Li, Jingyue and Bjørnson, Finn Olav and Conradi, Reidar and Kampenes, Vigdis B.",
    place=ESE,
    pp="433--461",
    entrytype="article",
    month="Sep",
    day="01",
    volume="11",
    number="3",
    issn="1573-7616",
    doi="10.1007/s10664-006-9005-5",
    ID="Li2006",
    springer2015="1",
    placex="Empirical Software Engineering",
))

liu2006a = DB(WorkSnowball(
    2006, "Business-oriented software process improvement based on CMM using QFD",
    display="liu",
    authors="Liu, X. and Sun, Y. and Kane, G. and Kyoya, Y. and Noguchi, K.",
    place=SPIP,
    pp="573--589",
    entrytype="article",
    volume="11",
    number="6",
    doi="10.1002/spip.295",
    note="cited By 6",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-33845939841&doi=10.1002%2fspip.295&partnerID=40&md5=f6417a89b52c03fc47ae07b6b99b3955",
    document_type="Article",
    source="Scopus",
    ID="Liu2006573",
    scholar="https://scholar.google.com/scholar?cites=18358451812604453084&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="18358451812604453084",
    scholar_ok=True,
    placex="Software Process Improvement and Practice",
    selected_order="46",
    selected_snowballing="1",
))

liu2006b = DB(WorkUnrelated(
    2006, "Priority assessment of software process requirements from multiple perspectives",
    display="liu b",
    authors="Liu, X.(F.) and Sun, Y. and Veera, C.S. and Kyoya, Y. and Noguchi, K.",
    place=JSS,
    pp="1649--1660",
    entrytype="article",
    volume="79",
    number="11",
    doi="10.1016/j.jss.2006.03.012",
    note="cited By 15",
    ID="Liu20061649",
    placex="Journal of Systems and Software",
))

mahanti2006a = DB(WorkUnrelated(
    2006, "Six Sigma in software industries: some case studies and observations",
    display="mahanti",
    authors="Mahanti, Rupa and Antony, Jiju",
    place=FAKE,
    pp="263--290",
    entrytype="article",
    volume="2",
    number="3",
    publisher="Inderscience Publishers",
    ID="mahanti2006six",
    cluster_id="14100205714070344840",
    scholar="http://scholar.google.com/scholar?cites=14100205714070344840&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Journal of Six Sigma and Competitive Advantage",
))

maldonado2006a = DB(WorkUnrelated(
    2006, "Perspective-Based Reading: A Replicated Experiment Focused on Individual Reviewer Effectiveness",
    display="maldonado",
    authors="Maldonado, José C. and Carver, Jeffrey and Shull, Forrest and Fabbri, Sandra and Dória, Emerson and Martimiano, Luciana and Mendon{ç}a, Manoel and Basili, Victor",
    place=ESE,
    pp="119--142",
    entrytype="article",
    month="Mar",
    day="01",
    volume="11",
    number="1",
    issn="1573-7616",
    doi="10.1007/s10664-006-5967-6",
    ID="Maldonado2006",
    springer2015="1",
    placex="Empirical Software Engineering",
))

martins2006a = DB(WorkUnrelated(
    2006, "A case study applying process and project alignment methodology",
    display="martins",
    authors="Martins, P.V. and da Silva, A.R.",
    place=JBCS,
    pp="65--82",
    entrytype="article",
    volume="12",
    number="3",
    doi="10.1007/BF03194496",
    note="cited By 2",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-84942752098&doi=10.1007%2fBF03194496&partnerID=40&md5=0251a9a6bdbed39e2b0e4c885281ef00",
    document_type="Article",
    source="Scopus",
    ID="Martins200665",
    scopus="1",
    elcompendex="1",
    placex="Journal of the Brazilian Computer Society",
))

messnarz2006a = DB(WorkUnrelated(
    2006, "Software process improvement--EuroSPI 2006 conference",
    display="messnarz",
    authors="Messnarz, Richard and Richardson, Ita and Runeson, Per",
    place=FAKE,
    pp="1--4",
    entrytype="inproceedings",
    organization="Springer",
    ID="messnarz2006software",
    cluster_id="4817880809914343050",
    scholar="http://scholar.google.com/scholar?cites=4817880809914343050&as_sdt=2005&sciodt=0,5&hl=en",
    placex="European Conference on Software Process Improvement",
))

nejmeh2006a = DB(WorkUnrelated(
    2006, "The \PERFECT\ Approach to Experience-Based Process Evolution",
    display="nejmeh",
    authors="Brian A. Nejmeh and William E. Riddle",
    place=FAKE,
    pp="173 -- 238",
    entrytype="incollection",
    editor="Marvin V. Zelkowitz",
    publisher="Elsevier",
    volume="66",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(05)66005-6",
    link="https://www.sciencedirect.com/science/article/pii/S0065245805660056",
    ID="Nejmeh2006173",
    sciencedirect="1",
    placex="Quality Software Development",
))

niazi2006a = DB(WorkUnrelated(
    2006, "An empirical study identifying high perceived value requirements engineering practices",
    display="niazi",
    authors="Niazi, Mahmood and Cox, Karl A and Verner, June M",
    place=FAKE,
    pp="731--743",
    entrytype="incollection",
    publisher="Springer",
    ID="niazi2006empirical",
    gs="1",
    placex="Advances in Information Systems Development",
))

nonthaleerak2006a = DB(WorkUnrelated(
    2006, "Six Sigma: literature review and key future research areas",
    display="nonthaleerak",
    authors="Nonthaleerak, P and Hendry, LC",
    place=FAKE,
    pp="105--161",
    entrytype="article",
    volume="2",
    number="2",
    publisher="Inderscience Publishers",
    ID="nonthaleerak2006six",
    cluster_id="2865787316791780938",
    scholar="http://scholar.google.com/scholar?cites=2865787316791780938&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Journal of Six Sigma and Competitive Advantage",
))

oecd2006a = DB(WorkUnrelated(
    2006, "OECD Information Technology Outlook",
    display="oecd",
    authors="OECD",
    place=FAKE,
    entrytype="article",
    note="cited By 317",
    ID="OECD2006",
    placex="Organization for Economic Co-Operation and Development: OECD",
))

park2006a = DB(WorkUnrelated(
    2006, "The Effect of Improving IT Standard in IT Governance",
    display="park",
    authors="H. Y. Park and S. H. Jung and Y. j. Lee and K. C. Jang",
    place=FAKE,
    pp="22--22",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="organisational aspects;production engineering computing;semiconductor device manufacture;IT governance;IT standard;Samsung Electronics Semiconductor Business;business renovation;business strategy;robust set;semiconductor manufacturing;senior management attention;Companies;Computational intelligence;Decision making;Fabrication;Information systems;Investments;Manufacturing processes;Robust control;Semiconductor device manufacture;Standards organizations",
    doi="10.1109/CIMCA.2006.210",
    issn="",
    ID="4052669",
    ieee="1",
    placex="2006 International Conference on Computational Inteligence for Modelling Control and Automation and International Conference on Intelligent Agents Web Technologies and International Commerce (CIMCA'06)",
    organization="IEEE",
    gs="1",
    ieee2015="1",
))

pu2006a = DB(WorkUnrelated(
    2006, "Real time business performance monitoring and analysis using metric network",
    display="pu",
    authors="Pu, H. and Hui, L. and Lipyeow, L.",
    place=FAKE,
    pp="442--448",
    entrytype="article",
    doi="10.1109/ICEBE.2006.84",
    artnumber="4031685",
    note="cited By 4",
    ID="Pu2006442",
    placex="Proceedings - IEEE International Conference on e-Business Engineering, ICEBE 2006",
))

pérez2006a = DB(WorkUnrelated(
    2006, "Requirements Variability Support Through MDA and Graph Transformation",
    display="pérez",
    authors="Javier Pérez and Miguel A. Laguna and Yania Crespo González-Carvajal and Bruno González-Baixauli",
    place=FAKE,
    pp="161 -- 173",
    entrytype="article",
    volume="152",
    number="",
    note="Proceedings of the International Workshop on Graph and Model Transformation (GraMoT 2005)Graph and Model Transformation 2005",
    issn="1571-0661",
    doi="https://doi.org/10.1016/j.entcs.2005.10.023",
    link="https://www.sciencedirect.com/science/article/pii/S1571066106001459",
    keyword="Layered Graph Grammars",
    ID="Pérez2006161",
    sciencedirect="1",
    placex="Electronic Notes in Theoretical Computer Science",
    sciencedirect2015="1",
))

redzic2006a = DB(WorkUnrelated(
    2006, "Six sigma approach in software quality improvement",
    display="redzic",
    authors="Redzic, C. and Baik, J.",
    place=FAKE,
    pp="396--405",
    entrytype="conference",
    doi="10.1109/SERA.2006.61",
    art_number="1691407",
    note="cited By 10",
    ID="Redzic2006396",
    placex="Proceedings - Fourth International Conference on Software Engineering Research, Management and Applications, SERA 2006",
))

rocha2006a = DB(WorkUnrelated(
    2006, "Success Factors and Difficulties in Software Process Deployment Experiences based on CMMI and MR-MPS.BR",
    display="rocha",
    authors="Rocha, A.R. and Montoni, M. and Santos, G. and Oliveira, K. and Natali, A.C. and Mian, P. and Conte, T. and Mafra, S. and Barreto, A. and Albuquerque, A. and Figueiredo, S. and Soares, A. and Bianchi, F. and Cabral, R. and Neto, A.D.",
    place=FAKE,
    pp="77--87",
    entrytype="article",
    note="cited By 7",
    ID="Rocha200677",
    placex="Proc. of the 6th International Workshop on Learning Software Organizations (LSO'2006)",
))

schweikhard2006a = DB(WorkUnrelated(
    2006, "Identification of inspection-variation-factors for a decision-support-tool",
    display="schweikhard",
    authors="Schweikhard, T.",
    place=FAKE,
    entrytype="article",
    note="cited By 2",
    ID="Schweikhard2006",
    placex="Diploma Thesis, Department of Computer Science, University of Kaiserslautern, Germany",
    other1="Department of Computer Science, University of Kaiserslautern, Germany",
))

sei2006a = DB(WorkUnrelated(
    2006, "SEI Carnegie Mellon Software Engineering Institute",
    journal="CMMI",
    display="sei",
    authors="SEI",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="SEI2006",
    placex="",
))

sei2006b = DB(WorkUnrelated(
    2006, "Standard CMMI Appraisal Method for Process Improvement (SCAMPI) A, Version 1.2: Method Definition Document",
    display="sei b",
    authors="SEI",
    place=FAKE,
    entrytype="article",
    note="cited By 4",
    ID="SEI2006",
    placex="CMU SEI",
))

sfetsos2006a = DB(WorkUnrelated(
    2006, "Investigating the extreme programming system--An empirical study",
    display="sfetsos",
    authors="Sfetsos, Panagiotis and Angelis, Lefteris and Stamelos, Ioannis",
    place=ESE,
    pp="269--301",
    entrytype="article",
    month="Jun",
    day="01",
    volume="11",
    number="2",
    issn="1573-7616",
    doi="10.1007/s10664-006-6404-6",
    ID="Sfetsos2006",
    springer2015="1",
    placex="Empirical Software Engineering",
))

shull2006a = DB(WorkUnrelated(
    2006, "Victor R. Basili's contributions to software quality",
    display="shull",
    authors="Shull, F. and Seaman, C. and Zelkowitz, M.",
    place=IEEES,
    pp="16--18",
    entrytype="article",
    volume="23",
    number="1",
    doi="10.1109/MS.2006.33",
    note="cited By 12",
    ID="Shull200616",
    placex="IEEE Software",
))

solingen2006a = DB(WorkUnrelated(
    2006, "Calculating Software Process Improvements Return on Investment",
    display="solingen",
    authors="Rini Van Solingen and David F. Rico",
    place=FAKE,
    pp="1 -- 41",
    entrytype="incollection",
    editor="Marvin V. Zelkowitz",
    publisher="Elsevier",
    volume="66",
    series="Advances in Computers",
    issn="0065-2458",
    doi="https://doi.org/10.1016/S0065-2458(05)66001-9",
    link="https://www.sciencedirect.com/science/article/pii/S0065245805660019",
    ID="VanSolingen20061",
    sciencedirect="1",
    placex="Quality Software Development",
))

standardization2006a = DB(WorkUnrelated(
    2006, "ISO/IEC 15504:2004,",
    display="standardization",
    authors="International Organization for Standardization",
    place=FAKE,
    other1="ISO/IEC, Geneva, Switzerland",
    placex="'Information technology - Process assessment'.",
))

storey2006a = DB(WorkUnrelated(
    2006, "Theories, tools and research methods in program comprehension: past, present and future",
    display="storey",
    authors="Storey, Margaret-Anne",
    place=SQJ,
    pp="187--208",
    entrytype="article",
    month="Sep",
    day="01",
    volume="14",
    number="3",
    issn="1573-1367",
    doi="10.1007/s11219-006-9216-4",
    ID="Storey2006",
    springer2015="1",
    placex="Software Quality Journal",
))

tihinen2006a = DB(WorkUnrelated(
    2006, "How to build and sustain a measurement data management environment in a SME",
    display="tihinen",
    authors="Tihinen, Maarit and Järvinen, Janne",
    place=FAKE,
    entrytype="article",
    ID="tihinen2006build",
    cluster_id="5654856157852152882",
    scholar="http://scholar.google.com/scholar?cites=5654856157852152882&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

tonini2006a = DB(WorkUnrelated(
    2006, "A contribui{ç}ão do Seis Sigma para a melhoria dos processos de software.",
    display="tonini",
    authors="Tonini, Antonio Carlos",
    place=Thesis,
    entrytype="phdthesis",
    ID="tonini2006contribuiccao",
    cluster_id="1183052021563397904",
    scholar="http://scholar.google.com/scholar?cites=1183052021563397904&as_sdt=2005&sciodt=0,5&hl=en",
    local="Universidade de São Paulo",
    placex="",
))

tuan2006a = DB(WorkUnrelated(
    2006, "Using ABC model for software process improvement: A balanced perspective",
    display="tuan",
    authors="Tuan, H. W., Liu, C. Y., & Chen, C. M.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Tuan2006",
    placex="Proceedings of the 39th annual Hawaii international conference on system sciences",
))

wang2006a = DB(WorkUnrelated(
    2006, "BSR: a statistic-based approach for establishing and refining software process performance baseline",
    display="wang",
    authors="Wang, Qing and Jiang, Nan and Gou, Lang and Liu, Xia and Li, Mingshu and Wang, Yongji",
    place=ICSE,
    pp="585--594",
    entrytype="inproceedings",
    organization="ACM",
    ID="wang2006bsr",
    cluster_id="8175570722120207926",
    scholar="http://scholar.google.com/scholar?cites=8175570722120207926&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Proceedings of the 28th international conference on Software engineering",
))

wangeheim2006a = DB(WorkUnrelated(
    2006, "Helping small companies assess software processes",
    display="wangeheim",
    authors="von Wangeheim, C.G. and Anacleto, A. and Salviano, C.F.",
    place=IEEES,
    pp="91--98",
    entrytype="article",
    volume="23",
    number="1",
    doi="10.1109/MS.2006.13",
    note="cited By 51",
    ID="vonWangeheim200691",
    placex="IEEE Software",
))

wangenheim2006a = DB(WorkUnrelated(
    2006, "Experiences on establishing software processes in small companies",
    display="wangenheim",
    authors="Christiane Gresse von Wangenheim and Sérgio Weber and Jean Carlo Rossa Hauck and Gisele Trentin",
    place=IST,
    pp="890 -- 900",
    entrytype="article",
    volume="48",
    number="9",
    note="Special Issue Section: Distributed Software Development",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2005.12.010",
    link="https://www.sciencedirect.com/science/article/pii/S0950584905001965",
    keyword="Small Organisation",
    ID="Wangenheim2006890",
    sciencedirect="1",
    placex="Information and Software Technology",
))

wong2006a = DB(WorkUnrelated(
    2006, "Software process improvements in Bagladesh",
    display="wong",
    authors="Wong, Bernard and Hasan, Sazzad",
    place=ICSE,
    entrytype="inproceedings",
    organization="CSREA Press",
    ID="wong2006software",
    cluster_id="128097436475771037",
    scholar="http://scholar.google.com/scholar?cites=128097436475771037&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Engineering Research and Practice",
))

wu2006a = DB(WorkUnrelated(
    2006, "An integrated structural model toward successful continuous improvement activity",
    display="wu",
    authors="Wu, Chih Wei and Chen, Chyong Ling",
    place=FAKE,
    pp="697--707",
    entrytype="article",
    volume="26",
    number="5-6",
    publisher="Elsevier",
    ID="wu2006integrated",
    cluster_id="5897908042983255809",
    scholar="http://scholar.google.com/scholar?cites=5897908042983255809&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Technovation",
))

xu2006a = DB(WorkUnrelated(
    2006, "Requirement process establishment and improvement from the viewpoint of cybernetics",
    display="xu",
    authors="Hong Xu and Pete Sawyer and Ian Sommerville",
    place=JSS,
    pp="1504 -- 1513",
    entrytype="article",
    volume="79",
    number="11",
    note="Software Cybernetics",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2006.03.050",
    link="https://www.sciencedirect.com/science/article/pii/S0164121206001191",
    keyword="Control theory",
    ID="Xu20061504",
    sciencedirect="1",
    placex="Journal of Systems and Software",
    sciencedirect2015="1",
))
