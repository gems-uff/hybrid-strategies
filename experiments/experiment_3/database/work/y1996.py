# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

chen1996a = DB(WorkUnrelated(
    1996, "Toward Intelligent Meeting Agents",
    display="Chen",
    authors="Hsinchun Chen, Andrea Houston , Jay Nunamaker , Jerome Yen,",
    place=FAKE,
    placex="Computer",
))

doheny1996a = DB(WorkUnrelated(
    1996, "A Framework and Tool for Modelling and Assessing Software Development Processes",
    display="doheny",
    authors="Doheny, Jim and Filby, IM",
    place=FAKE,
    entrytype="article",
    publisher="THE UNIVERSITY OF EDINBURGH",
    ID="doheny1996aframework",
    cluster_id="16164347461171448111",
    scholar="http://scholar.google.com/scholar?cites=16164347461171448111&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="TECHNICAL REPORT-UNIVERSITY OF EDINBURGH ARTIFICIAL INTELLIGENCE APPLICATIONS INSTITUTE AIAI TR",
    other1="Wilmslow, May",
))

doheny1996b = DB(WorkUnrelated(
    1996, "A framework for modelling software development processes",
    display="doheny b",
    authors="Doheny, JG and Filby, IM",
    place=FAKE,
    entrytype="article",
    publisher="THE UNIVERSITY OF EDINBURGH",
    ID="doheny1996bframework",
    cluster_id="2184567551688903067",
    scholar="http://scholar.google.com/scholar?cites=2184567551688903067&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="TECHNICAL REPORT-UNIVERSITY OF EDINBURGH ARTIFICIAL INTELLIGENCE APPLICATIONS INSTITUTE AIAI TR",
))

doheny1996c = DB(WorkUnrelated(
    1996, "Modelling Software Development Processes and Standards",
    display="doheny c",
    authors="Doheny, JG and Filby, IM",
    place=FAKE,
    entrytype="article",
    publisher="THE UNIVERSITY OF EDINBURGH",
    ID="doheny1996modelling",
    cluster_id="15606324768416123047",
    scholar="http://scholar.google.com/scholar?cites=15606324768416123047&as_sdt=2005&sciodt=0,5&hl=en",
    gs2016="1",
    placex="TECHNICAL REPORT-UNIVERSITY OF EDINBURGH ARTIFICIAL INTELLIGENCE APPLICATIONS INSTITUTE AIAI TR",
))

doheny1996d = DB(WorkUnrelated(
    1996, "The ASPEN Toolkit For Modelling And Assessing The Software Development Process",
    display="doheny d",
    authors="Doheny, JG and Filby, IM",
    place=Book,
    entrytype="book",
    publisher="Artificial Intelligence Applications Institute, University of Edinburgh",
    ID="doheny1996aspen",
    gs2016="1",
    placex="",
))

gasston1996a = DB(WorkUnrelated(
    1996, "Process improvement: an alternative to BPR for software development organizations",
    display="gasston",
    authors="Gasston, JL",
    place=SQJ,
    pp="171--183",
    entrytype="article",
    volume="5",
    number="3",
    publisher="Springer",
    ID="gasston1996process",
    gs2016="1",
    placex="Software Quality Journal",
    springer2016="1",
))
