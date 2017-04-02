from Common.CBase import CBase
from os.path import join
from pandas import read_csv
import numpy as np

class CData(CBase):

    # CTOR
    def __init__(self):
        CBase.__init__(self)
        self.pathPic = join(self.pathData, self.config['fileNamePic'])
        self.pathClass = join(self.pathData, self.config['fileNameClass'])
        # pic
        self.ReadData(self.pathPic, self.pathClass, self.config)



    def ReadData(self, pathPic, pathClass, config):
        dataPic = read_csv(pathPic, sep = ',', header = None, skiprows = 1)
        dataClass = read_csv(pathClass, sep = ',', header = None, skiprows = 1)
        classification = dataClass.get_values()
        # manage training-set test-set
        incTest = int(1.0 / float(config['ratioTest']))

        pic = dataPic.get_values()
        pic0 = pic[classification == 0]

        picTest0 = pic0[np.arange(0, pic0.size, incTest)]
        picTrain0 = pic0[~np.arange(0, pic0.size, incTest)]


        pic1 = pic[classification == 1]

        picTest1 = pic1[np.arange(0, pic1.size, incTest)]
        picTrain1 = pic1[~np.arange(0, pic1.size, incTest)]
        self.trainingSet.pic1 = np.reshape(picTrain1, (48, 48), 'C')


        dummy=1;

