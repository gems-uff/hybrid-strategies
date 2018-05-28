# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1993 import blackerby1993a
from ..work.y1996 import dod1996a
from ..work.y1998 import mccoy1998a
from ..work.y1998 import madni1998a
from ..work.y1998 import dynsys1998a
from ..work.y1998 import kapp1998a

DB(Citation(
    mccoy1998a, dod1996a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccoy1998a, blackerby1993a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccoy1998a, madni1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccoy1998a, dynsys1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccoy1998a, kapp1998a, ref="",
    contexts=[

    ],
))
