# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1959 import goffman1959a
from ..work.y1965 import wiener1965a
from ..work.y1967 import glaser1967a
from ..work.y1981 import yin1981a
from ..work.y1984 import huberman1984a
from ..work.y1986 import takeuchi1986a
from ..work.y1987 import wegner1987a
from ..work.y1989 import eisenhardt1989a
from ..work.y1990 import locke1990a
from ..work.y1990 import malone1990a
from ..work.y1992 import eisenhardt1992a
from ..work.y1993 import desanctis1993a
from ..work.y1994 import bazerman1994a
from ..work.y1995 import calvert1995a
from ..work.y1995 import galbraith1995a
from ..work.y1995 import henneman1995a
from ..work.y1995 import sandelowski1995a
from ..work.y1996 import harland1996a
from ..work.y1996 import marshall1996a
from ..work.y1997 import mentzer1997a
from ..work.y2000 import mathieu2000a
from ..work.y2000 import rising2000a
from ..work.y2001 import beck2001b
from ..work.y2001 import knight2001a
from ..work.y2001 import mentzer2001a
from ..work.y2003 import boonstra2003a
from ..work.y2003 import saunders2003a
from ..work.y2004 import schwaber2004a
from ..work.y2005 import ågerfalk2005a
from ..work.y2005 import brown2005a
from ..work.y2005 import sahin2005a
from ..work.y2005 import sutherland2005a
from ..work.y2006 import andrei2006a
from ..work.y2006 import cockburn2006a
from ..work.y2007 import baltacioglu2007a
from ..work.y2007 import leffingwell2007a
from ..work.y2007 import myers2007a
from ..work.y2007 import schwaber2007b
from ..work.y2007 import sutherland2007a
from ..work.y2008 import dul2008a
from ..work.y2008 import hildenbrand2008a
from ..work.y2008 import kim2008a
from ..work.y2008 import moe2008a
from ..work.y2008 import sharp2008a
from ..work.y2008 import sutherland2008a
from ..work.y2009 import begel2009a
from ..work.y2009 import garg2009a
from ..work.y2009 import lehto2009a
from ..work.y2009 import petersen2009a
from ..work.y2009 import port2009a
from ..work.y2009 import saldana2009a
from ..work.y2009 import talby2009a
from ..work.y2009 import yin2009a
from ..work.y2010 import batra2010a
from ..work.y2010 import candea2010a
from ..work.y2010 import freudenberg2010a
from ..work.y2010 import gibbert2010a
from ..work.y2010 import green2010a
from ..work.y2010 import humble2010a
from ..work.y2010 import lee2010a
from ..work.y2010 import sharp2010a
from ..work.y2010 import wei2010a
from ..work.y2010 import woodward2010a
from ..work.y2011 import birks2011a
from ..work.y2011 import datta2011a
from ..work.y2011 import gregory2011a
from ..work.y2011 import jonker2011a
from ..work.y2011 import jyothi2011a
from ..work.y2011 import lewis2011a
from ..work.y2011 import mishra2011a
from ..work.y2011 import oppenheim2011b
from ..work.y2011 import rautiainen2011a
from ..work.y2011 import schnitter2011a
from ..work.y2012 import ambler2012a
from ..work.y2012 import bannerman2012a
from ..work.y2012 import dorairaj2012a
from ..work.y2012 import jalali2012a
from ..work.y2012 import kniberg2012a
from ..work.y2012 import olsson2012a
from ..work.y2012 import paasivaara2012a
from ..work.y2012 import saddington2012a
from ..work.y2012 import soundararajan2012a
from ..work.y2012 import strode2012a
from ..work.y2012 import waardenburg2012a
from ..work.y2013 import brown2013a
from ..work.y2013 import dingyr2013a
from ..work.y2013 import dingsøyr2013a
from ..work.y2013 import feitelson2013a
from ..work.y2013 import hardion2013a
from ..work.y2013 import kruchten2013a
from ..work.y2013 import larman2013a
from ..work.y2013 import muşlu2013a
from ..work.y2013 import vlietland2013a
from ..work.y2014 import dove2014a
from ..work.y2014 import fitzgerald2014b
from ..work.y2014 import scheerer2014a
from ..work.y2014 import ståhl2014b
from ..work.y2014 import vlietland2014a
from ..work.y2014 import vlietland2014b
from ..work.y2014 import pages2014a
from ..work.y2015 import vlietland2015a
from ..work.y2015 import krimpmann2015a
from ..work.y2015 import almutairi2015a
from ..work.y2015 import jigeesh2015a
from ..work.y2015 import stettina2015b
from ..work.y2015 import mansouri2015a
from ..work.y2015 import krimpmann2015b
from ..work.y2015 import vlietland2015b
from ..work.y2015 import andreassen2015a
from ..work.y2015 import jr2015a
from ..work.y2015 import sousa2015a
from ..work.y2016 import bass2016a
from ..work.y2016 import batra2016a
from ..work.y2016 import aintila2016a
from ..work.y2016 import bonassa2016a
from ..work.y2016 import haaster2016a
from ..work.y2016 import syversen2016a
from ..work.y2017 import moe2017a
from ..work.y2017 import sensuse2017a
from ..work.y2017 import aamir2017a
from ..work.y2017 import patel2017a
from ..work.y2017 import oomen2017a
from ..work.y2017 import noll2017a
from ..work.y2017 import musa2017a
from ..work.y2017 import arango2017a
from ..work.y2018 import dingsøyr2018a
from ..work.y2018 import dingsøyr2018b
from ..work.y2018 import bjørnson2018a
from ..work.y2018 import imani2018a

DB(Citation(
    vlietland2015a, ågerfalk2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, ambler2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, andrei2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, baltacioglu2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, bannerman2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, batra2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, bazerman1994a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, beck2001b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, begel2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, birks2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, boonstra2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, brown2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, brown2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, calvert1995a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, candea2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, cockburn2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, datta2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, desanctis1993a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, dingyr2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, dingsøyr2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, dorairaj2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, dove2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, dul2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, eisenhardt1989a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, eisenhardt1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, feitelson2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, fitzgerald2014b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, freudenberg2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, galbraith1995a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, garg2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, gibbert2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, glaser1967a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, goffman1959a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, green2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, gregory2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, hardion2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, harland1996a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, henneman1995a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, hildenbrand2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, huberman1984a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, humble2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, jalali2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, jonker2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, jyothi2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, kim2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, kniberg2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, knight2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, kruchten2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, larman2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, lee2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, leffingwell2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, lehto2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, lewis2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, locke1990a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, malone1990a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, marshall1996a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, mathieu2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, mentzer2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, mentzer1997a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, mishra2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, moe2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, muşlu2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, myers2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, olsson2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, oppenheim2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, paasivaara2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, petersen2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, port2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, rautiainen2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, rising2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, saddington2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sahin2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, saldana2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sandelowski1995a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, saunders2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, scheerer2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, schnitter2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, schwaber2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, schwaber2007b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sharp2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sharp2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, soundararajan2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, ståhl2014b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, strode2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sutherland2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sutherland2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, sutherland2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, talby2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, takeuchi1986a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, vlietland2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, vlietland2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, vlietland2014b, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, waardenburg2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, wegner1987a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, wei2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, wiener1965a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, woodward2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, yin1981a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, yin2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dingsøyr2018a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    krimpmann2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    batra2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moe2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    almutairi2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dingsøyr2018b, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jigeesh2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stettina2015b, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    aintila2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bjørnson2018a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sensuse2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    imani2018a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    aamir2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mansouri2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    patel2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pages2014a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bonassa2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    krimpmann2015b, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haaster2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oomen2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015b, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    noll2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    syversen2016a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    musa2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    andreassen2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    arango2017a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jr2015a, vlietland2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sousa2015a, vlietland2015a, ref="",
    contexts=[

    ],
))
