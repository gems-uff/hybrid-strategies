# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bandinelli1993a = DB(WorkUnrelated(
    1993, "Cooperation  support  in  the  SPADE Environment:   A   Case   Study",
    display="bandinelli",
    authors="Bandinelli,  S.,  Braga,  M.,  Fuggetta,  A.,  Lavazza,  L.",
    place=FAKE,
    placex="Proceeding   of   Workshop   on   Computer   Supported Cooperative Work Petri Nets and Related Formalisms",
))

ben1993a = DB(WorkUnrelated(
    1993, "Process Evolution in the Marvel Environment",
    display="ben",
    authors="Ben-Shaul, I.Z., Kaiser, G.E.",
    place=FAKE,
    placex="Proceedings of   8th   International   Software   Process   Workshop:   State   of   the   Practice   in   Process Technology",
))

paulk1993a = DB(WorkUnrelated(
    1993, "CMM  Capability  Maturity Model SM for Software. Version 1.1",
    display="Paulk",
    authors="Paulk  M.C.,  Curtis,  B.,  Chrissis,  M.B.,  Weber,  C.V.",
    place=EBSE,
    other1="CMU/SEI",
    placex="Technical Report",
))
