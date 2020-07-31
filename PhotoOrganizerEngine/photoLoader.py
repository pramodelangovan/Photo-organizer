import os
import json

import setUp
import PIL.Image
import PIL.ExifTags
from GPSPhoto import gpsphoto

from photos.models import FileLocations

# FileLocations(path='/media/disks/photos-disks/Photos').save()

def getAllImagesFromPaths():
    fileList = list()
    fileLocations = FileLocations.objects.all()
    for fileLocation in fileLocations:
        fileList = getImagesFromPath(fileLocation.path, fileList)
    
    getExifdata(fileList[:1])
        
def getImagesFromPath(path, fileList):
    for root, dirs, files in os.walk(path): 
        for name in files:
            fileList.append(os.path.join(root, name))
    return fileList

def getExifdata(fileList):
    for image in fileList:
        data = gpsphoto.getGPSData(image)
        print(data)
        print(data['Latitude'], data['Longitude'])
    #     img = PIL.Image.open(image)
    #     exif = { PIL.ExifTags.TAGS[k]: str(v) for k, v in img._getexif().items() if k in PIL.ExifTags.TAGS }
    #     gpsinfo = {}
    #     for key in exif['GPSInfo'].keys():
    #         decode = ExifTags.GPSTAGS.get(key,key)
    #         gpsinfo[decode] = exif['GPSInfo'][key]
    #     print(gpsinfo)
        

if __name__ == "__main__":
    getAllImagesFromPaths()