# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1967 import glaser1967a
from ..work.y1978 import glaser1978a
from ..work.y1986 import takeuchi1986a
from ..work.y1992 import glaser1992a
from ..work.y1997 import stapleton1997a
from ..work.y1998 import parry1998a
from ..work.y1998 import strauss1998a
from ..work.y2000 import beck2000a
from ..work.y2000 import highsmith2000a
from ..work.y2001 import highsmith2001a
from ..work.y2001 import cockburn2001a
from ..work.y2002 import schwaber2002a
from ..work.y2002 import palmer2002a
from ..work.y2003 import larman2003a
from ..work.y2003 import martin2003a
from ..work.y2003 import anderson2003a
from ..work.y2003 import fraser2003a
from ..work.y2003 import cockburn2003a
from ..work.y2003 import allan2003a
from ..work.y2003 import boehm2003a
from ..work.y2004 import fraser2004a
from ..work.y2004 import cockburn2004a
from ..work.y2004 import highsmith2004a
from ..work.y2004 import chau2004a
from ..work.y2004 import glasser2004a
from ..work.y2004 import kan2004a
from ..work.y2005 import grisham2005a
from ..work.y2005 import nerur2005a
from ..work.y2005 import augustine2005a
from ..work.y2005 import glaser2005a
from ..work.y2005 import mann2005a
from ..work.y2006 import hanssen2006a
from ..work.y2006 import korkala2006a
from ..work.y2007 import coleman2007a
from ..work.y2007 import lowery2007a
from ..work.y2008 import judy2008a
from ..work.y2008 import chow2008a
from ..work.y2008 import dybå2008a
from ..work.y2008 import pikkarainen2008a
from ..work.y2008 import sharp2008a
from ..work.y2008 import georgieva2008a
from ..work.y2008 import adolph2008a
from ..work.y2009 import martin2009a
from ..work.y2009 import misra2009a
from ..work.y2009 import conboy2009a
from ..work.y2009 import cao2009a
from ..work.y2009 import mangalaraj2009a
from ..work.y2010 import hoda2010a
from ..work.y2010 import hoda2010b
from ..work.y2010 import beaumont2010a
from ..work.y2010 import hoda2010c
from ..work.y2011 import hoda2011a
from ..work.y2011 import hoda2011b
from ..work.y2011 import hoda2011c
from ..work.y2011 import hoda2011d
from ..work.y2011 import stojanov2011a
from ..work.y2011 import saleh2011a
from ..work.y2011 import mchugh2011a
from ..work.y2011 import tahir2011a
from ..work.y2011 import waardenburg2011a
from ..work.y2011 import almeida2011a
from ..work.y2012 import hoda2012b
from ..work.y2012 import senapathi2012a
from ..work.y2012 import kirk2012a
from ..work.y2012 import stojanov2012a
from ..work.y2012 import nielsen2012b
from ..work.y2012 import junior2012a
from ..work.y2012 import porrawatpreyakorn2012a
from ..work.y2013 import schwaber2013b
from ..work.y2013 import bass2013a
from ..work.y2013 import gandomani2013a
from ..work.y2013 import gandomani2013b
from ..work.y2013 import liebel2013a
from ..work.y2013 import rajadurai2013a
from ..work.y2013 import gandomani2013c
from ..work.y2013 import benassi2013a
from ..work.y2014 import conforto2014a
from ..work.y2014 import hummel2014a
from ..work.y2014 import gandomani2014a
from ..work.y2014 import bass2014a
from ..work.y2014 import sverrisdottir2014a
from ..work.y2014 import gandomani2014b
from ..work.y2014 import sharif2014a
from ..work.y2014 import parizi2014a
from ..work.y2014 import kanwal2014a
from ..work.y2014 import babb2014a
from ..work.y2014 import beranek2014a
from ..work.y2014 import shawky2014a
from ..work.y2014 import eichhorn2014a
from ..work.y2014 import kristinsdóttir2014a
from ..work.y2014 import cornelius2014a
from ..work.y2014 import ng2014b
from ..work.y2014 import vanathi2014a
from ..work.y2014 import júnior2014a
from ..work.y2014 import bass2014ab
from ..work.y2014 import amaral2014a
from ..work.y2014 import hellemond2014a
from ..work.y2014 import mehmeti2014a
from ..work.y2014 import krogh2014a
from ..work.y2014 import lang2014a
from ..work.y2015 import inayat2015b
from ..work.y2015 import gandomani2015a
from ..work.y2015 import gandomani2015b
from ..work.y2015 import bass2015a
from ..work.y2015 import gregory2015a
from ..work.y2015 import diebold2015a
from ..work.y2015 import eichhorn2015a
from ..work.y2015 import baumgart2015a
from ..work.y2015 import gonzález2015a
from ..work.y2015 import mckinley2015a
from ..work.y2015 import shirouyehzad112015a
from ..work.y2015 import hutten2015a
from ..work.y2015 import stettina2015b
from ..work.y2015 import idea2015a
from ..work.y2015 import ramadani2015a
from ..work.y2015 import gandomania2015a
from ..work.y2015 import ojastu2015a
from ..work.y2015 import mohamed2015a
from ..work.y2015 import torstensen2015a
from ..work.y2015 import ikram2015a
from ..work.y2015 import read2015a
from ..work.y2015 import reljanovic2015a
from ..work.y2015 import roslund2015a
from ..work.y2015 import widell2015a
from ..work.y2016 import stol2016a
from ..work.y2016 import conforto2016a
from ..work.y2016 import moran2016a
from ..work.y2016 import gregory2016a
from ..work.y2016 import hoda2016a
from ..work.y2016 import gandomani2016a
from ..work.y2016 import yagüe2016a
from ..work.y2016 import zhang2016b
from ..work.y2016 import batra2016a
from ..work.y2016 import roses2016a
from ..work.y2016 import stanica2016a
from ..work.y2016 import marshall2016b
from ..work.y2016 import tareq2016a
from ..work.y2016 import persson2016a
from ..work.y2016 import kristinsdottir2016a
from ..work.y2016 import gonzález2016a
from ..work.y2016 import hall2016a
from ..work.y2016 import sunner2016a
from ..work.y2016 import rathor2016a
from ..work.y2016 import tootoonchi2016a
from ..work.y2016 import ghimire2016a
from ..work.y2016 import truszczynski2016a
from ..work.y2016 import zaitsev2016a
from ..work.y2016 import rathor2016ab
from ..work.y2016 import werder2016a
from ..work.y2016 import gandomani2016b
from ..work.y2016 import bass2016b
from ..work.y2016 import singh2016b
from ..work.y2016 import murugesan2016a
from ..work.y2016 import litchmore2016a
from ..work.y2016 import iyawa2016a
from ..work.y2017 import alahyari2017a
from ..work.y2017 import shastri2017a
from ..work.y2017 import alqudah2017a
from ..work.y2017 import otaduy2017a
from ..work.y2017 import bordin2017a
from ..work.y2017 import shameem2017a
from ..work.y2017 import jovanovi2017a
from ..work.y2017 import kakar2017a
from ..work.y2017 import ejaz2017a
from ..work.y2017 import kuusinen2017a
from ..work.y2017 import batra2017a
from ..work.y2017 import tessem2017a
from ..work.y2017 import singh2017a
from ..work.y2017 import babb2017a
from ..work.y2017 import klünder2017a
from ..work.y2017 import razzak2017a
from ..work.y2017 import carew2017a
from ..work.y2017 import werder2017a
from ..work.y2017 import li2017a
from ..work.y2017 import oomen2017a
from ..work.y2017 import gjøystdal2017a
from ..work.y2017 import haines2017a
from ..work.y2017 import obrutsky2017a
from ..work.y2017 import slater2017a
from ..work.y2017 import gichuki2017a
from ..work.y2017 import abdul2017a
from ..work.y2017 import regassa2017a
from ..work.y2017 import amrit2017a
from ..work.y2017 import kimawati2017a
from ..work.y2017 import gencer2017a
from ..work.y2017 import bordin2017b
from ..work.y2017 import cengiz2017a
from ..work.y2017 import jovanovi2017b
from ..work.y2017 import gonzález2017a
from ..work.y2017 import combler2017a
from ..work.y2018 import dönmez2018a
from ..work.y2018 import kakar2018a
from ..work.y2018 import kråkevik2018a
from ..work.y2018 import bass2018a
from ..work.y2018 import salleh2018a
from ..work.y2018 import bass2018b
from ..work.y2018 import tolfo2018a
from ..work.y2018 import rodríguez2018a
from ..work.y2018 import ochodek2018a
from ..work.y2018 import bass2018c
from ..work.y2018 import eichhorn2018a

DB(Citation(
    hoda2011a, grisham2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, hanssen2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, judy2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, nerur2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, hoda2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, chow2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, dybå2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, highsmith2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, martin2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, misra2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, fraser2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, larman2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, schwaber2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, beck2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, cockburn2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, palmer2002a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, stapleton1997a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, highsmith2000a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, pikkarainen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, cockburn2001a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, martin2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, schwaber2013b, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, sharp2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, highsmith2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, takeuchi1986a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, augustine2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, anderson2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, chau2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, fraser2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, glaser1978a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, glaser2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, glaser1967a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, hoda2010b, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, cockburn2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, coleman2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, allan2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, parry1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, georgieva2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, glaser1992a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, glasser2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, strauss1998a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, kan2004a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, beaumont2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, conboy2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, cao2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, mangalaraj2009a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, korkala2006a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, lowery2007a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, mann2005a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, boehm2003a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, hoda2010c, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011a, adolph2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    inayat2015b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    conforto2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2012b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    senapathi2012a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stol2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    conforto2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hummel2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moran2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gregory2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2015b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gregory2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011c, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alahyari2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sverrisdottir2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hoda2011d, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kirk2012a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2014b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sharif2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stojanov2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stojanov2012a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    diebold2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    yagüe2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    parizi2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhang2016b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    saleh2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kanwal2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eichhorn2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2013b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    batra2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    babb2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    baumgart2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    beranek2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shawky2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eichhorn2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dönmez2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shastri2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gonzález2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mchugh2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    roses2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stanica2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alqudah2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mckinley2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    otaduy2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    marshall2016b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tareq2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bordin2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kristinsdóttir2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shameem2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jovanovi2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cornelius2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shirouyehzad112015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    persson2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kristinsdottir2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ng2014b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hutten2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gonzález2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hall2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sunner2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stettina2015b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kakar2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kakar2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kråkevik2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liebel2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    vanathi2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tahir2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ejaz2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    júnior2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    idea2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rathor2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tootoonchi2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ghimire2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kuusinen2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rajadurai2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    truszczynski2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ramadani2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    batra2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tessem2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    singh2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zaitsev2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    babb2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    klünder2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    waardenburg2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomania2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2014ab, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    razzak2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rathor2016ab, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carew2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    amaral2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    werder2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hellemond2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    salleh2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    werder2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2018c, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2013c, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tolfo2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oomen2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gjøystdal2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    haines2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mehmeti2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    obrutsky2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    slater2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ojastu2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rodríguez2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gichuki2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ochodek2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    abdul2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gandomani2016b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2016b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mohamed2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    torstensen2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ikram2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    read2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    singh2016b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    murugesan2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bass2018b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    regassa2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    litchmore2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    amrit2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    iyawa2016a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kimawati2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nielsen2012b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eichhorn2018a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    reljanovic2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    roslund2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    junior2012a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gencer2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    krogh2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    porrawatpreyakorn2012a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bordin2017b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    almeida2011a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cengiz2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    widell2015a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jovanovi2017b, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2014a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    benassi2013a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gonzález2017a, hoda2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    combler2017a, hoda2011a, ref="",
    contexts=[

    ],
))
