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
