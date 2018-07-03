# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

isoiec1998a = DB(WorkUnrelated(
    1998, "Standard  For  Software  Process  Assessment  (Parts  1-9)",
    display="isoiec1998a",
    authors="ISO IEC",
    place=FAKE,
    other1="ISO/IEC 15504 International St andards organization",
    placex="ISO/IEC Technical Report (TR)",
))

marttiin1998a = DB(WorkUnrelated(
    1998, "Similarities and differences of method engineering and process engineering approaches",
    display="marttiin",
    authors="Marttiin, Pentti and Koskinen, Minna",
    place=FAKE,
    pp="420--424",
    entrytype="article",
    ID="marttiin1998similarities",
    gs2016="1",
    placex="Effective Utilization and Management of Emerging Information Technologies",
))
