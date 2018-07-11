# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

glaser1978a = DB(WorkUnrelated(
    1978, "Theoretical Sensitivity: Advances in the Methodology of Grounded Theory",
    display="glaser",
    authors="Glaser, B.G.",
    place=FAKE,
    entrytype="article",
    note="cited By 2880",
    ID="Glaser1978",
    placex="Sociology Press Mill Valley",
))

glaser1978b = DB(WorkUnrelated(
    1978, "Advances in the methodology of grounded theory. Theoretical sensitivity",
    display="glaser b",
    authors="Glaser, B.G.",
    place=FAKE,
    entrytype="article",
    note="cited By 202",
    ID="Glaser1978",
    placex="Advances in the Methodology of Grounded Theory: Theoretical Sensitivity",
))

susman1978a = DB(WorkUnrelated(
    1978, "An assessment of the scientific merits of action research",
    display="susman",
    authors="Susman, G.I. and Evered, R.D.",
    place=FAKE,
    pp="582--603",
    entrytype="article",
    volume="23",
    number="4",
    note="cited By 1095",
    ID="Susman1978582",
    placex="Administrative Science Quarterly",
))
