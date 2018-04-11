# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

osterweil1987a = DB(WorkUnrelated(
    1987, "Software Processes Are Software Too",
    display="osterweil",
    authors="Osterweil, L.",
    place=FAKE,
    entrytype="article",
    note="cited By 1",
    ID="Osterweil1987",
    placex="Proc. Ninth Int'l Conf. Software Eng., Pp. 2-12",
))

rombach1987a = DB(WorkUnrelated(
    1987, "Quantitative assessment of maintenance an industrial",
    display="rombach",
    authors="Rombach, H.D., Basili, V.R.",
    place=FAKE,
    other1="Proc. of Conf. on Software Maintenance,",
    other2="Austin, Texas.",
    other3="IEEE Comp. Soc.",
    placex="Case Study, pp. 13 5-147,",
))
