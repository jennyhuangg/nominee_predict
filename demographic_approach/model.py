# %%
import subprocess
import os
import re
import pathlib
import qgrid
import ipywidgets as widgets

%matplotlib inline

#%%
scdb_file = "nlp_approach/data/scdb.csv"
scdb_path = os.path.join(os.getcwd(), scdb_file)
scdb = pd.read_csv(scdb_path, encoding="latin")
