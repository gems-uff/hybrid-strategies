# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import cmmi2002ab
from ..work.y2004 import w3c2004c
from ..work.y2004 import mendes2004a
from ..work.y2005 import carnegie2005a
from ..work.y2005 import liao2005a
from ..work.y2006 import soydan2006a
from ..work.y2006 import carnegie2006a

DB(Citation(
    soydan2006a, cmmi2002ab, ref="1.",
    contexts=[

    ],
))

DB(Citation(
    soydan2006a, w3c2004c, ref="2.",
    contexts=[

    ],
))

DB(Citation(
    soydan2006a, carnegie2005a, ref="3.",
    contexts=[

    ],
))

DB(Citation(
    soydan2006a, carnegie2006a, ref="4.",
    contexts=[

    ],
))

DB(Citation(
    soydan2006a, mendes2004a, ref="5.",
    contexts=[

    ],
))

DB(Citation(
    soydan2006a, liao2005a, ref="6.",
    contexts=[

    ],
))
