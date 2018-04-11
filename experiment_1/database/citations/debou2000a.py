# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import basili1988b
from ..work.y1993 import paulk1993a
from ..work.y1993 import paulk1993e
from ..work.y1994 import mcgarry1994a
from ..work.y1995 import debou1995a
from ..work.y1995 import pulford1995a
from ..work.y1996 import mcfeeley1996c
from ..work.y1997 import spice1997a
from ..work.y2000 import debou2000a

DB(Citation(
    debou2000a, basili1988b, ref="[1]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, debou1995a, ref="[2]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, mcfeeley1996c, ref="[3]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, mcgarry1994a, ref="[4]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, paulk1993a, ref="[5]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, paulk1993e, ref="[6]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, pulford1995a, ref="[7]",
    contexts=[

    ],
))

DB(Citation(
    debou2000a, spice1997a, ref="[8]",
    contexts=[

    ],
))
