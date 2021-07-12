import numpy as np
import pandas as pd


def get_portfolio(train: pd.DataFrame):
    return np.ones(train.shape[1]) / train.shape[1]
