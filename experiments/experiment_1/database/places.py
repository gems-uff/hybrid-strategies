from snowballing.models import Place, DB
from snowballing.common_places import *


ASSM = conference("ASSM", "Applied Statistics for Software Managers")
ACMICPS = conference("ACMICPS", "ACM International Conference Proceeding Series")
AISC = journal("AISC", "Advances in Intelligent Systems and Computing")
BMJ = journal("BMJ", "BMJ")
BI = journal("BI","Biometrics")
BIP = journal("BIP", "Business Information Processing")
BC=journal("BC","Benjamin-Cummins")
CACM = journal("CACM", "Communications of the ACM")
CAESAR = journal("CAESAR", "CAESAR")
C = journal ("C", "Computer")
CC = journal("CC","Computer Communications")
CCIS = conference ("CCIS","Communications in Computer and Information Science")
CSI = journal("CSI", "Computer Standards & Interfaces")
CSUR = journal("CSUR", "ACM Computing Surveys")
DASC = conference("DASC", "Digital Avionics Systems Conference")
DP = journal("DP","Duxbury Press")
EASE = conference("EASE", "Evaluation and Assessment in Software Engineering")
EBSE = journal("EBSE", "EBSE Technical Report")
ECIME = conference("ECIME","European Conference on Information Management and Evaluation")
ESE = journal("ESE", "Empirical Software Engineering")
FTC = journal("FTC","Future Technologies Conference")
GWCBR = journal("GWCBR", "German Workshop on Case-Based Reasoning")

IACSE = conference("IACSE", "Ibero-American Conference on Software Engineering")
ICASE = conference("ICASE","IEEE/ACM International Conference on Automated Software Engineering")
ICACCI = journal("ICACCI","Advances in Computing, Communications and Informatics")
ICEIS = conference ("ICEIS","International Conference on Enterprise Information Systems")
IC=journal("IC","Information Sciences")
ICL = journal("ICL", "ICL technical journal")
ICSE = conference("ICSE", "International Conference on Software Engineering")
ICSPICD = conference("ICSPICD","International Conference on Software Process Improvement and Capability Determination")
ICPFSPI = conference("ICPFSPI","International Conference on Product Focused Software Process Improvement")
ICQICT = conference("ICQICT","International Conference on the Quality of Information and Communications Technology")
IEECD = conference("IEECD", "IEE Colloquium (Digest)")
IEEE = conference("IEEE", "International Software Engineering Conference")
IEEES= journal("IEEES","IEEE Software")
IMECE = conference("IMECE","International Mechanical Engineering Congress and Exposition")
ISSM = conference("ISSM", "International Symposium on Software Metrics")
ISMS = conference("ISMS", "International Software Metrics Symposium")
IST =  journal("IST","Information & Software Technology")
IWSM = conference("IWSM","Internatina Workshop on Software Measurement")
IWETSM = conference("IWETSM", "International Workshop on Emerging Trends in Software Metrics")
JBCS = conference ("JBCS", "Journal of the Brazilian Computer Society")
JCP =  journal("JCP","Journal of Cleaner Production")
ICASEA = conference("ICASEA","International Conference on Advanced Software Engineering and Its Applications")
ICSA = conference("ICSA","Software Architecture (ICSA), 2017 IEEE International Conference on")
ESEM =  conference("ESEM","International Symposium on Empirical Software Engineering and Measurement")

IPAW = conference("IPAW", "International Provenance and Annotation Workshop")

JCA = journal("JCA","International Journal of Computers and Applications")
JCS = journal("JCS","Journal of Computer Science")
JCP =  journal("JCP","Journal of Cleaner Production")
JSEP = journal("JSEP", "Journal of Software: Evolution and Process")
JSS = journal("JSS", "Journal of Systems and Software")

LEA = journal("LEA","Lawrence Erlbaum Associates")
MK = journal("MK", "Morgan Kaufmann")
MIS = conference("MIS", "Management Information Systems Quarterly")
MODELSWARD = conference("MODELSWARD", "Model-Driven Engineering and Software Development (MODELSWARD), 2016 4th International Conference on")
MS = journal("MS", "Management Science")

ICSTW = conference("ICSTW", "Software Testing, Verification and Validation Workshops")
ISESE = conference("ISESE","ACM/IEEE international symposium on Empirical software engineering")
ISBSG = conference("ISBSG","ISBSG")
IWBIPI = conference("IWBIPI","International Workshop on Business Impact of Process Improvements")
ICSPPM = conference ("ICSPPM","International Conference on Software Process and Product Measurement")
PMSE = conference("PMSE","international workshop on Predictor models in software engineering")
PROFES = conference("PROFES", "Product-Focused Software Process Improvement")
Producao = journal("Producao", "Producao")
QASS = conference("QASS", "Quantitative Applications in the Social Sciences")
RCIS = conference("RCIS","Research Challenges in Information Science")
REFSQ = conference("REFSQ", "International Working Conference on Requirements Engineering: Foundation for Software Quality")
RN = journal ("RN", "Research Note - UCL DEPARTMENT OF COMPUTER SCIENCE")
REABTIC = journal("REABTIC", "Revista Eletrônica Argentina-Brasil de Tecnologias da Informacao e da Comunicacao")
SAGE = journal("SAGE","SAGE Publications")
SBSE = conference("SBSE","Search Based Software Engineering")
SCAM = conference("SCAM", "Source Code Analysis and Manipulation, 2016 IEEE 16th International Working Conference on")
SCP = conference("SCP", "Science of computer programming")
SEAA = conference("SEAA","Software Engineering and Advanced Applications")
SEC=conference("SEC","Software Engineering Conference")
SIGSOFT = conference("SIGSOFT","European software engineering conference and the ACM SIGSOFT symposium on The foundations of software engineering")
SITA = conference("SITA","INTERNATIONAL CONFERENCE ON INTELLIGENT SYSTEMS: THEORIES AND APPLICATIONS")
SPICD = conference("SPICD", "SOFTWARE PROCESS IMPROVEMENT AND CAPABILITY DETERMINATION")
SPIP = journal("SPIP","Software Process Improvement and Practice")
SM=conference("SM","Software Metrics")
SQJ = journal("SQJ", "Software Quality Journal")
SQRS = conference("SQRS", "Software Quality, Reliability and Security")

TaPP = conference("TaPP", "Workshop on the Theory and Practice of Provenance")
TITS = conference("TITS", "IEEE Transactions on Intelligent Transportation Systems")

Tec= journal("Tec", "Technometrics")
ToR = journal("ToR", "IEEE Transactions on Reliability")
ToSE = conference("ToSE", "Transactions on Software Engineering")
TMMSME = conference("TMMSME","Tutorial on Models and Metrics for Software Management and Engineering")
WE = journal("WE","Web  Engineering")
WWW = conference("WWW", "International World Wide Web Conference")

arXiv = DB(Place("arXiv", "arXiv", "Archive"))
FAKE = DB(Place("Fake", "Fake", "Fake"))