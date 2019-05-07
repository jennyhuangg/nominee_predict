# %%
import numpy as np
import pandas as pd
import sklearn
import sklearn.preprocessing
from  sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import qgrid
#%%
df = pd.read_pickle("data/cases_justices_merged.pk")


#%%
# For comparison, we see how effective past votes are at predicting currrent voting behavior




#%%
# df = df.dropna()
# df.fillna(df.mode().iloc[0])
X = df.drop(columns = ["justice", "justiceName", "justice_vote"])
Y = df["justice_vote"]

min_max_scaler = sklearn.preprocessing.StandardScaler()
X = min_max_scaler.fit_transform(X)

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(X)
X = imp.transform(X)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

reg = linear_model.LogisticRegression(penalty="l1")

reg.fit(X_train, Y_train)
reg.score(X_test, Y_test)

coeffs = pd.DataFrame(zip(reg.classes_, reg.coef_[0]), columns=["var", "coefficient"])
coeffs
coeffs.to_csv("logreg.csv")
    
