from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

# import jwt
# import requests
# import json
# from time import time
  
  
# # Enter your API key and your API secret
# API_KEY = 'XyaHSJC_SbSAQYHtvKnk3g'
# API_SEC = '8KOBnBQ2rHktKp7zkY0qlj74gBAz5ZPtUPiQ'
  
# # create a function to generate a token
# # using the pyjwt library
  
  
# def generateToken():
#     token = jwt.encode(
  
#         # Create a payload of the token containing
#         # API Key & expiration time
#         {'iss': API_KEY, 'exp': time() + 5000},
  
#         # Secret used to generate token signature
#         API_SEC,
  
#         # Specify the hashing alg
#         algorithm='HS256'
#     )
#     return token
  
  
# # create json data for post requests
# meetingdetails = {"topic": "The title of your zoom meeting",
#                   "type": 2,
#                   "start_time": "2019-06-14T10: 21: 57",
#                   "duration": "45",
#                   "timezone": "Europe/Madrid",
#                   "agenda": "test",
  
#                   "recurrence": {"type": 1,
#                                  "repeat_interval": 1
#                                  },
#                   "settings": {"host_video": "true",
#                                "participant_video": "true",
#                                "join_before_host": "False",
#                                "mute_upon_entry": "False",
#                                "watermark": "true",
#                                "audio": "voip",
#                                "auto_recording": "cloud"
#                                }
#                   }
  
# # send a request with headers including
# # a token and meeting details
  
  
# def createMeeting():
#     headers = {'authorization': 'Bearer ' + generateToken(),
#                'content-type': 'application/json'}
#     r = requests.post(
#         f'https://api.zoom.us/v2/users/me/meetings',
#         headers=headers, data=json.dumps(meetingdetails))
  
#     print("\n creating zoom meeting ... \n")
#     # print(r.text)
#     # converting the output into json and extracting the details
#     y = json.loads(r.text)
#     global join_URL
#     join_URL = y["join_url"]
#     global meetingPassword
#     meetingPassword = y["password"]
    
  
#     print(
#         f'\n here is your zoom meeting link {join_URL} and your \
#         password: "{meetingPassword}"\n')

mode = [
    ("ONLINE",'ONLINE'),
    ("OFFLINE", 'OFFLINE')
]

status_field = [
    ("on going",'on going'),
]


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class EventName(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    eventtype = models.ForeignKey(EventName, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    date  = models.DateField()
    start_time = models.TimeField(help_text="Eg time: 06:00:00 means 6 am")
    end_time = models.TimeField(help_text="Eg time: 18:00:00 means 6 pm")
    mode = models.CharField(choices=mode,max_length = 8, blank=True, null=True)
    meet_url = models.URLField(max_length = 2083, blank=True, null = True)
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE,blank=True, null=True)
    guest = models.CharField(max_length=200,blank=True, null=True)
    convenor = models.CharField(max_length=200,blank=True, null=True)
    banner = ResizedImageField(size=[1000, 400],upload_to='banners/')


    def __str__(self):
        return f"{self.name}"
    
   
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.name))



