# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import wang2000b
from ..work.y2001 import lopez2001a
from ..work.y2001 import berners2001a
from ..work.y2001 import w32001a
from ..work.y2001 import w32001b
from ..work.y2002 import conradi2002a
from ..work.y2003 import miller2003a
from ..work.y2004 import w3c2004a
from ..work.y2004 import liao2004b
from ..work.y2005 import liao2005b
from ..work.y2017 import tarhan2017a

DB(Citation(
    liao2005b, conradi2002a, ref="[1]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, lopez2001a, ref="[2]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, wang2000b, ref="[3]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, berners2001a, ref="[4]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, w3c2004a, ref="[5]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, Site("Jena,", "http://sourceforge.net/projects/jena/"), ref="[6]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, Site("Sesame,", "http://sesame.aidministrator.nl/"), ref="[7]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, w32001a, ref="[8]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, w32001b, ref="[9]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, miller2003a, ref="[10]",
    contexts=[

    ],
))

DB(Citation(
    liao2005b, liao2004b, ref="[11]",
    contexts=[

    ],
))

DB(Citation(
    tarhan2017a, liao2005b, ref="",
    contexts=[

    ],
))
