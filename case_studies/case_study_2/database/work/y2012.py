# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

jalali2012a = DB(WorkOk(
    2012, "Systematic literature studies: Database searches vs. backward snowballing",
    display="jalali",
    authors="Jalali, S. and Wohlin, C.",
    place=ESEM,
    other1="29-38",
))

jalali2012b = DB(WorkOk(
    2012, "Global software engineering and agile practices: A systematic review",
    display="jalali2012b",
    authors="Jalali, S. and Wohlin, C.",
    place=JSEP,
    other1="24, 6, 643-659.",
))

smite2012a = DB(WorkOk(
    2012, "An empirically based terminology and taxonomy for global software engineering",
    display="smite",
    authors="Smite, D., Wohlin, C., Galvina, Z. and Prikladnicki, R.",
    place=ESE,
    other1="19, 1, 105-153",
))
