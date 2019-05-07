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
# st_cats

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

# jd[st_cats] ##a lot of 1s... maybe this isn't useful anymore?... maybe just not seeing the 0s?

#%% removing columns labeled as useless
useless_features = ['zukid', 'readn', 'birdate', 'datenom']
for (a,b,c,d) in columns:
    if d == 3:
        useless_features.append(b)

useless_features
jd = jd.drop(useless_features, axis=1)
# jd
#%% converting absolute year data to years before nomination
#get ids for each year columns
year_cols = []
for (a,b,c,d) in columns:
    if ("Year" in c) & ("Years" not in c) & (b not in useless_features):
        year_cols.append(b)
#get rid of the first element which is yrnom
year_cols = year_cols[1:]
year_cols


#replace these data with yrnom-year
for row in year_cols:
    jd[row] = jd[row].replace(to_replace=[777.0,888.0,999.0], value=np.NaN)
    jd[row] = jd["yrnom"]-jd[row]

#%% get rid of 888,999
jd = jd.replace(to_replace=[888.0,999.0], value=np.NaN)

#%%
# jd.to_pickle('./data/nominees.pk1')

#%% making categorical the categorical categories
#list of data_columns_edited indexes of categorical things:
cat_inds = [13,16,17,18,19,20,21,22,26,31,35,36,39,40,51,56,65,69,73,74,77,78,113,116,119,122,127,130,133,136,205,206,207,210,215]
len(cat_inds)
# cat_cols = [a for (a, b, c, d) in columns if a in cat_inds] -- not sure why this isnt working...
inds_in_col_list = []
for (a,b,c,d) in columns:
    if a in cat_inds:
        inds_in_col_list.append(a)

#what is happening to 10 of these values not getting transfered over?...
missing_test = list(set(cat_inds) - set(inds_in_col_list))
missing_test
# the ones that for some reason aren't detected -- hard code these ids:
# [13, 16, 17, 18, 19, 20, 21, 22, 26, 31]
cat_cols=[]
for (a,b,c,d) in columns:
    if a in cat_inds:
        cat_cols.append(b)

for elt in ["birthcit","childst","childsur","famses","fathpol","famjud","nomrelig","natorig","race","fathoccu","undsch"]:
    cat_cols.append(elt)


#----------------------------------

#%% Replace each categorical column with the new dataframe of dummy variable cols
#   go through the rows adding them, then drop the original categorical col

#Apply this for each categorical column given by the above cell ^^
#input: id of column to be expanded
def replace_with_dummies(df, cat_column):
    col_expanded = pd.get_dummies(jd[cat_column], prefix=cat_column)
    for row in col_expanded:
        df[row] = col_expanded[row]
    df.drop(cat_column, axis=1)

for id in cat_cols:
    replace_with_dummies(jd, id)

jd.to_pickle('./data/nominees.pk1')
