# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

takeuchi1986a = DB(WorkUnrelated(
    1986, "The new new product development game",
    display="takeuchi",
    authors="Takeuchi, H. and Nonaka, I.",
    place=FAKE,
    pp="137-146",
    entrytype="article",
    volume="64",
    number="1",
    note="cited By 39",
    ID="Takeuchi1986137",
    placex="Harvard Business Review",
))

takeuchi1986b = DB(WorkUnrelated(
    1986, "New Product Development Game",
    display="takeuchi b",
    authors="Takeuchi and Nonaka",
    place=FAKE,
    entrytype="article",
    ID="Takeuchi1986",
    placex="Harvard Business Review",
))
