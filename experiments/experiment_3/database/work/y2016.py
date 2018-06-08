# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

clarke2016a = DB(WorkUnrelated(
    2016, "Software Process Improvement and Capability Determination",
    display="clarke",
    authors="Clarke, Paul M and O'Connor, Rory V and Rout, Terry and Dorling, Alec",
    place=Book,
    entrytype="book",
    publisher="Springer",
    ID="clarke2016software",
    gs2016="1",
    placex="",
))

clarke2016b = DB(WorkUnrelated(
    2016, "An investigation of software development process terminology",
    display="clarke b",
    authors="Clarke, Paul and Mesquida, Antoni-Lluís and Ekert, Damjan and Ekstrom, Joseph J and Gornostaja, Tatjana and Jovanovic, Milos and Johansen, Jørn and Mas, Antonia and Messnarz, Richard and Villar, Blanca Nájera and others",
    place=ICSPICD,
    pp="351--361",
    entrytype="inproceedings",
    organization="Springer",
    ID="clarke2016investigation",
    cluster_id="16844510422058803457",
    scholar="http://scholar.google.com/scholar?cites=16844510422058803457&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="International Conference on Software Process Improvement and Capability Determination",
))

colomo2016a = DB(WorkUnrelated(
    2016, "Towards Supporting International Standard-Based Software Engineering Approaches Using Semantic Web Technologies: A Systematic Literature Review",
    display="colomo",
    authors="Colomo-Palacios, Ricardo and Colombo-Mendoza, Luis Omar and Valencia-García, Rafael",
    place=FAKE,
    pp="169--183",
    entrytype="inproceedings",
    organization="Springer",
    ID="colomo2016towards",
    gs2016="1",
    placex="International Conference on Technologies and Innovation",
))

kabaale2016a = DB(WorkSnowball(
    2016, "Representing Software Process in Description Logics: n Ontology pproach for Software Process Reasoning and Verification",
    display="kabaale",
    authors="Kabaale, Edward and Wen, Lian and Wang, Zhe and Rout, Terry",
    place=ICSPICD,
    pp="362--376",
    entrytype="inproceedings",
    organization="Springer",
    ID="kabaale2016representing",
    cluster_id="16480715056040252890",
    scholar="http://scholar.google.com/scholar?cites=16480715056040252890&as_sdt=2005&sciodt=0,5&hl=en",
    seed_set="1",
    selected_order="9",
    final_selected="1",
    gs2016="1",
    placex="International Conference on Software Process Improvement and Capability Determination",
))

kreiner2016a = DB(WorkUnrelated(
    2016, "Systems, Software and Services Process Improvement",
    display="kreiner",
    authors="Kreiner, Christian and O'Connor, Rory V and Poth, Alexander and Messnarz, Richard",
    place=Book,
    entrytype="book",
    publisher="Springer",
    ID="kreiner2016systems",
    gs2016="1",
    placex="",
))

mejia2016a = DB(WorkUnrelated(
    2016, "Reinforcing the applicability of multi-model environments for software process improvement using knowledge management",
    display="mejia",
    authors="Mejia, Jezreel and Muñoz, Edrisi and Muñoz, Mirna",
    place=SCP,
    pp="3--15",
    entrytype="article",
    volume="121",
    publisher="Elsevier",
    ID="mejia2016reinforcing",
    cluster_id="3373933946626951801",
    scholar="http://scholar.google.com/scholar?cites=3373933946626951801&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="Science of Computer Programming",
))

pícha2016a = DB(WorkUnrelated(
    2016, "Alm tool data usage in software process metamodeling",
    display="pícha",
    authors="Pícha, Petr and Brada, Premek",
    place=SEAA,
    pp="1--8",
    entrytype="inproceedings",
    organization="IEEE",
    ID="picha2016alm",
    gs2016="1",
    placex="Software Engineering and Advanced Applications (SEAA), 2016 42th Euromicro Conference on",
))

stojanov2016a = DB(WorkUnrelated(
    2016, "Exploring software maintenance process characteristics by using inductive thematic analysis",
    display="stojanov",
    authors="Stojanov, Zeljko and Stojanov, Jelena",
    place=FAKE,
    entrytype="article",
    ID="stojanov2016exploring",
    gs2016="1",
    placex="International conference on Applied Internet and Information Technologies - AIIT 2016",
))
