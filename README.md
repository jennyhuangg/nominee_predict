# Predicting Voting Behavior of Supreme Court Nominees

AM231 Final Project

The goal of our project is to train a model to predict how Supreme Court nominees will vote on court cases if confirmed. 

We used three datasets -- information about nominees available at nomination time, their confirmation text hearings, and information about the future cases they hear and vote on.

## Dataset cleaning

There were three datasets used: 

- [Supreme Court Database (SCDB)](http://scdb.wustl.edu/): A database of case level attributes and a recording of justice votes, with detailed records stretching back to 1945
- [Supreme Court Justices Database](http://epstein.wustl.edu/research/justicesdata.html](http://epstein.wustl.edu/research/justicesdata.html): A database compiled by Lee Epstein of demographic data of all nominees to the Supreme Court 
- [Confirmation Hearing Transcripts](https://www.senate.gov/reference/Supreme_Court_Nomination_Hearings.htm): PDF transcripts of the confirmation hearings of all justices. Usable data stretched back to Harry Blackmun, in 1970

Raw PDF transcripts are contained in `nlp_approach/data/transcript`. Data cleaning occurs in `nlp_approach/parse_pdf.py`. That script first parsed the text using `pdftotext`, and then extracted every utterance by a justice using regular expressons. 

Nominee dataset was relatively clean, but contained many features that were either too sparse to use or were simply irrelevant for our purposes. These features were extracted in `demographic_approach/nominee_data_processing.py`

Finally, the SCDB data was cleaned and combined with the nominee data to make the final dataset. For each row representing a case-justice pair, we generated a column `justice_votes`, which was 1 if the justice voted in favor of the plaintiff and 0 otherwise. This occured in `demographic_approach/extract_scdb_data.py`.

## Feature set generation
This is how we generated our data. We would have included this in the python notebook but due to memory errors we had to run these through scripts on our local machines.

### Merge Justice and Case data

```
python demographic_approach/extract_scdb_data.py
```

### Basic 1-grams (bag of words)

```
python nlp_approach/ngram_feature_extraction.py
```

### n-grams with TF-IDF transform

```
python nlp_approach/ngram_feature_extraction_tfidf.py
```

### Word Embeddings

`nlp_approach/generate_mean_embeddings.ipynb`

## Model Training and Evaluation

This can be found and viewed in  `nominee_predict_models.ipynb`

## Authors

* Michael Fine, Jenny Huang, Chris Rohlicek


## Acknowledgments

* Thanks to Professor Ba for all his guidance!
