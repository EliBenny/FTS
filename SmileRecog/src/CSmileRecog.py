from Common.CBase import CBase
from Data.src import CData

import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

class CSmileRecog(CBase):

    # CTOR
    def __init__(self):
        CBase.__init__(self)
        self.data = CData()
