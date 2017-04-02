from Common.CBase import CBase
from os.path import join
import csv
from pandas import read_csv

class CData(CBase):

    # CTOR
    def __init__(self):
        CBase.__init__(self)
        self.pathPic = join(self.pathData, self.config['fileNamePic'])
        self.pathClass = join(self.pathData, self.config['fileNameClass'])
        # pic
        self.ReadData(self.pathPic, self.pathClass, self.config)



    def ReadData(self, pathPic, pathClass, config):
        dataPic = read_csv(pathPic, sep=',', header=None, skiprows = 1)
        dataClass = read_csv(pathClass, sep=',', header=None, skiprows=1)
        # manage training-set test-set
        self.pic = dataPic.get_values()
        self.classification = dataPic.get_values()
        dummy=1;

