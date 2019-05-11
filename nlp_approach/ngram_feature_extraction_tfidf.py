'''
Converts files of confirmation text hearings into vectorized counts of 1to5-grams.
Also applies the tf-idf transform.
Merges the counts with justice and case data and outputs the X,Y dataset.
'''

from collections import Counter
import os
import string
import pickle
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


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
vectorizer = CountVectorizer(input="filename", stop_words="english", max_features=5000, ngram_range=(1,5))
X = vectorizer.fit_transform(new_files)

# print n-grams
print(vectorizer.get_feature_names())
pickle.dump(vectorizer.get_feature_names(), open("data/ngrams/1to5grams_names.p", "wb"))

transformer = TfidfTransformer()
X = transformer.fit_transform(X)
Xdata = X.toarray()
pickle.dump(Xdata, open("data/ngrams/1to5grams.p", "wb"))
print("Number of ngrams: ", len(Xdata[0]))


# merge justice case data with n-grams from utterances
jc_data = pickle.load(open("../demographic_approach/data/cases_justices_merged.pk", "rb" ))
jc_data.sort_values(by=['justiceName'])
ngram_df = pd.DataFrame(data=np.array(Xdata).T, columns=justicenames)
ngram_df = ngram_df.T
ngram_df["justiceName"] = ngram_df.index
jc_data = jc_data.merge(ngram_df, on='justiceName')

# pickle.dump(jc_data, open("data/case_justices_1grams_merged.p", "wb"))

X = jc_data.drop(columns = ["justice", "justiceName", "justice_vote"]).values.astype(np.float64)
Y = jc_data["justice_vote"].values.astype(np.int32)
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(X)
X = imp.transform(X)

np.save("data/case_justices_1to5grams_merged_X_idf.npy", X)
np.save("data/case_justices_1to5grams_merged_Y_idf.npy", Y)

print("Done")