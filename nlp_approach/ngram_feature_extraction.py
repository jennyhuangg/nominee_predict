from collections import Counter
import os
import string
import pickle
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer


# Get file names
in_dir = "data/transcripts/utterances"
files = os.listdir(in_dir)
files.sort()
new_files = []
justicenames = []
for f in files:
    if f.endswith(".txt"):
        new_files.append(os.path.join(in_dir,f))
        justicenames.append(f[:-4])

print(justicenames)

# vectorize 1-gram counts
vectorizer = CountVectorizer(input="filename", stop_words="english", max_features=5000)
X = vectorizer.fit_transform(new_files)
Xdata = X.toarray()
pickle.dump(Xdata, open("data/ngrams/1grams.p", "wb"))

# print n-grams and total number of n-grams
# print(vectorizer.get_feature_names())
print("Number of ngrams: ", len(Xdata[0]))

# merge justice case data with n-grams from utterances
jc_data = pickle.load(open("../demographic_approach/data/cases_justices_merged.pk", "rb" ))
jc_data.sort_values(by=['justiceName'])
ngram_df = pd.DataFrame(data=np.array(Xdata).T, columns=justicenames)
ngram_df = ngram_df.T
ngram_df["justiceName"] = ngram_df.index
jc_data = jc_data.merge(ngram_df, on='justiceName')

#pickle.dump(jc_data, open("data/case_justices_1grams_merged.p", "wb"))

X = jc_data.drop(columns = ["justice", "justiceName", "justice_vote"]).values.astype(np.float64)
Y = jc_data["justice_vote"].values.astype(np.int32)
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(X)
X = imp.transform(X)

np.save("data/case_justices_1grams_merged_X.npy", X)
np.save("data/case_justices_1grams_merged_Y.npy", Y)

print("Done")