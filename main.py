import pandas as pd
from copy import deepcopy
import numpy as np
import pyfpgrowth
from fpgrowth_py import fpgrowth


def convert_toInt(s):
    nilai = 0
    if (s == "anemia defisiensi besi defisiensi besi"):
        nilai = 1
    elif (s == "Iron deficiency anemia "):
        nilai = 2
    else:
        nilai = 3
    return nilai


data = pd.read_csv("training_data.csv", "ISO-8859-1", ";")
headers = pd.read_csv("training_data.csv", index_col=0, nrows=0, delimiter=";")
cleaner = data.copy()
cleaner = cleaner[["REG_NO", "TEST_NAME", "RESULT", "REF_RANGE", "DESCRIPTION"]]
print(cleaner)

filterAll = pd.DataFrame(cleaner)

filterAll["DESCRIPTION"] = filterAll[["REG_NO", "DESCRIPTION"]].groupby(['REG_NO'])['DESCRIPTION'].transform(
    lambda x: ','.join(x))

filtered = filterAll[["REG_NO", "DESCRIPTION"]].drop_duplicates()
filterData = []
for index in filtered.index:
    uniqueIt = filtered.loc[index, "DESCRIPTION"].split(",")
    filterData.append(np.unique(uniqueIt))

freqItemSet, rules = fpgrowth(filterData, minSupRatio=0.5, minConf=0.5)
print(freqItemSet)
print(rules)
