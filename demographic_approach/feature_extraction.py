# %%
import pandas as pd
import numpy as np
from justice_data_columns import columns

meta = pd.DataFrame(columns, columns=["num", "id", "description", "category"])
jd = pd.read_csv("data/justicesdata.csv")

# %%

# Remove columns labeled as obviously useless
to_drop = meta[meta["category"] == 3]["id"]
jd.drop(to_drop, axis=1)


# Because providing the actual year would definitely lead to overfitting
# we replace any columns corresponding to a start year and an end year
# with the length server and the years between service and nomination
col = meta[meta["description"].str.contains("First Year")][0]:
col
last = meta[col["num"] + 1]

if not last.contains("Last Year"):
    continue

len_col_id = col["id"] + "_length"
years_before_nom_id = col["id"] + "_before_nom"

jd[len_col_id] = jd[last["id"]] - jd[col["id"]]
jd[years_before_nom_id] = jd["yrnom"] - jd["last"]
jd.drop(col["id"])
jd.drop(last["id"])
