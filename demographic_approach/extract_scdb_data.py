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
    "partyWinning": "category",
    "majority": "category",
    "vote": "object"
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

#%%
# No column for whether the justice voted in favor of the plaintiff or not, 
# which is what we are trying to predict. Construct this from a conjunction of
# how majority voted and if justice voted with the majority

# Drop rows without clear partywinning
df = df[df.partyWinning != "2"]
df.partyWinning = df.partyWinning.cat.remove_unused_categories()
df.partyWinning.value_counts()

df.vote.value_counts()
# Create new column justice_vote, which is 1 if voted in favor of plaintiff
# and 0 if voted in favor of defendant

# partyWinning = 1 if the plaintiff won and 2 otherwise. Thus if the justice voted
# with the majority and the plaintiff won, we can conclude the justice voted in
# favor of the plaintiff
df["justice_vote"] = np.where((df.partyWinning == "1") & (df.vote == "1"), 1, 0)
# Remove unneeeded outcome rows
df = df.drop(columns=["partyWinning", "vote", "majority"])
#%%

df = pd.get_dummies(df, columns=to_dummies)


#%% Merge with nominee demographic data
noms = pd.read_pickle("data/nominees.pk1")

merged = df.merge(noms, left_on="justice", right_on="spaethid")

# only use data for justices we have transcripts for
path = "../nlp_approach/data/transcripts/utterances"
justices = [f.split(".txt")[0] for f in listdir(path) if f.endswith(".txt")]
merged = merged[(merged.justiceName.isin(justices))]


#%%
merged.to_pickle("data/cases_justices_merged.pk")
merged.justice_vote.value_counts()
