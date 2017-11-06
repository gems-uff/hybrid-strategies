# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1999a = DB(WorkOk(
    1999, "Building knowledge through families of experiments",
    display="basili",
    authors="Basili, Victor R and Shull, Forrest and Lanubile, Filippo",
    place=ToSE,
    entrytype="inproceedings",
    volume="25",
    cluster_id="8728852333858540790",
    publisher="IEEE",
    pp="456--473",
    scholar="http://scholar.google.com/scholar?cites=8728852333858540790&as_sdt=2005&sciodt=0,5&hl=en",
    number="4",
    scholar_ok=True,
))

briand1999a = DB(Work(
    1999, "An assessment and comparison of common software cost estimation modeling techniques",
    display="briand1999a",
    authors="Briand, L.C., Emam, K. El, Surmann, D., Wieczorek, I. and Maxwell, K.",
    place1="In 21st International Conference on Software Engineering (ICSE 99)",
    other1="313–323",   
))

hayes1999a = DB(WorkOk(
    1999, "Research synthesis in software engineering: A case for meta-analysis",
    display="hayes",
    authors="Hayes, W.",
    place=ISMS,
    other1="143151",
))

maxwell1999a = DB(Work(
    1999, "Performance evaluation of general and company specific models in software development effort estimation",
    display="maxwell",
    authors="Maxwell, K., Wassenhove, L.V., and Dutta, S.",
    place1="In Proceedings Management Science",
    other1="787-803",   
))

miller1999a = DB(WorkOk(
    1999, "Can results from software engineering experiments be safely combined?",
    display="miller",
    authors="Miller, J.",
    place=ISSM,
    other1="152-158",
))
