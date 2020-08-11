import os
import sys

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
commonPath = os.path.join(root, 'Common')
configFile = os.path.join(root, 'config.yaml')
sys.path.insert(0, commonPath)

from utils.config.initiateConfig import Configurations
from mongoengine import *

Configurations.loadConfig(configFile)

dbConfig = Configurations.getDbDetails()

connect(db = dbConfig['dbName'], host = dbConfig['host'], port = int(dbConfig['port']), username = dbConfig['username'],
        password = dbConfig['password'], authentication_source = dbConfig['dbName'])
