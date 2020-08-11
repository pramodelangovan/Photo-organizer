import os
import sys
from mongoengine import *

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
commonPath = os.path.join(root, 'Common')
configFile = os.path.join(root, 'config.yaml')
sys.path.insert(0, commonPath)

from utils.config.initiateConfig import Configurations
from db.accessLayers.photoLayer import addPaths

Configurations.loadConfig(configFile)
dbConfig = Configurations.getDbDetails()
paths = Configurations.getPaths()

connect(db = dbConfig['dbName'], host = dbConfig['host'], port = int(dbConfig['port']), username = dbConfig['username'],
        password = dbConfig['password'], authentication_source = dbConfig['dbName'])

addPaths(paths)