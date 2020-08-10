import os
import json
from datetime import datetime

import setUp

from exifProcessor import getExifData, getGPSData
from DB.DBModels.PhotoModels import Paths, Photos, ExifData, PhotoDetails

def getAllImagesFromPaths():
    fileList = list()
    for path in Paths.objects:
        getImagesFromPath(path, fileList)
    getPhotoDetails()

def getImagesFromPath(path, fileList):
    for root, _, files in os.walk(path.path):
        for name in files:
            if not Photos.objects(path = path, photoName = name, photoPath = root):
                Photos(path = path, photoName = name, photoPath = root).save()

def getPhotoDetails():
    for photo in Photos.objects:
        exifData, rawExif = getExifData(os.path.join(photo.photoPath, photo.photoName))
        if not ExifData.objects(photo = photo):
            ExifData(photo=photo, exifData=exifData).save()

        if not PhotoDetails.objects(photo = photo):
            photoGpsInfo = getGPSData(rawExif)

            photoDetails = PhotoDetails()
            photoDetails.photo = photo
            photoDetails.dateInfo = datetime. strptime(exifData['Image']['DateTime'], '%Y:%m:%d %H:%M:%S')
            photoDetails.geoData = photoGpsInfo
            photoDetails.deviceModel = exifData['Image']['Model']
            photoDetails.save()

if __name__ == "__main__":
    getAllImagesFromPaths()