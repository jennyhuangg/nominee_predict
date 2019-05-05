#%%
import pandas as pd
import numpy as np
from data_columns_edited import columns
import re

meta = pd.DataFrame(columns, columns=["num", "id", "description", "category"])
jd = pd.read_csv("data/justicesdata_edited.csv", low_memory=False).iloc[:176]
jd = jd[jd.spaethid != 888]
jd

#find all categories coding in values for different states
# fair to say these are maked by the phrase "...state in which..."
#   there's one "state where...", might wanna go grab that too
st_cats = []
col = meta[meta["description"].str.contains("State in which")]
st_cats = list(col["id"])
st_cats

# traverse through row in st_cats and apply transformation to each
# st_cats row of jd

#%%
# state/cities have values 1-439 --> 888,999 are n/a values
# distinct_outputs = set()
#
# for row in st_cats:
#     for elt in jd[row]:
#         distinct_outputs.add(elt)
#
# distinct_outputs

#%% --> replace 888s and 999s with 0s and everything else with 1s
# jd[st_cats[0]]
# jd[st_cats[0]] = jd[st_cats[0]].replace(to_replace=[888.0,999.0], value=0.0)
# jd[st_cats[0]] = jd[st_cats[0]].replace(to_replace=range(500), value=1.0)
# jd[st_cats[0]]

for row in st_cats:
    jd[row] = jd[row].replace(to_replace=[888.0,999.0], value=0.0)
    jd[row] = jd[row].replace(to_replace=range(500), value=1.0)

jd[st_cats] ##a lot of 1s... maybe this isn't useful anymore?... maybe just not seeing the 0s?

#%% removing columns labeled as useless
useless_features = ['zukid', 'marryr', 'readn']
for (a,b,c,d) in columns:
    if d == 3:
        useless_features.append(b)

jd.drop(useless_features, axis=1)

#%% converting absolute year data to years before nomination
#get ids for each year columns
year_cols = []
for (a,b,c,d) in columns:
    if ("Year" in c) & ("Years" not in c):
        year_cols.append(b)
#get rid of the first element which is yrnom
year_cols = year_cols[1:]


#replace these data with yrnom-year
for row in year_cols:
    jd[row] = jd[row].replace(to_replace=[777.0,888.0,999.0], value=np.NaN)
    jd[row] = jd["yrnom"]-jd[row]

#%% get rid of 888,999
jd = jd.replace(to_replace=[888.0,999.0], value=np.NaN)

#%%
jd.to_pickle('./data/nominees.pk1')
