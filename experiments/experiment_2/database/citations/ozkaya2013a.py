# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1998 import bass1998a
from ..work.y2007 import leffingwell2007a
from ..work.y2010 import nanette2010a
from ..work.y2011 import lapham2011a
from ..work.y2012 import grant2012a
from ..work.y2012 import bachmann2012a
from ..work.y2013 import ozkaya2013a
from ..work.y2013 import gagliardi2013a
from ..work.y2015 import japan2015a

DB(Citation(
    ozkaya2013a, grant2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ozkaya2013a, leffingwell2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ozkaya2013a, bachmann2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ozkaya2013a, nanette2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ozkaya2013a, lapham2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ozkaya2013a, bass1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gagliardi2013a, ozkaya2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    japan2015a, ozkaya2013a, ref="",
    contexts=[

    ],
))
