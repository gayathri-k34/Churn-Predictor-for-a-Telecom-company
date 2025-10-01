# encoders.py
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.freq_map_ = {}

    def fit(self, X, y=None):
        X = pd.Series(X.ravel())
        freq = X.value_counts(normalize=True)
        self.freq_map_ = freq.to_dict()
        return self

    def transform(self, X):
        X = pd.Series(X.ravel())
        return X.map(self.freq_map_).fillna(0).to_frame()
