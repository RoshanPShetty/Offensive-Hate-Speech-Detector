import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv('temp_file.csv')
df = df.str.replace('[^a-zA-Z]', ' ')
print(df)
