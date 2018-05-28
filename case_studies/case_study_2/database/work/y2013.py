# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

wohlin2013a = DB(WorkOk(
    2013, "Systematic literature reviews in software engineering",
    display="wohlin",
    authors="Wohlin C. and Prikladnicki R.",
    place=IST,
    other1="55, 6, 919-920",
))

wohlin2013b = DB(WorkOk(
    2013, "On the reliability of mapping studies in software engineering",
    display="wohlin2013b",
    authors="Wohlin, C., Runeson, P., da Mota Silveira Neto, P. A., Engstrom, E., do Carmo Machado, I. and de Almeida, E. S.",
    place=JSS,
    other1="86, 10, 25942610",
))
