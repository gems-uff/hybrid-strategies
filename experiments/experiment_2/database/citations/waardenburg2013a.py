# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1967 import glaser1967b
from ..work.y1972 import janis1972a
from ..work.y1974 import harvey1974a
from ..work.y1978 import glaser1978b
from ..work.y1988 import boehm1988a
from ..work.y1988 import strauss1988a
from ..work.y1989 import star1989a
from ..work.y1991 import denison1991a
from ..work.y1991 import schwaber1991a
from ..work.y1992 import glaser1992a
from ..work.y1998 import glaser1998a
from ..work.y1998 import parry1998a
from ..work.y2000 import tanis2000a
from ..work.y2001 import beck2001a
from ..work.y2001 import cockburn2001a
from ..work.y2001 import sutherland2001a
from ..work.y2002 import agarwal2002a
from ..work.y2002 import boehm2002a
from ..work.y2002 import boehm2002b
from ..work.y2002 import cockburn2002a
from ..work.y2003 import abrahamsson2003a
from ..work.y2003 import allan2003a
from ..work.y2003 import cohn2003a
from ..work.y2003 import rasmusson2003a
from ..work.y2004 import drobka2004a
from ..work.y2004 import fraser2004a
from ..work.y2004 import he2004a
from ..work.y2004 import lindvall2004a
from ..work.y2005 import augustine2005a
from ..work.y2005 import boehm2005a
from ..work.y2005 import grisham2005a
from ..work.y2005 import levina2005a
from ..work.y2005 import nerur2005a
from ..work.y2005 import robinson2005a
from ..work.y2005 import svensson2005a
from ..work.y2006 import boehm2006c
from ..work.y2006 import karlström2006a
from ..work.y2006 import vinekar2006a
from ..work.y2007 import coleman2007a
from ..work.y2007 import conboy2007a
from ..work.y2007 import siakas2007a
from ..work.y2008 import benefield2008a
from ..work.y2008 import dybå2008a
from ..work.y2008 import isham2008a
from ..work.y2008 import kettunen2008a
from ..work.y2008 import moore2008a
from ..work.y2008 import pikkarainen2008a
from ..work.y2008 import tolfo2008a
from ..work.y2008 import vanvliet2008a
from ..work.y2009 import cao2009a
from ..work.y2009 import chan2009a
from ..work.y2009 import conboy2009a
from ..work.y2009 import larman2009a
from ..work.y2009 import mcavoy2009a
from ..work.y2009 import misra2009a
from ..work.y2009 import ogc2009a
from ..work.y2009 import petersen2009a
from ..work.y2009 import pink2009a
from ..work.y2009 import strode2009a
from ..work.y2010 import heidenberg2010a
from ..work.y2010 import petersen2010a
from ..work.y2011 import adolph2011a
from ..work.y2011 import baskerville2011a
from ..work.y2011 import hoda2011a
from ..work.y2011 import iivari2011a
from ..work.y2011 import laanti2011a
from ..work.y2011 import mishra2011a
from ..work.y2011 import ferreira2011a
from ..work.y2012 import adolph2012a
from ..work.y2012 import dingsøyr2012a
from ..work.y2012 import hoda2012a
from ..work.y2012 import kurapati2012a
from ..work.y2012 import magdaleno2012a
from ..work.y2012 import pikkarainen2012a
from ..work.y2012 import strode2012a
from ..work.y2012 import vijayasarathy2012a
from ..work.y2013 import waardenburg2013a
from ..work.y2013 import birks2013a
from ..work.y2013 import brown2013a
from ..work.y2013 import hoda2013a
from ..work.y2013 import kruchten2013a
from ..work.y2013 import matavire2013a
from ..work.y2014 import tarhan2014a
from ..work.y2014 import bass2014a
from ..work.y2014 import manen2014a
from ..work.y2014 import morken2014a
from ..work.y2014 import cornelius2014a
from ..work.y2014 import campanelli2014a
from ..work.y2014 import haaster2014a
from ..work.y2014 import bass2014b
from ..work.y2014 import salopaasi2014a
from ..work.y2015 import campanelli2015a
from ..work.y2015 import vlietland2015a
from ..work.y2015 import bass2015a
from ..work.y2015 import gregory2015a
from ..work.y2015 import heikkilä2015a
from ..work.y2015 import tomanek2015a
from ..work.y2015 import berger2015a
from ..work.y2015 import singh2015a
from ..work.y2015 import baseer2015a
from ..work.y2015 import darnell2015a
from ..work.y2015 import behm2015a
from ..work.y2015 import petrik2015a
from ..work.y2015 import felipe2015a
from ..work.y2015 import homrich2015a
from ..work.y2015 import felipe2015b
from ..work.y2015 import vlietland2015b
from ..work.y2015 import luger2015a
from ..work.y2015 import haaster2015a
from ..work.y2015 import roslund2015a
from ..work.y2016 import gregory2016a
from ..work.y2016 import kuusinen2016a
from ..work.y2016 import fitriani2016a
from ..work.y2016 import laukkanen2016a
from ..work.y2016 import bishop2016a
from ..work.y2016 import diebold2016a
from ..work.y2016 import zhang2016a
from ..work.y2016 import joseph2016a
from ..work.y2016 import haaster2016a
from ..work.y2016 import alzoubi2016b
from ..work.y2016 import confidential2016
from ..work.y2016 import chassart2016a
from ..work.y2016 import vrhovec2016a
from ..work.y2016 import norberg2016a
from ..work.y2016 import leur2016a
from ..work.y2016 import norberg2016b
from ..work.y2017 import joseph2017a
from ..work.y2017 import jovanovi2017a
from ..work.y2017 import kusters2017a
from ..work.y2017 import deley2017a
from ..work.y2017 import kalliamvakou2017a
from ..work.y2017 import patel2017a
from ..work.y2017 import haines2017a
from ..work.y2017 import östman2017a
from ..work.y2017 import musura2017a
from ..work.y2017 import alkema2017a
from ..work.y2017 import garbulho2017a
from ..work.y2017 import assis2017a
from ..work.y2017 import gencer2017a
from ..work.y2017 import almeida2017a
from ..work.y2017 import garcia2017b
from ..work.y2017 import jovanovi2017b
from ..work.y2017 import assis2017b
from ..work.y2018 import barroca2018a
from ..work.y2018 import hron2018a
from ..work.y2018 import campanelli2018a
from ..work.y2018 import theobald2018a
from ..work.y2018 import laukkanen2018a
from ..work.y2018 import sulaiman2018a
from ..work.y2018 import kinnunen2018a
from ..work.y2018 import järvi2018a

DB(Citation(
    waardenburg2013a, abrahamsson2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, adolph2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, adolph2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, agarwal2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, allan2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, augustine2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, baskerville2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, beck2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, benefield2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, birks2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, boehm2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, boehm2006c, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, boehm2002b, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, boehm2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, boehm1988a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, brown2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, cao2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, chan2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, cockburn2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, cockburn2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, cohn2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, coleman2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, conboy2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, conboy2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, denison1991a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, dingsøyr2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, drobka2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, dybå2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, fraser2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, glaser1978b, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, glaser1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, glaser1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, glaser1967b, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, grisham2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, harvey1974a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, he2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, heidenberg2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, hoda2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, hoda2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, iivari2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, isham2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, janis1972a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, karlström2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, kettunen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, kruchten2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, kurapati2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, laanti2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, larman2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, levina2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, lindvall2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, magdaleno2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, matavire2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, mcavoy2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, mishra2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, misra2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, moore2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, nerur2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, ogc2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, parry1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, ferreira2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, petersen2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, petersen2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, pikkarainen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, pikkarainen2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, pink2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, rasmusson2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, robinson2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, schwaber1991a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, siakas2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, star1989a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, strauss1988a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, strode2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, strode2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, sutherland2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, svensson2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, tanis2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, tolfo2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, vanvliet2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, vijayasarathy2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2013a, vinekar2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    campanelli2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gregory2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tarhan2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gregory2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heikkilä2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tomanek2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    barroca2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kuusinen2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fitriani2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    berger2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    singh2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    laukkanen2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    baseer2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    manen2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bishop2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    morken2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    joseph2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    darnell2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jovanovi2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cornelius2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kusters2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hron2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    campanelli2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    behm2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    petrik2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    diebold2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    campanelli2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    deley2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    theobald2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    laukkanen2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haaster2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kalliamvakou2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    patel2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    felipe2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhang2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    joseph2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2014b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haaster2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    homrich2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alzoubi2016b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haines2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    confidential2016, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    östman2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    felipe2015b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    musura2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chassart2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vlietland2015b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sulaiman2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vrhovec2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    luger2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alkema2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haaster2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kinnunen2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    garbulho2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    norberg2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leur2016a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    assis2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    roslund2015a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    järvi2018a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gencer2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    norberg2016b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    almeida2017a, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    garcia2017b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jovanovi2017b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    assis2017b, waardenburg2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    salopaasi2014a, waardenburg2013a, ref="",
    contexts=[

    ],
))
