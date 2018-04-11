# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

deming1986a = DB(WorkUnrelated(
    1986, "Out of crisis: Quality, productivity and competitive position",
    display="deming",
    authors="Deming, W.E.",
    place=FAKE,
    entrytype="article",
    note="cited By 331",
    ID="Deming1986",
    placex="Cambridge University Press",
))

deming1986b = DB(WorkUnrelated(
    1986, "Out of the crisis",
    display="deming b",
    authors="WE Deming",
    place=FAKE,
    other1="Education Services, Cambridge, MA",
    placex="Massachusetts Institute of Technology, Center for Advance",
))

takeuchi1986a = DB(WorkUnrelated(
    1986, "The new product development game",
    display="takeuchi",
    authors="Takeuchi, H. and Nonaka, I.",
    place=FAKE,
    pp="137--146",
    entrytype="article",
    volume="64",
    number="1",
    note="cited By 740",
    ID="Takeuchi1986137",
    placex="Harvard Business Review",
))
