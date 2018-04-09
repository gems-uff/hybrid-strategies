# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import solingen2002a
from ..work.y2003 import isoiec2003b
from ..work.y2004 import accenture2004a
from ..work.y2007 import orlov2007a
from ..work.y2007 import gartner2007a
from ..work.y2010 import basili2010a
from ..work.y2011 import trendowicz2011a
from ..work.y2011 import kowalczyk2011a

DB(Citation(
    trendowicz2011a, accenture2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, orlov2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, gartner2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, solingen2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, isoiec2003b, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, kowalczyk2011a, ref="",
    contexts=[

    ],
))
