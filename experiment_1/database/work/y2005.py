# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

beecham2005a = DB(WorkUnrelated(
    2005, "Using an expert panel to validate a requirements process improvement model",
    display="beecham",
    authors="Sarah Beecham and Tracy Hall and Carol Britton and Michaela Cottee and Austen Rainer",
    place=JSS,
    pp="251 - 275",
    entrytype="article",
    volume="76",
    number="3",
    ID="Beecham2005251",
    sciencedirect="1",
    placex="Journal of Systems and Software",
))

bleistein2005a = DB(WorkUnrelated(
    2005, "Strategic Alignment in Requirements Analysis for Organizational IT: An Integrated Approach",
    display="bleistein",
    authors="Bleistein, Steven J. and Cox, Karl and Verner, June",
    place=FAKE,
    pp="1300--1307",
    entrytype="inproceedings",
    series="SAC '05",
    isbn="1-58113-964-0",
    location="Santa Fe, New Mexico",
    ID="Bleistein:2005:SAR:1066677.1066972",
    acm="1",
    placex="Proceedings of the 2005 ACM Symposium on Applied Computing",
))

caetano2005a = DB(WorkUnrelated(
    2005, "Using Roles and Business Objects to Model and Understand Business Processes",
    display="caetano",
    authors="Caetano, Artur and Silva, Antonio Ritó and Tribolet, José",
    place=FAKE,
    pp="1308--1313",
    entrytype="inproceedings",
    series="SAC '05",
    isbn="1-58113-964-0",
    location="Santa Fe, New Mexico",
    ID="Caetano:2005:URB:1066677.1066973",
    acm="1",
    placex="Proceedings of the 2005 ACM Symposium on Applied Computing",
))

chaudet2005a = DB(WorkUnrelated(
    2005, "Optimal Positioning of Active and Passive Monitoring Devices",
    display="chaudet",
    authors="Chaudet, Claude and Fleury, Eric and Lassous, Isabelle Guérin and Rivano, Hervé and Voge, Marie-Emilie",
    place=FAKE,
    pp="71--82",
    entrytype="inproceedings",
    series="CoNEXT '05",
    isbn="1-59593-197-X",
    location="Toulouse, France",
    ID="Chaudet:2005:OPA:1095921.1095932",
    acm="1",
    placex="Proceedings of the 2005 ACM Conference on Emerging Network Experiment and Technology",
))

gairing2005a = DB(WorkUnrelated(
    2005, "Selfish Routing with Incomplete Information",
    display="gairing",
    authors="Gairing, Martin and Monien, Burkhard and Tiemann, Karsten",
    place=FAKE,
    pp="203--212",
    entrytype="inproceedings",
    series="SPAA '05",
    isbn="1-58113-986-1",
    location="Las Vegas, Nevada, USA",
    ID="Gairing:2005:SRI:1073970.1074000",
    acm="1",
    placex="Proceedings of the Seventeenth Annual ACM Symposium on Parallelism in Algorithms and Architectures",
))

snedaker2005a = DB(WorkUnrelated(
    2005, "Chapter 1 - What's project management got to do with IT?",
    display="snedaker",
    authors="Snedaker, Susan and ,  and Hoenig, Nels",
    place=FAKE,
    pp="1 - 29",
    entrytype="incollection",
    editor="Snedaker, Susan and ,  and Hoenig, Nels",
    publisher="Syngress",
    edition="",
    address="Burlington",
    series="How to Cheat",
    isbn="978-1-59749-037-5",
    doi="https://doi.org/10.1016/B978-159749037-5/50005-8",
    link="https://www.sciencedirect.com/science/article/pii/B9781597490375500058",
    key="tagkey20051",
    ID="tagkey20051",
    sciencedirect="1",
    placex="How to Cheat at \{IT\} Project Management",
))

taxen2005a = DB(WorkUnrelated(
    2005, "A sociotechnical approach towards alignment",
    display="taxen",
    authors="Taxen, Lars",
    place=SPIP,
    pp="427 - 439",
    entrytype="article",
    volume="10",
    number="4",
    ID="2005529614780",
    elcompendex="1",
    placex="Software Process Improvement and Practice",
))

trienekens2005a = DB(WorkSnowball(
    2005, "Business-oriented process improvement: Practices and experiences at Thales Naval the Netherlands (TNNL)",
    display="trienekens",
    authors="Trienekens, J.J.M. and Kusters, R.J. and Rendering, B. and Stokla, K.",
    place=IST,
    pp="67-79",
    entrytype="article",
    volume="47",
    number="2",
    doi="10.1016/j.infsof.2004.06.003",
    note="cited By 9",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-10644225897&doi=10.1016%2fj.infsof.2004.06.003&partnerID=40&md5=0de80b68bc7607407aa90eac4dc92be6",
    document_type="Article",
    source="Scopus",
    ID="Trienekens200567",
    sciencedirect="1",
    placex="Information and Software Technology",
))

vanter2005a = DB(WorkUnrelated(
    2005, "HPC Needs a Tool Strategy",
    display="vanter",
    authors="Van De Vanter, Michael L. and Post, D. E. and Zosel, Mary E.",
    place=FAKE,
    pp="55--59",
    entrytype="inproceedings",
    series="SE-HPCS '05",
    isbn="1-59593-117-1",
    location="St. Louis, Missouri",
    ID="VanDeVanter:2005:HNT:1145319.1145335",
    acm="1",
    placex="Proceedings of the Second International Workshop on Software Engineering for High Performance Computing System Applications",
))

wang2005a = DB(WorkSnowball(
    2005, "Measuring and improving software process in China",
    display="wang",
    authors="Wang, Q. and Li, M.",
    place=ESEM,
    pp="183-192",
    entrytype="inproceedings",
    doi="10.1109/ISESE.2005.1541827",
    art_number="1541827",
    note="cited By 22",
    link="https://www.scopus.com/inward/record.uri?eid=2-s2.0-33745888881&doi=10.1109%2fISESE.2005.1541827&partnerID=40&md5=a6cbea31fe63657e144e9188f9310d5c",
    document_type="Conference Paper",
    source="Scopus",
    ID="Wang2005183",
))
