import exifread
from PIL.ExifTags import TAGS, GPSTAGS

exifData = {}
rawExif = None

def getExifData(photoPath):
    with open(photoPath, 'rb') as img:
        rawExif = exifread.process_file(img, strict=True)
        for key, value in rawExif.items():
            _getTag(key, value)
        if not 'GPS' in exifData:
            exifData['GPS'] = {}
    return exifData, rawExif

def _getTag(key, value):
    try:
        if not key in ['MAKER', "JPEGThumbnail"]:
            header = key.split(' ')
            if not header[0] in exifData:
                exifData[header[0]] = {}
            if not 'GPS' in key:
                exifData[header[0]].update({TAGS.get(value.tag, header[1]) : value.printable})
            else:
                exifData[header[0]].update({GPSTAGS.get(value.tag, header[1]) : value.printable})
    except AttributeError as ae:
        pass

def getGPSData(tags):
    if 'GPS GPSLatitude' in tags:
        latitude = tags.get('GPS GPSLatitude')
        latitudeRef = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitudeRef = tags.get('GPS GPSLongitudeRef')
        if latitude:
            latValue = converToDegrees(latitude)
            if latitudeRef.values != 'N':
                latValue = -latValue
        else:
            return {}
        if longitude:
            lonValue = converToDegrees(longitude)
            if longitudeRef.values != 'E':
                lonValue = -lonValue
        else:
            return {}
        return {'latitude': latValue, 'longitude': lonValue}
    return {}

def converToDegrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


if __name__ == '__main__':
    getData()