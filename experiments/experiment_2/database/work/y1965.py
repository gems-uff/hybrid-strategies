# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

wiener1965a = DB(WorkUnrelated(
    1965, "Cybernetics-: or the Control and Communication in the Animal andthe Machine",
    display="wiener",
    authors="N. Wiener",
    place=FAKE,
    entrytype="conference",
    ID="Wiener1965",
    placex="MIT Press",
))
