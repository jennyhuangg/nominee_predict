from collections import Counter
import os
import string
import pickle
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer


# Get file names
in_dir = "data/transcripts/utterances"
files = os.listdir(in_dir)
files.sort()
new_files = []
for f in files:
    if f.endswith(".txt"):
        new_files.append(os.path.join(in_dir,f))

# vectorize 1-gram counts
vectorizer = CountVectorizer(input="filename", stop_words="english", max_df=0.9)
X = vectorizer.fit_transform(new_files)
Xdata = X.toarray()
pickle.dump(Xdata, open("data/ngrams/1grams.p", "wb"))

# print n-grams and total number of n-grams
# print(vectorizer.get_feature_names())
print("Number of ngrams: ", len(Xdata[0]))

# merge justice case data with n-grams from utterances
justicenames = [x[:-4] for x in files]
print(justicenames)
jc_data = pickle.load(open("../demographic_approach/data/cases_justices_merged.pk1", "rb" ))
jc_data.sort_values(by=['justiceName'])
ngram_df = pd.DataFrame(data=np.array(Xdata).T, columns=justicenames)
ngram_df = ngram_df.T
ngram_df["justiceName"] = ngram_df.index
jc_data.merge(ngram_df, on='justiceName')

pickle.dump(jc_data, open("data/case_justices_1grams_merged.p", "wb"))

print("Done")