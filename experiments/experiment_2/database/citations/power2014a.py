# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import cohn2009a
from ..work.y2011 import power2011a
from ..work.y2012 import rubin2012a
from ..work.y2012 import sutherland2012a
from ..work.y2014 import power2014a
from ..work.y2015 import pilcher2015a

DB(Citation(
    power2014a, power2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    power2014a, rubin2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    power2014a, pilcher2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    power2014a, cohn2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    power2014a, sutherland2012a, ref="",
    contexts=[

    ],
))
