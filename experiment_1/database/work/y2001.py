# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

bacon2001a = DB(WorkUnrelated(
    2001, "A Systemic Framework for the Field of Information Systems",
    display="bacon",
    authors="Bacon, C. James and Fitzgerald, Brian",
    place=FAKE,
    pp="46--67",
    entrytype="article",
    issue_date="Spring 2001",
    volume="32",
    number="2",
    month="apr",
    issn="0095-0033",
    ID="Bacon:2001:SFF:506732.506738",
    acm="1",
    placex="SIGMIS Database",
))

counsell2001a = DB(WorkUnrelated(
    2001, "An Evolutionary Approach to Digital Recording and Information About Heritage Sites",
    display="counsell",
    authors="Counsell, John",
    place=FAKE,
    pp="33--42",
    entrytype="inproceedings",
    series="VAST '01",
    isbn="1-58113-447-9",
    location="Glyfada, Greece",
    ID="Counsell:2001:EAD:584993.584999",
    acm="1",
    placex="Proceedings of the 2001 Conference on Virtual Reality, Archeology, and Cultural Heritage",
))

smart2001a = DB(WorkUnrelated(
    2001, "Creating Effective and Enjoyable Documentation: Enhancing the Experience of Users by Aligning Information with Strategic Direction and Customer Insights",
    display="smart",
    authors="Smart, Karl and Norton, Dave",
    place=FAKE,
    pp="220--220",
    entrytype="inproceedings",
    series="SIGDOC '01",
    isbn="1-58113-295-6",
    location="Sante Fe, New Mexico, USA",
    ID="Smart:2001:CEE:501516.501559",
    acm="1",
    placex="Proceedings of the 19th Annual International Conference on Computer Documentation",
))

waina2001a = DB(WorkSnowball(
    2001, "A business goal-based approach to achieving systems engineering capability maturity",
    display="waina",
    authors="R. B. Waina",
    place=DASC,
    pp="4B2/1-4B2/13 vol.1",
    entrytype="inproceedings",
    volume="1",
    number="",
    keyword="business data processing",
    doi="10.1109/DASC.2001.963369",
    issn="",
    ID="963369",
))
