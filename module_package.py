# import msg.email # 모듈 이름 = 파일 이름
# import msg.sms

from msg import email
from msg import sms

e = email.Email()
s = sms.SMS()

e.send("woodawon1234@gmail.com", "woodada5678@gmail.com", "잘 지내?")
s.send("010-1234-1234", "010-5678-5678", "응 잘 지내")
s.ping("010-2343-2243")

# geopy 패키지 가져오기
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent = "my-app")
# location = geolocator.geocode("Seoul, Korea")
# print(location.raw)