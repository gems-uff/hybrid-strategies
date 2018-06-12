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
    2000, "A dynamic framework for classifying information systems development methodologies and approaches",
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
