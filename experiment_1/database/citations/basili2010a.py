# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1992 import kaplan1992a
from ..work.y1994 import basili1994a
from ..work.y1994 import clegg1994a
from ..work.y1999 import becker1999a
from ..work.y2000 import buglione2000a
from ..work.y2000 import boehm2000a
from ..work.y2001 import bianchi2001a
from ..work.y2003 import usddusa2003a
from ..work.y2003 import card2003b
from ..work.y2007 import basili2007a
from ..work.y2010 import basili2010a
from ..work.y2010 import code2010a
from ..work.y2010 import guzmán2010a
from ..work.y2010 import sarcia2010a
from ..work.y2010 import mandić2010c
from ..work.y2010 import mandić2010d
from ..work.y2010 import hernández2010a
from ..work.y2010 import marca2010a
from ..work.y2010 import mandić2010f
from ..work.y2011 import trendowicz2011a
from ..work.y2011 import becker2011b
from ..work.y2011 import olsina2011a
from ..work.y2011 import lew2011a
from ..work.y2011 import cedergren2011a
from ..work.y2011 import olsina2011b
from ..work.y2011 import lescher2011a
from ..work.y2011 import lavazza2011a
from ..work.y2011 import cedergren2011b
from ..work.y2012 import lew2012a
from ..work.y2012 import papa2012a
from ..work.y2012 import becker2012a
from ..work.y2012 import münch2012a
from ..work.y2012 import monden2012a
from ..work.y2012 import eremenko2012a
from ..work.y2012 import leschera2012a
from ..work.y2012 import heidrich2012b
from ..work.y2012 import asghari2012a
from ..work.y2012 import papa2012b
from ..work.y2012 import machado2012a
from ..work.y2012 import olsina2012a
from ..work.y2012 import buse2012a
from ..work.y2012 import mandić2012a
from ..work.y2012 import olsina2012b
from ..work.y2012 import rombach2012a
from ..work.y2012 import rensburg2012a
from ..work.y2012 import mandić2012ab
from ..work.y2013 import novais2013a
from ..work.y2013 import trendowicz2013a
from ..work.y2013 import münch2013c
from ..work.y2013 import basili2013a
from ..work.y2013 import gencel2013a
from ..work.y2013 import ferreira2013a
from ..work.y2013 import münch2013d
from ..work.y2013 import kläs2013a
from ..work.y2013 import giannoulis2013a
from ..work.y2013 import jedlitschka2013a
from ..work.y2013 import oberscheven2013a
from ..work.y2013 import hästbacka2013a
from ..work.y2013 import guinea2013a
from ..work.y2013 import osadchyy2013a
from ..work.y2013 import lavazza2013a
from ..work.y2013 import heidrich2013a
from ..work.y2013 import doerr2013a
from ..work.y2013 import olsina2013a
from ..work.y2013 import hästbacka2013b
from ..work.y2013 import eremenko2013a
from ..work.y2013 import trendowicz2013b
from ..work.y2014 import wallace2014a
from ..work.y2014 import paternoster2014a
from ..work.y2014 import giardino2014a
from ..work.y2014 import olsina2014a
from ..work.y2014 import kobori2014b
from ..work.y2014 import kobori2014a
from ..work.y2014 import liggesmeyer2014a
from ..work.y2014 import heidrich2014a
from ..work.y2014 import cedergren2014a
from ..work.y2014 import unterkalmsteiner2014a
from ..work.y2014 import jahn2014a
from ..work.y2014 import zhang2014a
from ..work.y2014 import giannoulis2014a
from ..work.y2014 import janes2014a
from ..work.y2014 import kettunen2014a
from ..work.y2014 import ebner2014a
from ..work.y2014 import cocozza2014a
from ..work.y2014 import poligadu2014a
from ..work.y2014 import becker2014a
from ..work.y2014 import falessi2014a
from ..work.y2014 import trendowicz2014a
from ..work.y2014 import mitre2014a
from ..work.y2014 import rombach2014a
from ..work.y2014 import basili2014a
from ..work.y2014 import mitrehernández2014a
from ..work.y2014 import jørgensen2014a
from ..work.y2014 import trendowicz2014b
from ..work.y2014 import boehm2014a
from ..work.y2014 import ferreira2014a
from ..work.y2014 import YAMAMOTO2014a
from ..work.y2015 import bird2015a
from ..work.y2015 import becker2015a
from ..work.y2015 import kläs2015a
from ..work.y2015 import álvarez2015a
from ..work.y2015 import murphy2015a
from ..work.y2015 import koumaditis2015a
from ..work.y2015 import rivera2015a
from ..work.y2015 import lavazza2015a
from ..work.y2015 import papa2015a
from ..work.y2015 import rivera2015ab
from ..work.y2015 import abdulameer2015a
from ..work.y2015 import lavazza2015b
from ..work.y2015 import hyvönen2015a
from ..work.y2015 import jeners2015a
from ..work.y2015 import xu2015a
from ..work.y2016 import kim2016a
from ..work.y2016 import rivera2016a
from ..work.y2016 import rivera2016b
from ..work.y2016 import tahir2016a
from ..work.y2016 import aoki2016a
from ..work.y2016 import kobori2016a
from ..work.y2016 import djouab2016a
from ..work.y2016 import lópez2016b
from ..work.y2016 import lópez2016a
from ..work.y2016 import ahmad2016a
from ..work.y2016 import papa2016a
from ..work.y2016 import koumaditis2016a
from ..work.y2016 import jaramillo2016a
from ..work.y2016 import rivera2016c
from ..work.y2016 import yamamoto2016a
from ..work.y2016 import diep2016a
from ..work.y2016 import khalifa2016a
from ..work.y2016 import port2016a
from ..work.y2016 import armstrong2016a
from ..work.y2016 import machado2016a
from ..work.y2017 import mandić2017a
from ..work.y2017 import sanchez2017a
from ..work.y2017 import olsina2017a
from ..work.y2017 import washizaki2017a
from ..work.y2017 import pérez2017a
from ..work.y2017 import becker2017a
from ..work.y2017 import santos2017a
from ..work.y2017 import zapata2017a
from ..work.y2017 import mughal2017a
from ..work.y2017 import nicho2017a
from ..work.y2017 import pinheiro2017a
from ..work.y2017 import tebes2017a
from ..work.y2017 import ОВ2017a
from ..work.y2018 import novais2018a
from ..work.y2018 import sanchez2018a
from ..work.y9999 import anders9999a
from ..work.y9999 import heidrich9999a

DB(Citation(
    basili2010a, basili1994a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, basili2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, kaplan1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, usddusa2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, becker1999a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, buglione2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, bianchi2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, card2003b, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, code2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, clegg1994a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2010a, boehm2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    wallace2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    paternoster2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    novais2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lew2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    giardino2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kim2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    guzmán2010a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    papa2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    münch2013c, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sarcia2010a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bird2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    becker2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    becker2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    becker2011b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lew2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gencel2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010c, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cedergren2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kläs2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ferreira2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010d, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    münch2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kobori2014b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    monden2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    münch2013d, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2011b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rivera2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kläs2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kobori2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liggesmeyer2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rivera2016b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    giannoulis2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tahir2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    álvarez2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heidrich2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    murphy2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eremenko2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cedergren2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    aoki2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jedlitschka2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2010f, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    unterkalmsteiner2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jahn2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lescher2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kobori2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhang2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oberscheven2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lavazza2011a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    giannoulis2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    djouab2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hernández2010a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hästbacka2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hästbacka2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leschera2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    guinea2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lópez2016b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    janes2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    osadchyy2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lópez2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ahmad2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    papa2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kettunen2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ebner2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lavazza2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heidrich2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    koumaditis2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cocozza2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    marca2010a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sanchez2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    poligadu2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    koumaditis2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jaramillo2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rivera2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heidrich2012b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    doerr2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    novais2018a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    asghari2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lavazza2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    washizaki2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pérez2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    becker2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    papa2012b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    papa2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rivera2015ab, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rivera2016c, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    becker2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    yamamoto2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    falessi2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    diep2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    khalifa2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitre2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    machado2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    abdulameer2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rombach2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    port2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    santos2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    armstrong2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cedergren2011b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sanchez2018a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    machado2016a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zapata2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mughal2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lavazza2015b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    buse2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    basili2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    anders9999a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heidrich9999a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nicho2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mitrehernández2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olsina2012b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jørgensen2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hästbacka2013b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2014b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hyvönen2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rombach2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eremenko2013a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jeners2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rensburg2012a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    boehm2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pinheiro2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mandić2012ab, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ferreira2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tebes2017a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    xu2015a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trendowicz2013b, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    YAMAMOTO2014a, basili2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ОВ2017a, basili2010a, ref="",
    contexts=[

    ],
))
