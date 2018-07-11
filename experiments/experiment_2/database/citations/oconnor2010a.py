# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import oconnor2010a
from ..work.y2011 import oconnor2011a
from ..work.y2014 import mai2014a
from ..work.y2015 import pitkänen2015a
from ..work.y2017 import abidin2017a

DB(Citation(
    oconnor2011a, oconnor2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    abidin2017a, oconnor2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pitkänen2015a, oconnor2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mai2014a, oconnor2010a, ref="",
    contexts=[

    ],
))
