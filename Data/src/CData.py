from Common.CBase import CBase
from Common.EnumBool import EnumBool
from os.path import join
import numpy as np
import pickle

class CData(CBase):

    # CTOR
    def __init__(self):
        CBase.__init__(self)
        self.pathPic = join(self.pathes["data"], self.config['fileNamePic'])
        self.pathClass = join(self.pathes["data"], self.config['fileNameClass'])
        # pic
        if self.config["refresh"] == EnumBool.true.value:
            self.ReadData(self.pathPic, self.pathClass, self.config)
        else:
            inputFile = join(self.pathes["data"], self.config["bufferTest"])
            with open(inputFile, 'rb') as handle:
                self.test = pickle.load(handle)
            inputFile = join(self.pathes["data"], self.config["bufferTraining"])
            with open(inputFile, 'rb') as handle:
                self.training = pickle.load(handle)


    def ReadData(self, pathPic, pathClass, config):

        dataPic = np.loadtxt(pathPic, delimiter = config["delimiter"], skiprows = int(config["skipRows"]))
        dataClass = np.loadtxt(pathClass, delimiter = config["delimiter"], skiprows = int(config["skipRows"]))

        # index classesnp.reshape(picTest1,  [picTest1.shape[0], dim, dim])
        index1 = [index1 for index1, value in enumerate(dataClass) if value == 1]
        index0 = [index0 for index0, value in enumerate(dataClass) if value == 0]

        # manage training-set test-set
        incTest = int(1.0 / float(config['ratioTest']))
        indexTest1 = index1[::incTest]
        indexTest0 = index0[::incTest]

        picTest0 = dataPic[indexTest0,:]
        picTest1 = dataPic[indexTest1,:]
        iTrain0 = [element for i, element in enumerate(index0) if i not in indexTest0]
        iTrain1 = [element for i, element in enumerate(index1) if i not in indexTest1]
        pic0 = dataPic[iTrain0, :]
        pic1 = dataPic[iTrain1, :]

        # reshape
        dim = int(np.floor(np.sqrt(pic0.shape[1])))
        test = \
            {
            "pic0":np.reshape(picTest0, [picTest0.shape[0], dim, dim]),
                "pic1":np.reshape(picTest1,  [picTest1.shape[0], dim, dim])
            }

        self.test = test
        # buffer
        outFile = join(self.pathes["data"], config["bufferTest"])
        with open(outFile, 'wb') as handle:
            pickle.dump(test, handle, protocol = pickle.HIGHEST_PROTOCOL)

        training = \
            {
                "pic0": np.reshape(pic0, [pic0.shape[0], dim, dim]),
                "pic1": np.reshape(pic1, [pic1.shape[0], dim, dim])
            }
        self.training = training
        outFile = join(self.pathes["data"], config["bufferTraining"])
        with open(outFile, 'wb') as handle:
            pickle.dump(training, handle, protocol = pickle.HIGHEST_PROTOCOL)