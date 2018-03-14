# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1992 import basili1992a
from ..work.y1992 import kaplan1992a
from ..work.y1999 import becker1999a
from ..work.y2002 import ogc2002a
from ..work.y2005 import isaca2005a
from ..work.y2007 import kathuria2007a
from ..work.y2007 import basili2007b
from ..work.y2008 import isaca2008a
from ..work.y2009 import basili2009a
from ..work.y2010 import kowalczyk2010a
from ..work.y2011 import kaneko2011a
from ..work.y2012 import jaxa2012a

DB(Citation(
    kaneko2011a, kathuria2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, basili2007b, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, basili2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, basili1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, kowalczyk2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, isaca2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, isaca2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, ogc2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, kaplan1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, becker1999a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kaneko2011a, jaxa2012a, ref="",
    contexts=[

    ],
))
