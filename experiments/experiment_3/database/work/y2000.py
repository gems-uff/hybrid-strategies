# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

dutton2000a = DB(WorkUnrelated(
    2000, "Trust--Issues in the design and development of electronic commerce systems",
    display="dutton",
    authors="Dutton, Philip D",
    place=FAKE,
    entrytype="article",
    ID="dutton2000trust",
    gs2016="1",
    placex="Bachelor's thesis, Griffith university, School of Computing and Information Technology",
))

iivari2000a = DB(WorkUnrelated(
    2000, "A Dynamic Framework for Classifying",
    alias=(2000, "A dynamic framework for classifying information systems development methodologies and approaches", ),
    display="iivari",
    authors="Iivari, Juhani and Hirschheim, Rudy and Klein, Heinz K",
    place=FAKE,
    pp="179--218",
    entrytype="article",
    volume="17",
    number="3",
    publisher="Taylor & Francis",
    ID="iivari2000dynamic",
    gs2016="1",
    placex="Journal of management information systems",
))

iso2000a = DB(WorkUnrelated(
    2000, "ISO 9001:2000 Quality Management Systems -- Requirement",
    display="iso",
    authors="ISO",
    place=FAKE,
    placex="accessed site",
))

mair2000a = DB(WorkUnrelated(
    2000, "Agent-based Process Model Integration in Virtual Software Corporations",
    display="mair",
    authors="Quentin Mair  and Zsolt Haag",
    place=FAKE,
    entrytype="article",
    ID="quentin2000agent",
    gs2016="1",
    placex="Proceedings of the ECAI 2000 Workshop 13 Agent Technologies and Their Application Scenarios in Logistics",
))

nick2000a = DB(WorkUnrelated(
    2000, "Guidelines for evaluation and improvement of reuse and experience repository systems through measurement programs",
    display="nick",
    authors="Nick, Markus and Feldmann, Raimund",
    place=FAKE,
    entrytype="inproceedings",
    ID="nick2000guidelines",
    gs2016="1",
    placex="Proc. 3rd European Software Measurement Conference (FESMA-AEMES 2000), Madrid, Spain",
))

wang2000a = DB(WorkUnrelated(
    2000, "Software  Engineering",
    display="wang",
    authors="Wang,  Y.X.,  King,  G.",
    place=FAKE,
    other1="CRC Press LLC",
    placex="Processes-  Principles  and  Applications",
))

wang2000b = DB(WorkUnrelated(
    2000, "Software  Engineering  Processes-Principles  and  Applications,",
    display="wang b",
    authors="Y.X. Wang,  G.  King,",
    place=FAKE,
    placex="2000,  CRC Press LLC",
))

wimmer2000a = DB(WorkUnrelated(
    2000, "Report for the activities within the RENOIR exchange programme",
    display="wimmer",
    authors="Wimmer, Maria A",
    place=FAKE,
    entrytype="article",
    ID="wimmerreport",
    gs2016="1",
    placex="Requirements Engineering Network Of International cooperating Research groups",
))
