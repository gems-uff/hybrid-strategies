# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

conradi1994a = DB(WorkUnrelated(
    1994, "EPOS:  Object-oriented  cooperative  process  modeling",
    display="conradi1994a",
    authors="Conradi  R.,  Hagaseth  M.,  Larsen  J.O.,  et  al.",
    place=FAKE,
    placex="Software Process Modeling and Technology",
))

haase1994a = DB(WorkUnrelated(
    1994, "Bootstrap: Fine-Tuning Process Assessment.",
    display="haase",
    authors="Haase, V., Messnarz, R., Koch, G.,et al",
    place=IEEES,
    placex="IEEE Software",
))

nuseibeh1994a = DB(WorkUnrelated(
    1994, "A multi-perspective framework for method integration",
    display="nuseibeh",
    authors="Nuseibeh, Bashar",
    place=FAKE,
    entrytype="article",
    publisher="Citeseer",
    ID="nuseibeh1994multi",
    gs2016="1",
    placex="Department of Computing",
))

ramakrishnan1994a = DB(WorkUnrelated(
    1994, "Quality factors for resource allocation problems-linking domain analysis and object-oriented software engineering",
    display="ramakrishnan",
    authors="Ramakrishnan, Sita",
    place=FAKE,
    pp="68--72",
    entrytype="inproceedings",
    organization="IEEE",
    ID="ramakrishnan1994quality",
    gs2016="1",
    placex="Software Testing, Reliability and Quality Assurance, 1994. Conference Proceedings., First International Conference on",
))
