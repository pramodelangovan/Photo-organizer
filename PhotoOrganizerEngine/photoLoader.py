import os
import json

import setUp
import exifread
from photos.models import FileLocations

# FileLocations(path='/media/disks/photos-disks/Photos').save()

def getAllImagesFromPaths():
    fileList = list()
    fileLocations = FileLocations.objects.all()
    for fileLocation in fileLocations:
        fileList = getImagesFromPath(fileLocation.path, fileList)
    
    getExifdata(fileList[:2])
        
def getImagesFromPath(path, fileList):
    for root, _, files in os.walk(path): 
        for name in files:
            fileList.append(os.path.join(root, name))
    return fileList

def getExifdata(fileList):
    for image in fileList:
        exif = get_exif(image)
        print("DateTime:", exif['Image DateTime'])
        print("LatLong:", getGPS(exif))
        
def _convert_to_degress(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


def getGPS(tags):
    if 'GPS GPSLatitude' in tags:
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != 'N':
                lat_value = -lat_value
        else:
            return {}
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != 'E':
                lon_value = -lon_value
        else:
            return {}
        return {'latitude': lat_value, 'longitude': lon_value}
    return {}

def get_exif(fileName):
    with open(fileName, 'rb') as img:
        tags = exifread.process_file(img)
    return tags


if __name__ == "__main__":
    getAllImagesFromPaths()