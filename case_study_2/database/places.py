from snowballing.models import Place, DB
from snowballing.common_places import *

AISC = journal("AISC", "Advances in Intelligent Systems and Computing")
BMJ = journal("BMJ", "BMJ")
CC = journal("CC","Computer Communications")
CSI = journal("CSI", "Computer Standards & Interfaces")
CSUR = journal("CSUR", "ACM Computing Surveys")

EASE = conference("EASE", "Evaluation and Assessment in Software Engineering")
EBSE = journal("EBSE", "EBSE Technical Report")
ESE = journal("ESE", "Empirical Software Engineering")

IACSE = conference("IACSE", "Ibero-American Conference on Software Engineering")
ICSE = conference("ICSE", "International Conference on Software Engineering")
IEEE = conference("IEEE", "International Software Engineering Conference")
ISSM = conference("ISSM", "International Symposium on Software Metrics")
ISMS = conference("ISMS", "International Software Metrics Symposium")
IST =  journal("IST","Information & Software Technology")

JCP =  journal("JCP","Journal of Cleaner Production")

ICSA = conference("ICSA","Software Architecture (ICSA), 2017 IEEE International Conference on")
ESEM =  conference("ESEM","International Symposium on Empirical Software Engineering and Measurement")

IPAW = conference("IPAW", "International Provenance and Annotation Workshop")

JCP =  journal("JCP","Journal of Cleaner Production")
JSEP = journal("JSEP", "Journal of Software: Evolution and Process")
JSS = journal("JSS", "Journal of Systems and Software")

MIS = conference("MIS", "Management Information Systems Quarterly")
MODELSWARD = conference("MODELSWARD", "Model-Driven Engineering and Software Development (MODELSWARD), 2016 4th International Conference on")
MS = journal("MS", "Management Science")

ICSTW = conference("ICSTW", "Software Testing, Verification and Validation Workshops")

PROFES = conference("PROFES", "Product-Focused Software Process Improvement: 17th International Conference, PROFES 2016")

RCIS = conference("RCIS","Research Challenges in Information Science")
REFSQ = conference("REFSQ", "International Working Conference on Requirements Engineering: Foundation for Software Quality")

SCAM = conference("SCAM", "Source Code Analysis and Manipulation, 2016 IEEE 16th International Working Conference on")
SQJ = journal("SQJ", "Software Quality Journal")
SQRS = conference("SQRS", "Software Quality, Reliability and Security")

TaPP = conference("TaPP", "Workshop on the Theory and Practice of Provenance")
TITS = conference("TITS", "IEEE Transactions on Intelligent Transportation Systems")

ToR = journal("ToR", "IEEE Transactions on Reliability")
ToSE = conference("ToSE", "Transactions on Software Engineering")

arXiv = DB(Place("arXiv", "arXiv", "Archive"))
