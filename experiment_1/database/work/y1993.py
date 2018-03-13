# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

cederling1993a = DB(WorkUnrelated(
    1993, "Industrial software development --- a case study",
    display="cederling",
    authors="Cederling, Ulf",
    place=FAKE,
    pp="226--237",
    entrytype="inproceedings",
    editor="Sommerville, Ian and Paul, Manfred",
    publisher="Springer Berlin Heidelberg",
    address="Berlin, Heidelberg",
    ID="10.1007/3-540-57209-0_16",
    springer="1",
    placex="Software Engineering --- ESEC '93",
))

curtis1993a = DB(WorkUnrelated(
    1993, "Creating a software process improvement program",
    display="curtis",
    authors="B Curtis and M Paulk",
    place=IST,
    pp="381 - 386",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90009-R",
    link="https://www.sciencedirect.com/science/article/pii/095058499390009R",
    keyword="capability maturity model",
    ID="Curtis1993381",
    sciencedirect="1",
    placex="Information and Software Technology",
))

lott1993a = DB(WorkUnrelated(
    1993, "Measurement-based guidance of software projects using explicit project plans",
    display="lott",
    authors="CM Lott and HD Rombach",
    place=IST,
    pp="407 - 419",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90012-R",
    link="https://www.sciencedirect.com/science/article/pii/095058499390012R",
    keyword="project guidance",
    ID="Lott1993407",
    sciencedirect="1",
    placex="Information and Software Technology",
))

paulk1993a = DB(WorkUnrelated(
    1993, "Capability Maturity Model for Software, Version 1.1",
    display="paulk",
    authors="Paulk, M, Curtis, B, Chrissis, M, Weber, C. V,",
    place=EBSE,
    entrytype="article",
    ID="Paulk1993",
))

thompson1993a = DB(WorkUnrelated(
    1993, "Software process maturity (SPM) and the information systems developer",
    display="thompson",
    authors="K Thompson and P McParland",
    place=IST,
    pp="331 - 338",
    entrytype="article",
    volume="35",
    number="67",
    note="Software Process Modelling in Practice",
    issn="0950-5849",
    doi="https://doi.org/10.1016/0950-5849(93)90003-L",
    link="https://www.sciencedirect.com/science/article/pii/095058499390003L",
    keyword="software quality",
    ID="Thompson1993331",
    sciencedirect="1",
    placex="Information and Software Technology",
))
