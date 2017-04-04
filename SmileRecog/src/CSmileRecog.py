from Common.CBase import CBase
from Data.src.CData import CData

import numpy as np
import pandas
import keras
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K


class CSmileRecog(CBase):

    # CTOR
    def __init__(self):
        CBase.__init__(self)
        self.DataPreprocessing()

    def Build(self):
        y = keras.utils.to_categorical(self.y * self.w, int(self.config["classCount"]))
        yTest = keras.utils.to_categorical(self.yTest * self.wTest, int(self.config["classCount"]))
        inputShape = (self.x.shape[1], self.x.shape[2], 1)

        model = Sequential()
        model.add(Conv2D(5, kernel_size = (4, 4), activation = 'relu', input_shape = inputShape))
        model.add(Conv2D(5, (4, 4), activation = 'relu'))
        model.add(MaxPooling2D(pool_size = (8, 8)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(int(self.config["batchSize"]), activation = 'relu'))
        model.add(Dropout(0.5))
        model.add(Dense(int(self.config["classCount"]), activation = 'softmax'))

        model.compile\
            (
                loss = keras.losses.categorical_crossentropy,
                optimizer = keras.optimizers.Adadelta(),
                metrics = ['accuracy']
            )

        model.fit\
            (
                self.x, y, batch_size = int(self.config["batchSize"]),
                epochs = int(self.config["epochs"]),
                verbose = int(self.config["verbose"]),
                validation_data=(self.xTest, yTest)
            )

        score = model.evaluate(self.xTest, yTest, verbose = int(self.config["verbose"]))
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

    def DataPreprocessing(self):
        data = CData()
        # training set
        training1 = data.training["pic1"]
        training0 = data.training["pic0"]
        d = (float(training0.shape[0]) + float(training1.shape[0]))
        w1 = float(training0.shape[0]) / d
        w0 = float(training1.shape[0]) / d
        x = np.concatenate((training1, training0), axis = 0) / float(self.config["grayLevel"])
        self.x = np.reshape(x, [x.shape[0], x.shape[1], x.shape[2], 1])
        y = \
            np.concatenate\
                (
                    (np.ones([training1.shape[0], 1], 'float'),
                     np.zeros([training0.shape[0], 1], 'float')), axis = 0
                )
        self.y = np.reshape(y, [y.shape[0], 1])
        w = \
            np.concatenate\
                (
                    (w1 * np.ones([training1.shape[0], 1], 'float'),
                    w0 * np.zeros([training0.shape[0], 1], 'float')), axis = 0
                )
        self.w = np.reshape(w, [w.shape[0], 1])

        # test set
        test1 = data.test["pic1"]
        test0 = data.test["pic0"]
        d = (float(test0.shape[0]) + float(test1.shape[0]))
        w1 = float(test0.shape[0]) / d
        w0 = float(test1.shape[0]) / d
        xTest = np.concatenate((test1, test0), axis = 0)  / float(self.config["grayLevel"])
        self.xTest = np.reshape(xTest, [xTest.shape[0], xTest.shape[1], xTest.shape[2], 1])
        yTest = \
           np.concatenate(( np.ones([test1.shape[0], 1], 'float'), np.zeros([test0.shape[0], 1], 'float') ), axis = 0)
        self.yTest = np.reshape(yTest, [yTest.shape[0], 1])
        wTest =  \
            np.concatenate\
                (
                    (w1 * np.ones([test1.shape[0], 1], 'float'),
                    w0 * np.zeros([test0.shape[0], 1], 'float')), axis = 0
                )
        self.wTest = np.reshape(wTest, [wTest.shape[0], 1])






