# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import basili1984a
from ..work.y1992 import kaplan1992a
from ..work.y1994 import basili1994a
from ..work.y2002 import ogc2002a
from ..work.y2002 import psmsc2002a
from ..work.y2003 import chrissis2003a
from ..work.y2007 import basili2007b
from ..work.y2008 import isaca2008b

DB(Citation(
    basili2007b, basili1984a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, basili1994a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, chrissis2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, ogc2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, isaca2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, kaplan1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2007b, psmsc2002a, ref="",
    contexts=[

    ],
))
