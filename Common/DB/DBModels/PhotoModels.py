from mongoengine import *

connect('photoDB', username='pramod', password='@Sarathy92',  authentication_source='photoDB')


class Paths(Document):
    path = StringField(required=True)
    active = BooleanField(default=True)

class Photos(Document):
    path = ReferenceField(Paths, reverse_delete_rule=CASCADE)
    photoName = StringField(required=True)
    photoPath = StringField(required=True)

class Thumbnails(Document):
    photo = ReferenceField(Photos, reverse_delete_rule=CASCADE)
    thumbnail1 = StringField(max_length=1024, required=True)
    thumbnail2 = StringField(max_length=1024, required=True)
    thumbnail3 = StringField(max_length=1024, required=True)

class ExifData(Document):
    photo = ReferenceField(Photos, reverse_delete_rule=CASCADE)
    exifData =  DictField()

class PhotoDetails(Document):
    photo = ReferenceField(Photos, reverse_delete_rule=CASCADE)
    dateInfo = DateTimeField()
    geoData = DictField()
    deviceModel = StringField(max_length=256, required=True)