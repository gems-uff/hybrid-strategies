# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import basili1984a
from ..work.y1992 import kaplan1992b
from ..work.y1994 import basili1994d
from ..work.y2002 import basili2002a
from ..work.y2007 import kathuria2007a
from ..work.y2007 import basili2007b
from ..work.y2007 import basili2007c
from ..work.y2009 import basili2009a
from ..work.y2010 import kowalczyk2010a
from ..work.y2012 import heidrich2012b
from ..work.y2013 import kowalczyk2013a
from ..work.y2016 import chagas2016a

DB(Citation(
    kowalczyk2010a, basili1984a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, kathuria2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, basili2007b, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, basili2007c, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, basili2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, basili1994d, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, kaplan1992b, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2010a, basili2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kowalczyk2013a, kowalczyk2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heidrich2012b, kowalczyk2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chagas2016a, kowalczyk2010a, ref="",
    contexts=[

    ],
))
