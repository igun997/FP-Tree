import pandas as pd
from copy import deepcopy
import numpy as np
import pyfpgrowth


def convert_toInt(s):
    nilai = 0
    if (s == "anemia defisiensi besi defisiensi besi"):
        nilai = 1
    elif (s == "Iron deficiency anemia "):
        nilai = 2
    else:
        nilai = 3
    return nilai
data = pd.read_csv("training_data.csv","ISO-8859-1",";")
headers = pd.read_csv("training_data.csv",index_col=0, nrows=0,delimiter=";")
cleaner = data.copy()
cleaner = cleaner[["REG_NO","REG_DATE","TEST_NAME","RESULT","REF_RANGE","DESCRIPTION"]]
print(cleaner)


filterAll = pd.DataFrame(cleaner)
filterAll['REG_DATE'] = pd.to_datetime(filterAll['REG_DATE'], errors='coerce')
# grouped = filterAll.groupby(filterAll['REG_DATE'].dt.strftime('%m'))
# print(grouped)
uniques = filterAll["DESCRIPTION"].unique()
# Set 1,2,3
print(uniques)
for index in filterAll.index:
    filterAll.loc[index, "DESCRIPTION"] = convert_toInt(filterAll.loc[index,"DESCRIPTION"])
print(filterAll)

# filterAll["DESCRIPTION"] = filterAll[["REG_NO","DESCRIPTION"]].groupby(['REG_NO'])['DESCRIPTION'].transform(lambda x: ','.join(str(x)))
#
# filtered = filterAll[["REG_NO","DESCRIPTION"]].drop_duplicates()
filtered = filterAll
print(filtered)
# for index, row in filterAll.iterrows():
#     print(row['REG_DATE'], row['TEST_NAME'])
patterns = pyfpgrowth.find_frequent_patterns(filtered,1)
print("Patern")
print(patterns)
rules = pyfpgrowth. generate_association_rules(patterns,0.8)
print("Rules")
print(rules)

