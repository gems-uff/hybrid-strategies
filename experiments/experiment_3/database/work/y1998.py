# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

iso1998a = DB(WorkUnrelated(
    1998, "Information technology — Software process assessment",
    display="iso",
    authors="ISO",
    place=FAKE,
    other1="ISO/IEC, 15504-9, (1998-08-15).",
    placex="Part 9 Vocabulary, First edition,",
))

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

musen1998a = DB(WorkUnrelated(
    1998, "Domain Ontologies in Software Engineering: Use of protégé with the EON Architecture",
    display="musen",
    authors="M. A. Musen",
    place=FAKE,
    placex="Methods of Information in Medicine 37 1998 pp. 540-550",
))

obrien1998a = DB(WorkUnrelated(
    1998, "FIPA - Towards a Standard for Software Agents",
    display="obrien",
    authors="P.D. O'Brien and R.C. Nicol,",
    place=FAKE,
    placex="BT Technology Journal, 16 (3):51-59,",
))
