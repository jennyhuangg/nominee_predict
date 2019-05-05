#%%
import numpy as np
import pandas as pd
pd.options.display.max_rows = 1000
pd.options.display.max_rows = 50
pd.options.display.max_seq_items = 2000
np.set_printoptions(threshold=500)

from os import listdir
from os.path import isfile, join

#%%
features = {
    # metadata
    "petitionerState": "category",
    "respondentState": "category",
    "jurisdiction": "category",
    "caseOrigin": "category",
    "caseSource": "category",

    # Substantive case data
    "lcDisagreement": "category",
    "certReason": "category",
    "lcDisposition": "category",
    "lcDispositionDirection": "category",
    "issue": "category",
    "issueArea": "category",

    # Justice specific data"
    "justice": "int64",
    "justiceName": "category", # for convenience
    # Justice specific outcome data
    "majority": "category",
    "vote": "category"
}
# Categorical features that we'll need to convert to dummy variables
to_dummies = [
    "petitionerState", "respondentState", "jurisdiction", "caseOrigin",
    "caseSource", "lcDisagreement", "certReason", "lcDisposition",
    "lcDispositionDirection", "issue", "issueArea"
]

#%%
df = pd.read_csv("data/scdb.csv",
                 encoding="latin",
                 dtype=features,
                 usecols=features.keys())

df = pd.get_dummies(df, columns=to_dummies)
#%% Merge with nominee demographic data
noms = pd.read_csv("data/justicesdata.csv", encoding="latin")

merged = df.merge(noms, left_on="justice", right_on="spaethid")

# only use data for justices we have transcripts for
path = "../nlp_approach/data/transcripts/utterances"
justices = [f.split(".txt")[0] for f in listdir(path) if f.endswith(".txt")]
merged = merged[(merged.justiceName.isin(justices))]

#%%
merged.to_pickle("data/cases_justices_merged.pk")
