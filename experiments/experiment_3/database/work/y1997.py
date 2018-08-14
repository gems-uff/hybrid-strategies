# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

dorfmann1997a = DB(WorkUnrelated(
    1997, "Software System Engineering: An Engineering Process",
    display="dorfmann",
    authors="R.H. Thayer R.H. Thayer M. Dorfmann",
    place=FAKE,
    placex="in Software Requirements Engineering Los Alamitos CA:IEEE Press",
))

ericson1997a = DB(WorkUnrelated(
    1997, "TIM-A Test Improvement Model",
    display="Ursing",
    authors="Ericson T. Subotic A. Ursing S.",
    place=FAKE,
    placex="Software Testing Verification and Reliability 7(4) 1997 pp. 229-246",
))

hellens1997a = DB(WorkUnrelated(
    1997, "Information systems quality versus software quality a discussion from a managerial, an organisational and an engineering viewpoint",
    display="hellens",
    authors="Von Hellens, LA",
    place=IST,
    pp="801--808",
    entrytype="article",
    volume="39",
    number="12",
    publisher="Elsevier",
    ID="von1997information",
    googlescholar2016="1",
    planilha_googlescholar2016="1",
    placex="Information and Software Technology",
    sciencedirect2016="1",
    planilha_sciencedirect2016="1",
))

panfilis1997a = DB(WorkUnrelated(
    1997, "Experiences introducing a measurement program",
    display="panfilis",
    authors="De Panfilis, Stefano and Kitchenham, Barbara and Morfuni, N",
    place=IST,
    pp="745--754",
    entrytype="article",
    volume="39",
    number="11",
    publisher="Elsevier",
    ID="de1997experiences",
    googlescholar2016="1",
    planilha_googlescholar2016="1",
    placex="Information and Software Technology",
))
