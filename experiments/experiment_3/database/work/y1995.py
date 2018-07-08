# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

alonso1995a = DB(WorkUnrelated(
    1995, "IDERS: an integrated environment for the development of hard real-time systems",
    display="alonso",
    authors="Alonso, A., Christensen, H., Baresi, L., Heikkinen, M.",
    place=FAKE,
    other1="Proceedings of Seventh Euromicro Workshop",
    placex="Real-Time Systems",
))

humphrey1995a = DB(WorkUnrelated(
    1995, "A Discipline for Software Engineering",
    display="humphrey",
    authors="W. S. Humphrey",
    place=FAKE,
    placex="Addison-Wesley Longman Publishing Co. Inc",
))

musen1995a = DB(WorkUnrelated(
    1995, "Ontology-based Configuration of Problem-solving Methods and Generation of Knowledge-acquisition Tools: Application of Protégé-II to Protocol-based Decision Support",
    display="musen",
    authors="S. W. Tu H. Eriksson J. H. Gennari Y. Shahar M. A. Musen",
    place=FAKE,
    other1="vol. 7 no. 3",
    other2="pp. 257-289 June",
    placex="Artificial Intelligence in Medicine",
))
