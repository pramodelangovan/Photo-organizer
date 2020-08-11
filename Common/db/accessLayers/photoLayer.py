from db.models.photoModels import Paths

def addPaths(pathList):
    for path in pathList:
        addPath(path)

def addPath(path):
    if not Paths.objects(path=path):
        Paths(path=path).save()

