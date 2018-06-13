# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

ambriola2003a = DB(WorkUnrelated(
    2003, "A Framework for Comparing Software Processes off the Shelf (SPOTS)",
    display="ambriola",
    authors="Ambriola, Vincenzo and Cignoni, Giovanni A and Conradi, Reidar and Jaccheri, Letizia",
    place=FAKE,
    entrytype="article",
    ID="ambriola2003framework",
    gs2016="1",
    placex="article",
))

dolado2003a = DB(WorkUnrelated(
    2003, "TIC2001-1143-C03",
    display="dolado",
    authors="Dolado, José Javier and Riquelme, José and Tuya, Javier",
    place=FAKE,
    entrytype="article",
    ID="doladotic2001",
    gs2016="1",
    placex="Jornada de Seguimiento de Proyectos en Tecnologıas Informaticas, Programa Nacional de Tecnologıas de la Informacion y las Comunicaciones",
))

edwards2003a = DB(WorkUnrelated(
    2003, "Managing software engineers and their knowledge",
    display="edwards",
    authors="Edwards, John S",
    place=FAKE,
    pp="5--27",
    entrytype="incollection",
    publisher="Springer",
    ID="edwards2003managing",
    springer2016="1",
    placex="Managing software engineering knowledge",
))

hayes2003a = DB(WorkUnrelated(
    2003, "Observe-mine-adopt (OMA): an agile way to enhance software maintainability",
    display="hayes",
    authors="Huffman Hayes, Jane and Mohamed, Naresh and Gao, Tina Hong",
    place=JSEP,
    pp="297--323",
    entrytype="article",
    volume="15",
    number="5",
    publisher="Wiley Online Library",
    ID="huffman2003observe",
    gs2016="1",
    placex="Journal of Software: Evolution and Process",
    wiley2016="1",
))

ruiz2003a = DB(WorkUnrelated(
    2003, "Environment for Managing Software Maintenance Projects",
    display="ruiz",
    authors="Ruiz, Francisco and Garcia, Felix and Piattini, Mario and Polo, Macario",
    place=FAKE,
    pp="255--291",
    entrytype="incollection",
    publisher="IGI Global",
    ID="ruiz2003environment",
    gs2016="1",
    placex="Advances in software maintenance management: technologies and solutions",
))
