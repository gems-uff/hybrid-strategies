# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

delany1998a = DB(WorkOk(
    1998, "The limits of CBR in software project estimation",
    display="delany",
    authors="Delany, S.J. and Cunningham, P. and Wilke, W.",
    place=GWCBR,
    entrytype="article",
    note="cited By 5",
    ID="Delany1998",
))

kitchenham1998a = DB(WorkOk(
    1998, "A procedure for analyzing unbalanced datasets",
    display="kitchenham",
    authors="Kitchenham, Barbara",
    place=ToSE,
    pp="278--301",
    entrytype="article",
    volume="24",
    number="4",
    doi="10.1109/32.677185",
    note="cited By 69",
    ID="Kitchenham1998278",
    cluster_id="3452730155060426062",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=3452730155060426062&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
