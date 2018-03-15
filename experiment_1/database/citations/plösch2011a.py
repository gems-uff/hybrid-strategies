# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1931 import shewhart1931a
from ..work.y1993 import dion1993a
from ..work.y1996 import mcfeeley1996a
from ..work.y1998 import isoiec1998d
from ..work.y2002 import simon2002a
from ..work.y2003 import isoiec2003b
from ..work.y2003 import venzin2003a
from ..work.y2006 import cmmi2006a
from ..work.y2011 import plösch2011a

DB(Citation(
    plösch2011a, isoiec2003b, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, cmmi2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, shewhart1931a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, dion1993a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, mcfeeley1996a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, isoiec1998d, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, simon2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plösch2011a, venzin2003a, ref="",
    contexts=[

    ],
))
