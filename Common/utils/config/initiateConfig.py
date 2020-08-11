import os
import yaml

from utils.config.singleton import Singleton

class Configurations(metaclass=Singleton):

    @staticmethod
    def loadConfig(configFile):
        with open(configFile, 'r') as stream:
            Configurations.configData = yaml.safe_load(stream)

    @staticmethod
    def getDbDetails():
        return Configurations.configData['database']

    @staticmethod
    def getPaths():
        return Configurations.configData['photoPath']

    @staticmethod
    def getExtensions():
        return [x.strip() for y in Configurations.configData['AllowedExtensions'] for x in y.split('|')]



if __name__ == '__main__':
    Configurations.loadConfig()
    print(Configurations.getDbDetails())
    print(Configurations.getPaths())
    print(Configurations.getExtensions())