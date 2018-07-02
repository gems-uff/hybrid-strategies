# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import krutchen2000a
from ..work.y2002 import cockburn2002a
from ..work.y2002 import wirfs2002a
from ..work.y2002 import larman2002a
from ..work.y2004 import beck2004a
from ..work.y2005 import poger2005a
from ..work.y2005 import mitra2005a
from ..work.y2006 import werner2006a
from ..work.y2006 import bullinger2006a
from ..work.y2007 import mitra2007a

DB(Citation(
    mitra2007a, poger2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, werner2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, krutchen2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, cockburn2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, beck2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, bullinger2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, mitra2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, wirfs2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitra2007a, larman2002a, ref="",
    contexts=[

    ],
))
