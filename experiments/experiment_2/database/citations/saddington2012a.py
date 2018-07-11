# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import saddington2012a
from ..work.y2012 import myai2012a
from ..work.y2014 import haaster2014a
from ..work.y2015 import vlietland2015b
from ..work.y2015 import haaster2015a
from ..work.y2018 import kalenda2018a

DB(Citation(
    haaster2014a, saddington2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015b, saddington2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kalenda2018a, saddington2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haaster2015a, saddington2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    saddington2012a, myai2012a, ref="1.",
    contexts=[

    ],
))
