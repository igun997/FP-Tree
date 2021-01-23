import pandas as pd
from copy import deepcopy
data = pd.read_csv("training_data.csv","ISO-8859-1",";")
headers = pd.read_csv("training_data.csv",index_col=0, nrows=0,delimiter=";")
cleaner = data.copy()
cleaner = cleaner[["REG_DATE","TEST_NAME","RESULT","TEST_FLAG_NAME","REF_RANGE","DESCRIPTION"]]
print(cleaner)
print(headers)


