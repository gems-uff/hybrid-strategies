# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

basili1988a = DB(WorkUnrelated(
    1988, "The TAME Project: Towards Improvement-Oriented Software Environments",
    display="basili",
    authors="Basili, V.R. and Dieter Rombach, H.",
    place=ToSE,
    pp="758-773",
    entrytype="article",
    volume="14",
    number="6",
    doi="10.1109/32.6156",
    note="cited By 630",
    ID="Basili1988758",
    placex="IEEE Transactions on Software Engineering",
))

basili1988b = DB(WorkUnrelated(
    1988, "The TAME project: towards improvement-oriented software environments. IEEE Transactions on Software Engineering",
    display="basili b",
    authors="V. Basili,  H., Rombach",
    place=FAKE,
    placex="14: 758773",
))

curtis1988a = DB(WorkUnrelated(
    1988, "A field study of the software design process for large systems",
    display="curtis",
    authors="Curtis, B. and Krasner, H. and Iscoe, N.",
    place=CACM,
    pp="1268-1287",
    entrytype="article",
    volume="31",
    number="11",
    doi="10.1145/50087.50089",
    note="cited By 1112",
    ID="Curtis19881268",
    placex="Communications of the ACM",
))

david1988a = DB(WorkUnrelated(
    1988, "The Method of Paired Comparisons",
    display="david",
    authors="David, H.A.",
    place=FAKE,
    entrytype="article",
    note="cited By 791",
    ID="David1988",
    placex="Lubrecht & Cramer, Limited",
))

gilb1988a = DB(WorkUnrelated(
    1988, "Principles of Software Engineering Project Management,",
    display="gilb",
    authors="Gilb, T.",
    place=FAKE,
    placex="Addison-Wesley,",
))

humphrey1988a = DB(WorkUnrelated(
    1988, "Characterizing the Software Process",
    display="humphrey",
    authors="Humphrey, W.S.,",
    place=IEEES,
    entrytype="article",
    note="cited By 1",
    ID="Humphrey1988",
    placex="IEEE Software, Vol. 5, No. 2, Pp. 73-79",
))
