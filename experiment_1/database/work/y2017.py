# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

li2017a = DB(WorkUnrelated(
    2017, "A Comparative Study of Value in Agile Software Development Organizations",
    display="li",
    authors="Li, Xian and Cao, Qian",
    place=FAKE,
    entrytype="misc",
    ID="li2017comparative",
    placex="",
))

mandić2017a = DB(WorkUnrelated(
    2017, "An extension of the GQM+ Strategies approach with formal causal reasoning",
    display="mandić",
    authors="Mandi{c?}, Vladimir and Gvozdenovi{c?}, Neboj{}a",
    place=IST,
    pp="127--147",
    entrytype="article",
    volume="88",
    publisher="Elsevier",
    ID="mandic2017extension",
    cluster_id="10059951970390866765",
    scholar="http://scholar.google.com/scholar?cites=10059951970390866765&as_sdt=2005&sciodt=0,5&hl=en",
    placex="Information and Software Technology",
))

mughal2017a = DB(WorkUnrelated(
    2017, "A Framework for Implementing Software Measurement Programs in Small and Medium Enterprises",
    display="mughal",
    authors="Mughal, Aftab Ahmad",
    place=Thesis,
    entrytype="phdthesis",
    ID="mughal2017framework",
    local="University of Otago",
    placex="",
))

trinkenreich2017a = DB(WorkUnrelated(
    2017, "A Method To Select Goals, Indicators and Strategies for IT Services",
    display="trinkenreich",
    authors="Trinkenreich, Bianca and Santos, Gleison and Barcellos, Monalessa Perini",
    place=FAKE,
    entrytype="article",
    volume="10",
    number="1",
    ID="trinkenreich2017method",
    cluster_id="9788662361037217502",
    scholar="http://scholar.google.com/scholar?cites=9788662361037217502&as_sdt=2005&sciodt=0,5&hl=en",
    placex="RelaTe-DIA",
))

trinkenreich2017b = DB(WorkUnrelated(
    2017, "Eliciting Strategies for the GQM+ Strategies Approach in IT Service Measurement Initiatives",
    display="trinkenreich b",
    authors="Trinkenreich, Bianca and Santos, Gleison and Barcellos, Monalessa Perini and Conte, Tayana",
    place=ESEM,
    pp="374--383",
    entrytype="inproceedings",
    organization="IEEE",
    ID="trinkenreich2017eliciting",
    placex="2017 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)",
))
