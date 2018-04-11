# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

shewhart1939a = DB(WorkUnrelated(
    1939, "Statistical method from the viewpoint of quality control.",
    display="shewhart",
    authors="WA Shewhart",
    place=FAKE,
    placex="The Graduate School of the Department of Agriculture, Washington, DC. Reprinted by Dover Publications in the Dover Books on Mathematics series in 1986",
))
