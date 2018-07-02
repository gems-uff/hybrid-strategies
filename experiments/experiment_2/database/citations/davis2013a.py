# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1981 import boehm1981a
from ..work.y2000 import rothman2000a
from ..work.y2011 import jones2011a
from ..work.y2012 import one2012a
from ..work.y2013 import davis2013a

from ..work.y2013 import humphrey2013a
from ..work.y2013 import scrum2013a
from ..work.y2013 import agile2013a
from ..work.y2013 import davis2013b

DB(Citation(
    davis2013a, humphrey2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, jones2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, boehm1981a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, rothman2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, one2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, scrum2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, agile2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2013a, davis2013b, ref="",
    contexts=[

    ],
))
