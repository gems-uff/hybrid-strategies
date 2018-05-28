# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *

kitchenham2010a = DB(WorkOk(
    2010, "Systematic literature reviews in software engineering: A tertiary study",
    display="kitchenham",
    authors="Kitchenham, B. A., Pretorius, R., Budgen, D., Brereton, O. P., Turner, M., Niazi, M. and Linkman, S.",
    place=IST,
    other1="52, 8, 792-805.",
))

macdonell2010a = DB(WorkOk(
    2010, "How reliable are systematic reviews in empirical software engineering?",
    display="macdonell",
    authors="MacDonell, S., Shepperd, M., Kitchenham, B. A. and Mendes, E.",
    place=ToSE,
    other1="36, 5, 676687",
))
