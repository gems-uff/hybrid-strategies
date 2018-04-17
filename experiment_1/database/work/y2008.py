# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

aguiar2008a = DB(WorkUnrelated(
    2008, "Uma metodologia para implanta{ç}ão de melhoria de processo de software em grupos de empresas",
    display="aguiar",
    authors="AGUIAR, Heron Vieira",
    place=FAKE,
    entrytype="article",
    publisher="Universidade Federal de Pernambuco",
    ID="aguiar2008metodologia",
    cluster_id="9536356892945913280",
    scholar="http://scholar.google.com/scholar?cites=9536356892945913280&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

alagarsamy2008a = DB(WorkUnrelated(
    2008, "Implementation specification for software process improvement supportive knowledge management tool",
    display="alagarsamy",
    authors="Alagarsamy, K and Justus, Selwyn and Iyakutti, Kombiah",
    place=IEEES,
    pp="123--133",
    entrytype="article",
    volume="2",
    number="2",
    publisher="IET",
    ID="alagarsamy2008implementation",
    cluster_id="6143026836610612217",
    scholar="http://scholar.google.com/scholar?cites=6143026836610612217&as_sdt=2005&sciodt=0,5&hl=en",
    placex="IET software",
))

allee2008a = DB(WorkUnrelated(
    2008, "Value network analysis and value conversion of tangible and intangible assets",
    display="allee",
    authors="Allee, V.",
    place=FAKE,
    pp="5--24",
    entrytype="article",
    volume="9",
    number="1",
    doi="10.1108/14691930810845777",
    note="cited By 174",
    ID="Allee20085",
    placex="Journal of Intellectual Capital",
))

angelis2008a = DB(WorkUnrelated(
    2008, "An Empirical Study on Change Impact",
    alias=(0, "An Empirical Study on Change Impact",),
    display="angelis",
    authors="Angelis, Claes Wohlin",
    place=FAKE,
    entrytype="article",
    ID="angelisempirical",
    placex="",
))

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

aurum2008a = DB(WorkUnrelated(
    2008, "Investigating Knowledge Management practices in software development organisations  An Australian experience",
    display="aurum",
    authors="Aybüke Aurum and Farhad Daneshgar and James Ward",
    place=IST,
    pp="511 -- 533",
    entrytype="article",
    volume="50",
    number="6",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2007.05.005",
    link="https://www.sciencedirect.com/science/article/pii/S0950584907000602",
    keyword="KM process enablers",
    ID="Aurum2008511",
    sciencedirect="1",
    placex="Information and Software Technology",
    sciencedirect2015="1",
))

ba2008a = DB(WorkUnrelated(
    2008, "Information Quality Management Capability Maturity Model",
    display="ba",
    authors="Ba{}karada, Sa{}a",
    place=FAKE,
    entrytype="article",
    publisher="Springer",
    ID="bavskarada2008information",
    cluster_id="2620735428069460015",
    scholar="http://scholar.google.com/scholar?cites=2620735428069460015&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
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

barcellos2008a = DB(WorkUnrelated(
    2008, "Avalia{ç}ão de Bases de Medidas considerando sua Aplicabilidade ao Controle Estatístico de Processos de Software",
    display="barcellos",
    authors="Barcellos, Monalessa Perini and ROCHA, ARC",
    place=FAKE,
    entrytype="article",
    ID="barcellos2008avaliaccao",
    cluster_id="6130679276477238473",
    scholar="http://scholar.google.com/scholar?cites=6130679276477238473&as_sdt=2005&sciodt=0,5&hl=en",
    placex="VII Simpósio Brasileiro de Qualidade de Software (SBQS08), Florianópolis--SC",
))

barcellos2008b = DB(WorkUnrelated(
    2008, "Uma Abordagem para Controle Estatístico de Processos de Software em Organiza{ç}ões de Alta Maturidade",
    display="barcellos b",
    authors="Barcellos, Monalessa Perini",
    place=FAKE,
    entrytype="article",
    ID="barcellos2008abordagem",
    cluster_id="13291230235783373616",
    scholar="http://scholar.google.com/scholar?cites=13291230235783373616&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Exame de Qualifica{ç}ão para Tese de D. Sc., COPPE/UFRJ, Rio de Janeiro, Brasil",
))

becker2008a = DB(WorkSnowball( # 1
    2008, "An approach to support the strategic alignment of software process improvement programs",
    display="becker b",
    authors="Becker, A.L. and Audy, J.L.N. and Prikladnicki, R.",
    place=ICEIS,
    pp="66--73",
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
    scholar="https://scholar.google.com/scholar?cites=12615708466078293814&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    final_selected="1",
    selected_order="3",
    webofscience2015="1",
    elcompendex2015="1",
    scopus2015="1",
))

becker2008b = DB(WorkSnowball(
    2008, "Strategic alignment of software process improvement programs using QFD",
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
    scholar="http://scholar.google.com/scholar?cites=2559826507613970329&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    cluster_id="2559826507613970329",
    scholar_ok=True,
    artnumber="1370840",
    note="cited By 9",
    placex="Proceedings - International Conference on Software Engineering",
    art_number="1370840",
    other1="Germany",
    final_selected="1",
    selected_order="19",
    acm2015="1",
))

beijun2008a = DB(WorkUnrelated(
    2008, "A case study of software process improvement in a Chinese small company",
    display="beijun",
    authors="Beijun, S. and Tong, R.",
    place=FAKE,
    pp="609--612",
    entrytype="conference",
    volume="2",
    doi="10.1109/CSSE.2008.701",
    art_number="4722125",
    note="cited By 11",
    ID="Beijun2008609",
    placex="Proceedings - International Conference on Computer Science and Software Engineering, CSSE 2008",
))

bennicke2008a = DB(WorkUnrelated(
    2008, "Software Controlling",
    display="bennicke",
    authors="Bennicke, Marcel and Hofmann, Alexander and Lewerentz, Claus and Wichert, Karl-Heinz",
    place=FAKE,
    pp="556",
    entrytype="article",
    volume="31",
    number="6",
    publisher="Springer",
    ID="bennicke2008software",
    cluster_id="6401885050051856412",
    scholar="http://scholar.google.com/scholar?cites=6401885050051856412&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Informatik-Spektrum",
))

bertrand2008a = DB(WorkUnrelated(
    2008, "Modeling and management of process in numerical engineering. Application in foundry",
    display="bertrand",
    authors="Bertrand, B and Danesi, F and Gardan, N and Gardan, Y",
    place=FAKE,
    pp="206--210",
    entrytype="inproceedings",
    organization="World Scientific and Engineering Academy and Society (WSEAS)",
    ID="bertrand2008modeling",
    placex="Proceedings of the 7th WSEAS international conference on System science and simulation in engineering",
))

birkhölzer2008a = DB(WorkUnrelated(
    2008, "Customized predictive models for process improvement projects",
    display="birkhölzer",
    authors="Birkhölzer, T. and Dickmann, C. and Klein, H. and Vaupel, J. and Ast, S. and Meyer, L.",
    place=FAKE,
    pp="304--316",
    entrytype="article",
    volume="5089 LNCS",
    doi="10.1007/978-3-540-69566-0_25",
    note="cited By 2",
    ID="Birkhölzer2008304",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

bjørnson2008a = DB(WorkUnrelated(
    2008, "Knowledge management in software engineering: A systematic review of studied concepts, findings and research methods used",
    display="bjørnson",
    authors="Finn Olav Bjørnson and Torgeir Dingsøyr",
    place=IST,
    pp="1055 -- 1068",
    entrytype="article",
    volume="50",
    number="11",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2008.03.006",
    link="https://www.sciencedirect.com/science/article/pii/S0950584908000487",
    keyword="Systematic review",
    ID="Bjørnson20081055",
    sciencedirect="1",
    placex="Information and Software Technology",
    sciencedirect2015="1",
))

brindgeland2008a = DB(WorkUnrelated(
    2008, "Business modeling: a practical guide to realizing business value",
    display="brindgeland",
    authors="DM Brindgeland, R Zahavi",
    place=MK,
    placex="Morgan Kaufmann, Boston, MA",
))

butt2008a = DB(WorkUnrelated(
    2008, "Identifying Factors Affecting Software Process Improvement during Change",
    display="butt",
    authors="Butt, Asim",
    place=FAKE,
    entrytype="misc",
    ID="butt2008identifying",
    cluster_id="14144555277093950953",
    scholar="http://scholar.google.com/scholar?cites=14144555277093950953&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

chen2008a = DB(WorkUnrelated(
    2008, "An objective-oriented and product-line-based manufacturing performance measurement",
    display="chen",
    authors="Chen, Chee-Cheng",
    place=FAKE,
    pp="380--390",
    entrytype="article",
    volume="112",
    number="1",
    publisher="Elsevier",
    ID="chen2008objective",
    cluster_id="2788151225591553526",
    scholar="http://scholar.google.com/scholar?cites=2788151225591553526&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Journal of Production Economics",
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

ciolkowski2008a = DB(WorkUnrelated(
    2008, "Practical guidelines for introducing software cockpits in industry",
    display="ciolkowski",
    authors="Ciolkowski, Marcus and Heidrich, Jens and Münch, Jürgen",
    place=FAKE,
    entrytype="inproceedings",
    ID="ciolkowski2008practical",
    cluster_id="14116596596256369202",
    scholar="http://scholar.google.com/scholar?cites=14116596596256369202&as_sdt=2005&sciodt=0,5&hl=en",
    placex="4th Software Measurement European Forum (SMEF 2008)",
))

cohen2008a = DB(WorkUnrelated(
    2008, "Assessing the business value of software process improvement using CMMI{	extregistered} in South Africa",
    display="cohen",
    authors="Cohen, Douglas James and others",
    place=Thesis,
    entrytype="phdthesis",
    ID="cohen2008assessing",
    cluster_id="5248559068027256155",
    scholar="http://scholar.google.com/scholar?cites=5248559068027256155&as_sdt=2005&sciodt=0,5&hl=en",
    local="University of Pretoria",
    placex="",
))

coleman2008a = DB(WorkUnrelated(
    2008, "Investigating software process in practice: A grounded theory perspective",
    display="coleman",
    authors="Gerry Coleman and Rory OConnor",
    place=JSS,
    pp="772 -- 784",
    entrytype="article",
    volume="81",
    number="5",
    note="Software Process and Product Measurement",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2007.07.027",
    link="https://www.sciencedirect.com/science/article/pii/S0164121207001811",
    keyword="XP",
    ID="Coleman2008772",
    sciencedirect="1",
    placex="Journal of Systems and Software",
    sciencedirect2015="1",
))

couch2008a = DB(WorkUnrelated(
    2008, "1.4 - System Configuration Management",
    display="couch",
    authors="Alva L. Couch",
    place=FAKE,
    pp="75 -- 133",
    entrytype="incollection",
    editor="Bergstra, Jan  and Burgess, Mark",
    publisher="Elsevier",
    edition="",
    address="Amsterdam",
    isbn="978-0-444-52198-9",
    doi="https://doi.org/10.1016/B978-044452198-9.50006-9",
    link="https://www.sciencedirect.com/science/article/pii/B9780444521989500069",
    ID="Couch200875",
    sciencedirect="1",
    placex="Handbook of Network and System Administration",
))

cyra2008a = DB(WorkUnrelated(
    2008, "Extending GQM by Argument Structures",
    display="cyra",
    authors="Cyra, ?ukasz and Górski, Janusz",
    place=FAKE,
    pp="26--39",
    entrytype="inproceedings",
    editor="Meyer, Bertrand and Nawrocki, Jerzy R. and Walter, Bartosz",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-85279-7_3",
    springer="1",
    placex="Balancing Agility and Formalism in Software Engineering",
))

damiani2008a = DB(WorkUnrelated(
    2008, "SAF: strategic alignment framework for monitoring organizations",
    display="damiani",
    authors="E Damiani, F Mulazzani, B Russo, G Succi",
    place=FAKE,
    other1="Innsbruck, Austria. Springer",
    placex="Proceedings to the eleventh international conference on business information systems,",
    pp="213--226",
    entrytype="inproceedings",
    organization="Springer",
    ID="damiani2008saf",
    scholar="http://scholar.google.com/scholar?cites=16015635733652860478&as_sdt=2005&sciodt=0,5&hl=en",
))

danovaro2008a = DB(WorkUnrelated(
    2008, "PEM: experience management tool for software companies",
    display="danovaro",
    authors="Danovaro, Emanuele and Remencius, Tadas and Sillitti, Alberto and Succi, Giancarlo",
    place=FAKE,
    pp="733--734",
    entrytype="inproceedings",
    organization="ACM",
    ID="danovaro2008pem",
    cluster_id="17490022466926352948",
    scholar="http://scholar.google.com/scholar?cites=17490022466926352948&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Companion to the 23rd ACM SIGPLAN conference on Object-oriented programming systems languages and applications",
))

darwish2008a = DB(WorkUnrelated(
    2008, "\TTPM\  An efficient deadlock-free algorithm for multicast communication in 2D torus networks",
    display="darwish",
    authors="M.G. Darwish and A.A. Radwan and M.A. Abd El-Baky and K. Hamed",
    place=FAKE,
    pp="919 -- 928",
    entrytype="article",
    volume="54",
    number="10",
    note="",
    issn="1383-7621",
    doi="https://doi.org/10.1016/j.sysarc.2008.03.004",
    link="https://www.sciencedirect.com/science/article/pii/S1383762108000465",
    keyword="Deadlock-free routing",
    ID="Darwish2008919",
    sciencedirect="1",
    placex="Journal of Systems Architecture",
    sciencedirect2015="1",
))

daubner2008a = DB(WorkUnrelated(
    2008, "Konzeption und prototypische Implementierung eines Frameworks zur automatisierten Softwaremessung",
    display="daubner",
    authors="Daubner, Bernhard",
    place=Thesis,
    entrytype="phdthesis",
    ID="daubner2008konzeption",
    cluster_id="15219583948292450725",
    scholar="http://scholar.google.com/scholar?cites=15219583948292450725&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

dybå2008a = DB(WorkUnrelated(
    2008, "Empirical studies of agile software development: A systematic review",
    display="dybå",
    authors="Tore Dybå and Torgeir Dingsøyr",
    place=IST,
    pp="833 -- 859",
    entrytype="article",
    volume="50",
    number="910",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2008.01.006",
    link="https://www.sciencedirect.com/science/article/pii/S0950584908000256",
    keyword="Scrum",
    ID="Dybå2008833",
    sciencedirect="1",
    placex="Information and Software Technology",
    sciencedirect2015="1",
))

díaz2008a = DB(WorkUnrelated(
    2008, "MIS-PyME software measurement maturity model-supporting the definition of software measurement programs",
    display="díaz",
    authors="Díaz-Ley, M. and García, F. and Piattini, M.",
    place=FAKE,
    pp="19--33",
    entrytype="article",
    volume="5089 LNCS",
    doi="10.1007/978-3-540-69566-0_5",
    note="cited By 7",
    ID="Díaz-Ley200819",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
))

eilat2008a = DB(WorkUnrelated(
    2008, "R&D project evaluation: An integrated DEA and balanced scorecard approach",
    display="eilat",
    authors="Eilat, H. and Golany, B. and Shtub, A.",
    place=FAKE,
    pp="895--912",
    entrytype="article",
    volume="36",
    number="5",
    doi="10.1016/j.omega.2006.05.002",
    note="cited By 132",
    ID="Eilat2008895",
    placex="Omega",
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

ferreira2008a = DB(WorkUnrelated(
    2008, "ROI of software process improvement at BL informática: SPIdex is really worth it",
    display="ferreira",
    authors="Ferreira, A.I.F. and Santos, G. and Cerqueira, R. and Montoni, M. and Barreto, A. and Rocha, A.R. and Barreto, A.O.S. and Silva Filho, R.C.",
    place=SPIP,
    pp="311--318",
    entrytype="article",
    volume="13",
    number="4",
    doi="10.1002/spip.392",
    note="cited By 8",
    ID="Ferreira2008311",
    placex="Software Process Improvement and Practice",
))

gimenes2008a = DB(WorkUnrelated(
    2008, "A Product Line for Business Process Management",
    display="gimenes",
    authors="I. M. d. S. Gimenes and M. Fantinato and M. B. F. d. Toledo",
    place=FAKE,
    pp="265-274",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="business data processing;contracts;organisational aspects;product development;software reusability;Internet technology;business process management;e-contract negotiation;electronic contract establishment;feature modeling;intraorganizational interchange;product line;service oriented computing;Asset management;Conference management;Contracts;Informatics;Marine technology;Monitoring;Quality of service;Telecommunication computing;Web and internet services;Web services",
    doi="10.1109/SPLC.2008.10",
    issn="",
    ID="4626860",
    placex="2008 12th International Software Product Line Conference",
    ieee2015="1",
))

gorschek2008a = DB(WorkUnrelated(
    2008, "Requirements engineering: In search of the dependent variables",
    display="gorschek",
    authors="Tony Gorschek and Alan M. Davis",
    place=IST,
    pp="67 -- 75",
    entrytype="article",
    volume="50",
    number="12",
    note="Special issue with two special sections. Section 1: Most-cited software engineering articles in 2001. Section 2: Requirement engineering: Foundation for software quality",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2007.10.003",
    link="https://www.sciencedirect.com/science/article/pii/S0950584907001188",
    keyword="Organizational perspective",
    ID="Gorschek200867",
    sciencedirect="1",
    placex="Information and Software Technology",
    scholar="http://scholar.google.com/scholar?cites=11359460249030422468&as_sdt=2005&sciodt=0,5&hl=en",
    sciencedirect2015="1",
))

gou2008a = DB(WorkUnrelated(
    2008, "Quantitatively managing defects for iterative projects: An industrial experience report in China",
    display="gou",
    authors="Gou, Lang and Wang, Qing and Yuan, Jun and Yang, Ye and Li, Mingshu and Jiang, Nan",
    place=ICSE,
    pp="369--380",
    entrytype="inproceedings",
    organization="Springer",
    ID="gou2008quantitatively",
    cluster_id="1595857835389432228",
    scholar="http://scholar.google.com/scholar?cites=1595857835389432228&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
))

habib2008a = DB(WorkUnrelated(
    2008, "Blending six sigma and CMMI-an approach to accelerate process improvement in SMEs",
    display="habib",
    authors="Habib, Maria and Ahmed, Sana and Rehmat, Amna and Khan, Malik Jahan and Shamail, Shafay",
    place=FAKE,
    pp="386--391",
    entrytype="inproceedings",
    organization="IEEE",
    ID="habib2008blending",
    cluster_id="12942614433290959761",
    scholar="http://scholar.google.com/scholar?cites=12942614433290959761&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Multitopic Conference, 2008. INMIC 2008. IEEE International",
))

hanssen2008a = DB(WorkUnrelated(
    2008, "Process fusion: An industrial case study on agile software product line engineering",
    display="hanssen",
    authors="Geir K. Hanssen and Tor E. Fægri",
    place=JSS,
    pp="843 -- 854",
    entrytype="article",
    volume="81",
    number="6",
    note="Agile Product Line Engineering",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2007.10.025",
    link="https://www.sciencedirect.com/science/article/pii/S0164121207002518",
    keyword="Agile software development",
    ID="Hanssen2008843",
    sciencedirect="1",
    placex="Journal of Systems and Software",
    sciencedirect2015="1",
))

harjumaa2008a = DB(WorkUnrelated(
    2008, "How does a measurement programme evolve in software organizations?",
    display="harjumaa",
    authors="Harjumaa, L., Markkula, J., & Oivo, M",
    place=PROFES,
    entrytype="article",
    note="cited By 1",
    ID="Harjumaa2008",
    placex="PROFES",
    pp="230--243",
    organization="Springer",
    scholar="http://scholar.google.com/scholar?cites=2258055919187012201&as_sdt=2005&sciodt=0,5&hl=en",
))

heidrich2008a = DB(WorkUnrelated(
    2008, "Goal-oriented setup and usage of custom-tailored software cockpits",
    display="heidrich",
    authors="Heidrich, Jens and Münch, Jürgen",
    place=ICPFSPI,
    pp="4--18",
    entrytype="inproceedings",
    organization="Springer",
    ID="heidrich2008goal",
    cluster_id="4477990520413087096",
    scholar="http://scholar.google.com/scholar?cites=4477990520413087096&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Product Focused Software Process Improvement",
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

isaca2008a = DB(WorkUnrelated(
    2008, "VAL IT Framework 2.0",
    display="isaca",
    authors="ISACA",
    place=FAKE,
    entrytype="article",
    note="cited By 6",
    ID="ISACA2008",
    placex="IT Governance Institute",
))

isaca2008b = DB(WorkUnrelated(
    2008, "Control Objectives for Information and related Technology (COBIT)",
    display="isaca b",
    authors="isaca",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="isaca2008",
    placex="ISACA",
))

isoiec2008a = DB(WorkUnrelated(
    2008, "Quality management systemsrequirements, international standards organization",
    display="isoiec",
    authors="ISOIEC",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="ISOIECr2008",
    placex="ISO/IEC 9001:2008",
))

isoiec2008b = DB(WorkUnrelated(
    2008, "Systems and Software Engineering - System Life Cycle Processes ISO/IEC 15288:2008",
    display="isoiec b",
    authors="ISOIEC",
    place=FAKE,
    entrytype="article",
    note="cited By 193",
    ID="ISOIEC2008",
    placex="ISO/IEC 15288:2008 International Standards Organization",
))

isoiec2008c = DB(WorkUnrelated(
    2008, "Systems and Software Engineering - System Life Cycle Processes ISO/IEC 12207:2008",
    display="isoiec c",
    authors="ISOIEC",
    place=FAKE,
    entrytype="article",
    note="cited By 184",
    ID="ISOIEC2008",
    placex="ISO/IEC 12207:2008 International Standards Organization",
))

j2008a = DB(WorkUnrelated(
    2008, "Aligning business strategies with software measurement - exercise handouts",
    display="j",
    authors="Münch J, Heidrich J",
    place=FAKE,
    placex="exercise handouts",
    entrytype="article",
    note="cited By 1",
    ID="Münch2008",
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

jönsson2008a = DB(WorkUnrelated(
    2008, "An Empirical Study on Views of Importance of Change Impact Analysis Issues",
    alias=(0, "An Empirical Study on Views of Importance of Change Impact Analysis Issues",),
    display="jönsson",
    authors="Jönsson, Per and Angelis, Lefteris and Wohlin, Claes",
    place=FAKE,
    entrytype="article",
    ID="jonssonempirical",
    placex="",
))

kabbaj2008a = DB(WorkUnrelated(
    2008, "A deviation management system for handling software process enactment evolution",
    display="kabbaj",
    authors="Kabbaj, Mohammed and Lbath, Redouane and Coulette, Bernard",
    place=ICSE,
    pp="186--197",
    entrytype="inproceedings",
    organization="Springer",
    ID="kabbaj2008deviation",
    cluster_id="5271360689171300486",
    scholar="http://scholar.google.com/scholar?cites=5271360689171300486&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
))

kaplan2008a = DB(WorkUnrelated(
    2008, "Plan the strategy: Aligning the organization for effective strategy execution",
    display="kaplan",
    authors="Kaplan, R. S., & Norton, D. P.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Kaplan2008",
    placex="Harvard Business Press",
))

kaplan2008b = DB(WorkUnrelated(
    2008, "Execution premium: linking strategy to operations for competitive advantage",
    display="kaplan b",
    authors="RS Kaplan, DP Norton",
    place=FAKE,
    placex="Harvard Business School Press, Boston, MA",
))

kasunic2008a = DB(WorkUnrelated(
    2008, "Can You Trust Your Data? Establishing the Need for a Measurement and Analysis Infrastructure Diagnostic",
    display="kasunic",
    authors="Kasunic, M. and McCurley, J. and Zubrow, D.",
    place=FAKE,
    entrytype="article",
    note="cited By 2",
    ID="Kasunic2008",
    placex="Technical Report CMU/SEI-2008-TN-028",
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

kojima2008a = DB(WorkUnrelated(
    2008, "Risk analysis of software process measurements",
    display="kojima",
    authors="Kojima, T. and Hasegawa, T. and Misumi, M. and Nakamura, T.",
    place=SQJ,
    pp="361--376",
    entrytype="article",
    volume="16",
    number="3",
    doi="10.1007/s11219-007-9040-5",
    note="cited By 2",
    ID="Kojima2008361",
    placex="Software Quality Journal",
    springer2015="1",
))

kulpa2008a = DB(WorkUnrelated(
    2008, "Interpreting the CMMI (R): A Process Improvement Approach",
    display="kulpa",
    authors="Kulpa, Margaret K and Johnson, Kent A",
    place=Book,
    entrytype="book",
    publisher="CRC Press",
    ID="kulpa2008interpreting",
    gs="1",
    placex="",
))

kuppusamy2008a = DB(WorkUnrelated(
    2008, "Fostering ICT development for growth: Measuring the payoffs for Australia and the Asean-5 countries",
    display="kuppusamy",
    authors="Kuppusamy, M. and Pahlavani, M. and Saleh, A.S.",
    place=FAKE,
    pp="1676--1685",
    entrytype="article",
    volume="5",
    number="12",
    note="cited By 11",
    ID="Kuppusamy20081676",
    placex="American Journal of Applied Sciences",
))

landaeta2008a = DB(WorkUnrelated(
    2008, "Practical SPI planning",
    display="landaeta",
    authors="Landaeta, José Francisco and García, Javier and Amescua, Antonio",
    place=FAKE,
    pp="82--93",
    entrytype="inproceedings",
    organization="Springer",
    ID="landaeta2008practical",
    cluster_id="8912082203644082263",
    scholar="http://scholar.google.com/scholar?cites=8912082203644082263&as_sdt=2005&sciodt=0,5&hl=en",
    placex="European Conference on Software Process Improvement",
))

lang2008a = DB(WorkUnrelated(
    2008, "软件缺陷预测技术",
    display="lang",
    authors="王青 and 伍书剑 [1 and 李明树 [1",
    place=Thesis,
    entrytype="phdthesis",
    ID="王青2008软件缺陷预测技术",
    cluster_id="17143179528404677757",
    scholar="http://scholar.google.com/scholar?cites=17143179528404677757&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

li2008a = DB(WorkUnrelated(
    2008, "On Software Requirement Metrics Based on Six-Sigma",
    display="li",
    authors="Li, Li and He, Shuguang and Qi, E-S",
    place=FAKE,
    entrytype="inproceedings",
    ID="li2008software",
    cluster_id="14981432110732704966",
    scholar="http://scholar.google.com/scholar?cites=14981432110732704966&as_sdt=2005&sciodt=0,5&hl=en",
    placex="2008 IEEE Symposium on Advanced Management of Information for Globalized Enterprises (AMIGE)",
))

liu2008a = DB(WorkUnrelated(
    2008, "The impact of software process standardization on software flexibility and project management performance: Control theory perspective",
    display="liu",
    authors="Liu, Julie Yu-Chih and Chen, Victor J and Chan, Chien-Lung and Lie, Ting",
    place=IST,
    pp="889--896",
    entrytype="article",
    volume="50",
    number="9--10",
    publisher="Elsevier",
    ID="liu2008impact",
    cluster_id="2258168969150207003",
    scholar="http://scholar.google.com/scholar?cites=2258168969150207003&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information and Software Technology",
))

long2008a = DB(WorkUnrelated(
    2008, "ITIL version 3 at a glance",
    display="long",
    authors="Long, J. O.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Long2008",
    placex="Springer US",
))

lui2008a = DB(WorkUnrelated(
    2008, "Start with Open Source",
    display="lui",
    authors="Lui, Kim Man and Chan, Keith CC",
    place=FAKE,
    pp="55--84",
    entrytype="article",
    publisher="Wiley Online Library",
    ID="lui2008start",
    placex="Software Development Rhythms: Harmonizing Agile Practices for Synergy",
))

madachy2008a = DB(WorkUnrelated(
    2008, "Assessing quality processes with ODC COQUALMO",
    display="madachy",
    authors="Madachy, R. and Boehm, B.",
    place=FAKE,
    pp="198--209",
    entrytype="article",
    volume="5007 LNCS",
    doi="10.1007/978-3-540-79588-9_18",
    note="cited By 10",
    ID="Madachy2008198",
    placex="Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)",
    other1="11, 2008, Leipzig, Germany, Lecture Notes in Computer Science, pp. 198-209,",
))

mao2008a = DB(WorkUnrelated(
    2008, "A coherent object-oriented (oo) software metric framework model: Software engineering",
    display="mao",
    authors="Mao, Mingzhi and Jiang, Yunfei",
    place=ICSE,
    pp="68--72",
    entrytype="inproceedings",
    volume="2",
    organization="IEEE",
    ID="mao2008coherent",
    cluster_id="10340103246267672850",
    scholar="http://scholar.google.com/scholar?cites=10340103246267672850&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Computer Science and Software Engineering, 2008 International Conference on",
))

markovic2008a = DB(WorkUnrelated(
    2008, "Linking business goals to process models in semantic business process modeling",
    display="markovic",
    authors="Markovic, I. and Kowalkiewicz, M.",
    place=FAKE,
    pp="332--338",
    entrytype="article",
    doi="10.1109/EDOC.2008.43",
    artnumber="4634785",
    note="cited By 51",
    ID="Markovic2008332",
    placex="Proceedings - 12th IEEE International Enterprise Distributed Object Computing Conference, EDOC 2008",
))

martins2008a = DB(WorkSnowball(
    2008, "ProPAMet: a Metric for process and project alignment",
    display="martins",
    authors="Martins, Paula Ventura and Da Silva, Alberto Rodrigues",
    place=CCIS,
    pp="201--212",
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
    scholar="http://scholar.google.com/scholar?cites=201686578103891917&as_sdt=2005&sciodt=0,5&hl=en",
    organization="Springer",
    cluster_id="201686578103891917",
    scholar_ok=True,
    selected_order="12",
    webofscience2015="1",
))

mishra2008a = DB(WorkUnrelated(
    2008, "Software process improvement methodologies for small and medium enterprises",
    display="mishra",
    authors="Mishra, D., & Mishra, A.",
    place=PROFES,
    entrytype="article",
    note="cited By 1",
    ID="Mishra2008",
    placex="Product-focused software process improvement",
    scholar="http://scholar.google.com/scholar?cites=4586401233150442603&as_sdt=2005&sciodt=0,5&hl=en",
))

mohagheghi2008a = DB(WorkUnrelated(
    2008, "An empirical investigation of software reuse benefits in a large telecom product",
    display="mohagheghi",
    authors="Mohagheghi, P. and Conradi, R.",
    place=ToSE,
    entrytype="article",
    volume="17",
    number="3",
    doi="10.1145/1363102.1363104",
    art_number="13",
    note="cited By 37",
    ID="Mohagheghi2008",
    placex="ACM Transactions on Software Engineering and Methodology",
))

montebelo2008a = DB(WorkUnrelated(
    2008, "Identificando dificuldades e benefícios do uso do PSP apoiado por ferramentas de 3{	extordfeminine}. gera{ç}ão",
    display="montebelo",
    authors="Montebelo, Renan Polo and others",
    place=FAKE,
    entrytype="article",
    publisher="Universidade Federal de São Carlos",
    ID="montebelo2008identificando",
    placex="",
))

monteiro2008a = DB(WorkUnrelated(
    2008, "Defini{ç}ão de um catálogo de medidas para a análise de desempenho de processo de software",
    display="monteiro",
    authors="Monteiro, Luis Felipe Salin and others",
    place=FAKE,
    entrytype="article",
    publisher="Universidade Católica de Brasília",
    ID="monteiro2008definiccao",
    cluster_id="5865241509283977422",
    scholar="http://scholar.google.com/scholar?cites=5865241509283977422&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

napier2008a = DB(WorkUnrelated(
    2008, "Software process re-engineering: a model and its application to an industrial case study",
    display="napier",
    authors="Napier, Nannette P and Kim, Jonathan and Mathiassen, Lars",
    place=SPIP,
    pp="451--471",
    entrytype="article",
    volume="13",
    number="5",
    publisher="Wiley Online Library",
    ID="napier2008software",
    cluster_id="2736453439848134766",
    scholar="http://scholar.google.com/scholar?cites=2736453439848134766&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process: Improvement and Practice",
))

niebuhr2008a = DB(WorkUnrelated(
    2008, "Engaging Patterns: Challenges and Means Shown by an Example",
    display="niebuhr",
    authors="Niebuhr, Sabine and Kohler, Kirstin and Graf, Christian",
    place=FAKE,
    pp="586--600",
    entrytype="inproceedings",
    editor="Gulliksen, Jan and Harning, Morton Borup and Palanque, Philippe and van der Veer, Gerrit C. and Wesson, Janet",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/978-3-540-92698-6_35",
    springer="1",
    placex="Engineering Interactive Systems",
))

nobre2008a = DB(WorkUnrelated(
    2008, "The pursuit of cognition in manufacturing organizations",
    display="nobre",
    authors="Farley S. Nobre and Andrew M. Tobias and David S. Walker",
    place=FAKE,
    pp="145 -- 157",
    entrytype="article",
    volume="27",
    number="4",
    note="",
    issn="0278-6125",
    doi="https://doi.org/10.1016/j.jmsy.2009.01.001",
    link="https://www.sciencedirect.com/science/article/pii/S0278612509000235",
    ID="Nobre2008145",
    sciencedirect="1",
    placex="Journal of Manufacturing Systems",
    sciencedirect2015="1",
))

nollen2008a = DB(WorkUnrelated(
    2008, "Software Industry Performance in India and China",
    display="nollen",
    authors="Nollen, S.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Nollen2008",
    placex="INDIA in the Emerging Global Order",
))

pereira2008a = DB(WorkUnrelated(
    2008, "What do software practitioners really think about project success: A cross-cultural comparison",
    display="pereira",
    authors="Javier Pereira and Narciso Cerpa and June Verner and Mario Rivas and J. Drew Procaccino",
    place=JSS,
    pp="897 -- 907",
    entrytype="article",
    volume="81",
    number="6",
    note="Agile Product Line Engineering",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2007.07.032",
    link="https://www.sciencedirect.com/science/article/pii/S0164121207001847",
    keyword="Freedom",
    ID="Pereira2008897",
    sciencedirect="1",
    placex="Journal of Systems and Software",
    sciencedirect2015="1",
))

peters2008a = DB(WorkUnrelated(
    2008, "Quantifying the yield of risk-bearing IT-portfolios",
    display="peters",
    authors="R.J. Peters and C. Verhoef",
    place=SCP,
    pp="17 -- 56",
    entrytype="article",
    volume="71",
    number="1",
    note="",
    issn="0167-6423",
    doi="https://doi.org/10.1016/j.scico.2007.11.001",
    link="https://www.sciencedirect.com/science/article/pii/S016764230700189X",
    keyword="Time over-runs",
    ID="Peters200817",
    sciencedirect="1",
    placex="Science of Computer Programming",
    sciencedirect2015="1",
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

ponisio2008a = DB(WorkUnrelated(
    2008, "Analysing Boundary Objects to Develop Results that Support Business Goals",
    display="ponisio",
    authors="M. L. Ponisio and P. Vruggink",
    place=FAKE,
    pp="516-521",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="knowledge management;outsourcing;project management;software development management;boundary object;boundary object translation;business goal;coordination practice;knowledge coordination;mediator;multiple information passage point;outsourcing project;software development;work visibility;Collaborative work;Companies;Concrete;Costs;Guidelines;Information analysis;Knowledge transfer;Outsourcing;Programming;Project management;outsourcing;project management;software development",
    doi="10.1109/CIMCA.2008.131",
    issn="",
    ID="5172679",
    placex="2008 International Conference on Computational Intelligence for Modelling Control Automation",
    ieee2015="1",
))

porter2008a = DB(WorkUnrelated(
    2008, "The five competitive forces that shape strategy",
    display="porter",
    authors="ME Porter",
    place=FAKE,
    other1="86(1):7893",
    placex="Harv Bus Rev",
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

qumer2008a = DB(WorkUnrelated(
    2008, "A framework to support the evaluation, adoption and improvement of agile methods in practice",
    display="qumer",
    authors="A. Qumer and B. Henderson-Sellers",
    place=JSS,
    pp="1899 -- 1919",
    entrytype="article",
    volume="81",
    number="11",
    note="",
    issn="0164-1212",
    doi="https://doi.org/10.1016/j.jss.2007.12.806",
    link="https://www.sciencedirect.com/science/article/pii/S0164121208000113",
    keyword="Industry case studies",
    ID="Qumer20081899",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

rasidi2008a = DB(WorkUnrelated(
    2008, "The adoption of software process improvement (SPI) Program in the construction industry",
    display="rasidi",
    authors="Rasidi, Hanim and Ibrahim, Rahinah",
    place=FAKE,
    pp="79--90",
    entrytype="article",
    volume="3",
    number="1",
    ID="rasidi2008adoption",
    cluster_id="12183783356567413526",
    scholar="http://scholar.google.com/scholar?cites=12183783356567413526&as_sdt=2005&sciodt=0,5&hl=en",
    placex="ALAM CIPTA, International Journal on Sustainable Tropical Design Research & Practice",
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

rifaut2008a = DB(WorkUnrelated(
    2008, "Using Goal-Oriented Requirements Engineering for Improving the Quality of ISO/IEC 15504 based Compliance Assessment Frameworks",
    display="rifaut",
    authors="A. Rifaut and E. Dubois",
    place=FAKE,
    pp="33--42",
    entrytype="inproceedings",
    volume="",
    number="",
    keyword="Business;Context modeling;IEC standards;ISO standards;Knowledge management;Process design;Project management;Risk management;Software systems;Taxonomy;Business Process;Compliance;Goal-Oriented;ISO/IEC 15504;Requirements Engineering",
    doi="10.1109/RE.2008.44",
    issn="1090-705X",
    ID="4685650",
    ieee="1",
    placex="2008 16th IEEE International Requirements Engineering Conference",
    ieee2015="1",
    gs="1",
    organization="IEEE",
))

rose2008a = DB(WorkUnrelated(
    2008, "Managerial and Organizational Assumptions in the CMMs",
    display="rose",
    authors="Rose, Jeremy and Aaen, Ivan and Nielsen, Peter Axel",
    place=FAKE,
    pp="9",
    entrytype="article",
    ID="rose2008managerial",
    cluster_id="15390234121326747672",
    scholar="http://scholar.google.com/scholar?cites=15390234121326747672&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Processes & Knowledge",
))

rovegård2008a = DB(WorkUnrelated(
    2008, "An empirical study on views of importance of change impact analysis issues",
    display="rovegård",
    authors="Rovegård, Per and Angelis, Lefteris and Wohlin, Claes",
    place=ToSE,
    pp="516--530",
    entrytype="article",
    volume="34",
    number="4",
    publisher="IEEE",
    ID="rovegaard2008empirical",
    cluster_id="4198046884117281611",
    scholar="http://scholar.google.com/scholar?cites=4198046884117281611&as_sdt=2005&sciodt=0,5&hl=en",
    placex="IEEE Transactions on Software Engineering",
))

sanders2008a = DB(WorkUnrelated(
    2008, "Finding out what really happened after SPI assistance in Ireland",
    display="sanders",
    authors="Sanders, Martha H",
    place=FAKE,
    entrytype="article",
    publisher="University of Limerick",
    ID="sanders2008finding",
    placex="",
))

santana2008a = DB(WorkUnrelated(
    2008, "Incongruência para com as Atividades Primárias de Interven{ç}ão: uma Barreira a Iniciativas de MPS",
    display="santana",
    authors="Santana, André Felipe Lemos and de Moura, Hermano Perrelli",
    place=FAKE,
    entrytype="inproceedings",
    volume="6",
    ID="santana2008incongruencia",
    cluster_id="8580024173035980954",
    scholar="http://scholar.google.com/scholar?cites=8580024173035980954&as_sdt=2005&sciodt=0,5&hl=en",
    placex="IV Workshop Um Olhar Sociotécnico sobre a Engenharia de Software, Florianópolis-SC",
))

santos2008a = DB(WorkUnrelated(
    2008, "Ambientes de Engenharia de Software Orientados a Corpora{ç}ão",
    display="santos",
    authors="Santos, Gleison and Rocha, Ana Regina and Travassos, Guilherme Horta",
    place=Thesis,
    entrytype="phdthesis",
    ID="santos2008ambientes",
    cluster_id="3210481893095229341",
    scholar="http://scholar.google.com/scholar?cites=3210481893095229341&as_sdt=2005&sciodt=0,5&hl=en",
    local="Tese de D. Sc., COPPE/UFRJ, Rio de Janeiro, RJ, Brasil",
    placex="",
))

sharma2008a = DB(WorkUnrelated(
    2008, "Business value through product line engineering - a case study",
    display="sharma",
    authors="Sharma, D. and Aurum, A. and Paech, B.",
    place=SEAA,
    pp="167--174",
    entrytype="article",
    doi="10.1109/SEAA.2008.19",
    art_number="4725719",
    note="cited By 6",
    ID="Sharma2008167",
    placex="EUROMICRO 2008 - Proceedings of the 34th EUROMICRO Conference on Software Engineering and Advanced Applications, SEAA 2008",
))

shen2008a = DB(WorkUnrelated(
    2008, "Software Engineering Challenges in Small Companies",
    display="shen",
    authors="Shen, Yiyun",
    place=FAKE,
    entrytype="article",
    ID="shen2008software",
    cluster_id="15244587620961666101",
    scholar="http://scholar.google.com/scholar?cites=15244587620961666101&as_sdt=2005&sciodt=0,5&hl=en",
    placex="UNIVERSITY OF HELSINKI",
))

siritanachot2008a = DB(WorkUnrelated(
    2008, "The Impact of Interventional Change Techniques on an Internet Banking Cross-functional Team",
    display="siritanachot",
    authors="Siritanachot, Chansit",
    place=Thesis,
    entrytype="phdthesis",
    ID="siritanachot2008impact",
    local="The University of Waikato",
    placex="",
))

songnisai2008a = DB(WorkUnrelated(
    2008, "Using Capability Maturity Model to Assess the Effectiveness of ISO 9001: 2000 Implementation: Case Study at Sanyo Semiconductor (Thailand) Co., Ltd",
    display="songnisai",
    authors="Songnisai, Sakulrat",
    place=Thesis,
    entrytype="phdthesis",
    ID="songnisai2008using",
    local="Kasetsart University",
    placex="",
))

spork2008a = DB(WorkUnrelated(
    2008, "Establishment of a performance driven improvement programme",
    display="spork",
    authors="Spork, Gunther and Pichler, Uwe",
    place=SPIP,
    pp="371--382",
    entrytype="article",
    volume="13",
    number="4",
    publisher="Wiley Online Library",
    ID="spork2008establishment",
    cluster_id="5365433577894133177",
    scholar="http://scholar.google.com/scholar?cites=5365433577894133177&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process: Improvement and Practice",
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

staples2008a = DB(WorkUnrelated(
    2008, "Systematic review of organizational motivations for adopting CMM-based \SPI",
    display="staples",
    authors="Mark Staples and Mahmood Niazi",
    place=IST,
    pp="605 -- 620",
    entrytype="article",
    volume="50",
    number="78",
    note="",
    issn="0950-5849",
    doi="https://doi.org/10.1016/j.infsof.2007.07.003",
    link="https://www.sciencedirect.com/science/article/pii/S0950584907000778",
    keyword="Software Process Improvement",
    ID="Staples2008605",
    sciencedirect="1",
    placex="Information and Software Technology",
    scholar="http://scholar.google.com/scholar?cites=14831048305439200443&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Elsevier",
    cluster_id="14831048305439200443",
))

sureshchandra2008a = DB(WorkUnrelated(
    2008, "Adopting agile in distributed development",
    display="sureshchandra",
    authors="Sureshchandra, K. and Shrinivasavadhani, J.",
    place=FAKE,
    pp="217--221",
    entrytype="article",
    doi="10.1109/ICGSE.2008.25",
    art_number="4638670",
    note="cited By 44",
    ID="Sureshchandra2008217",
    placex="Proceedings - 2008 3rd IEEE International Conference Global Software Engineering, ICGSE 2008",
))

tjornehoj2008a = DB(WorkUnrelated(
    2008, "Between control and drift: negotiating improvement in a small software firm",
    display="tjornehoj",
    authors="Tjornehoj, Gitte and Mathiassen, Lars",
    place=FAKE,
    pp="69--90",
    entrytype="article",
    volume="21",
    number="1",
    publisher="Emerald Group Publishing Limited",
    ID="tjornehoj2008between",
    cluster_id="15402895200947573760",
    scholar="http://scholar.google.com/scholar?cites=15402895200947573760&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information Technology & People",
))

tjørnehøj2008a = DB(WorkUnrelated(
    2008, "The Role of improvisation in adoption of process technology in a small software firm",
    display="tjørnehøj",
    authors="Tjørnehøj, Gitte and Mathiassen, Lars",
    place=FAKE,
    pp="137",
    entrytype="article",
    publisher="Software Innovation Publisher Aalborg, Denmark",
    ID="tjornehoj2008role",
    cluster_id="1615703338188678444",
    scholar="http://scholar.google.com/scholar?cites=1615703338188678444&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Processes & Knowledge",
))

umarji2008a = DB(WorkUnrelated(
    2008, "Why do programmers avoid metrics?",
    display="umarji",
    authors="Umarji, M. and Seaman, C.",
    place=ESEM,
    pp="129--138",
    entrytype="conference",
    doi="10.1145/1414004.1414027",
    note="cited By 8",
    ID="Umarji2008129",
    placex="ESEM'08: Proceedings of the 2008 ACM-IEEE International Symposium on Empirical Software Engineering and Measurement",
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

wang2008a = DB(WorkUnrelated(
    2008, "Estimating fixing effort and schedule based on defect injection distribution",
    display="wang",
    authors="Wang, Qing and Gou, Lang and Jiang, Nan and Che, Meiru and Zhang, Ronghui and Yang, Yun and Li, Mingshu",
    place=SPIP,
    pp="35--50",
    entrytype="article",
    volume="13",
    number="1",
    publisher="Wiley Online Library",
    ID="wang2008estimating",
    cluster_id="10037802072190717452",
    scholar="http://scholar.google.com/scholar?cites=10037802072190717452&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Software Process: Improvement and Practice",
))

wirth2008a = DB(WorkUnrelated(
    2008, "A Brief History of Software Engineering",
    display="wirth",
    authors="Wirth, N.",
    place=FAKE,
    pp="32--39",
    entrytype="article",
    volume="30",
    number="3",
    doi="10.1109/MAHC.2008.33",
    note="cited By 18",
    ID="Wirth200832",
    placex="IEEE Annals of the History of Computing",
))

wojcicki2008a = DB(WorkUnrelated(
    2008, "Evaluating and combining verification and validation technologies,",
    display="wojcicki",
    authors="Wojcicki, M. A.",
    place=FAKE,
    placex="Brisbane, Queensland, Australia. School of Information Technol and Elec Engineering, University of Queensland",
))

zhai2008a = DB(WorkUnrelated(
    2008, "automated process quality assurance for distributed software development",
    display="zhai",
    authors="Zhai, Jian and Yang, Qiusong and Yang, Ye and Xiao, Junchao and Wang, Qing and Li, Mingshu",
    place=FAKE,
    pp="196--210",
    entrytype="inproceedings",
    organization="Springer",
    ID="zhai2008automated",
    placex="International Conference on Software Engineering Approaches for Offshore and Outsourced Development",
))

zhang2008a = DB(WorkUnrelated(
    2008, "Capability assessment of individual software development processes using software repositories and dea",
    display="zhang",
    authors="Zhang, Shen and Wang, Yongji and Yang, Ye and Xiao, Junchao",
    place=ICSE,
    pp="147--159",
    entrytype="inproceedings",
    organization="Springer",
    ID="zhang2008capability",
    cluster_id="8413074065970719792",
    scholar="http://scholar.google.com/scholar?cites=8413074065970719792&as_sdt=2005&sciodt=0,5&hl=en",
    placex="International Conference on Software Process",
))

zhang2008b = DB(WorkUnrelated(
    2008, "Basic research in computer science and software engineering at SKLCS",
    display="zhang b",
    authors="Zhang, Jian and Zhang, Wenhui and Zhan, Naijun and Shen, Yidong and Chen, Haiming and Zhang, Yunquan and Wang, Yongji and Wu, Enhua and Wang, Hongan and Zhu, Xueyang",
    place=FAKE,
    pp="1--11",
    entrytype="article",
    volume="2",
    number="1",
    publisher="Springer",
    ID="zhang2008basic",
    placex="Frontiers of Computer Science in China",
))

zhang2008c = DB(WorkUnrelated(
    2008, "Applying Six Sigma in Software Companies for Process Improvement",
    display="zhang c",
    authors="Zhang, Long and Khan, Adnan Rafiq",
    place=FAKE,
    entrytype="misc",
    ID="zhang2008applying",
    cluster_id="2658004860669062059",
    scholar="http://scholar.google.com/scholar?cites=2658004860669062059&as_sdt=2005&sciodt=0,5&hl=en",
    placex="",
))

zhang2008d = DB(WorkUnrelated(
    2008, "A Laboratory for Basic Research in Computer Science and Software Engineering",
    alias=(0, "A Laboratory for Basic Research in Computer Science and Software Engineering",),
    display="zhang",
    authors="Zhang, Jian and Zhang, Wenhui and Zhan, Naijun and Shen, Yidong and Chen, Haiming and Zhang, Yunquan and Wang, Yongji and Wu, Enhua and Wang, Hongan and Zhu, Xueyang",
    place=FAKE,
    entrytype="article",
    ID="zhanglaboratory",
    placex="",
))
