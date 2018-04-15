# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1993 import basili1993a
from ..work.y1994 import basili1994a
from ..work.y1998 import brandon1998a
from ..work.y2003 import boehm2003a
from ..work.y2003 import boehm2003b
from ..work.y2004 import erdogmus2004a
from ..work.y2010 import mandić2010a
from ..work.y2010 import basili2010a
from ..work.y2010 import mandić2010b
from ..work.y2013 import garay2013a
from ..work.y2014 import basili2014b
from ..work.y2014 import basili2014a
from ..work.y2014 import basili2014c
from ..work.y2015 import valente2015a
from ..work.y2015 import valente2015b
from ..work.y2016 import lópez2016a

DB(Citation(
    mandić2010a, erdogmus2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, brandon1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, boehm2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, boehm2003b, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, basili1993a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, basili1994a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010a, mandić2010b, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2014b, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    valente2015a, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    garay2013a, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lópez2016a, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2014a, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2014c, mandić2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    valente2015b, mandić2010a, ref="",
    contexts=[

    ],
))
