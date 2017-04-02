import json
from os.path import join


class CBase:

    def __init__(self):
        # read json
        fileNameConfig = join('Common', 'configGlobal.json')
        with open(fileNameConfig) as data_file:
            configGlobal = json.load(data_file)

        # address config file
        className = self.__class__.__name__[1:]
        configPath = \
            join\
                (
                    className, configGlobal['config'][0]['subfolder'],
                    configGlobal['config'][0]['initiFileName'] + className +
                    "." + configGlobal['config'][0]['format']
                )
        # load config file
        fileNameConfig = join(configPath)
        with open(fileNameConfig) as data_file:
            self.config = json.load(data_file)

        # address doc path
        self.docPath = \
            join \
                (
                   className, configGlobal['doc'][0]['subfolder'],
                   configGlobal['doc'][0]['initiFileName'] + className +
                   "." + configGlobal['doc'][0]['format']
                )

        # address test path
        self.testPath = \
            join \
                    (
                    className, configGlobal['test'][0]['subfolder'],
                    configGlobal['test'][0]['initiFileName'] + className +
                    "." + configGlobal['test'][0]['format']
                )