import requests
from datetime import datetime

MY_LAT=41.299496
MY_LONG=69.240074

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

reponse = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
reponse.raise_for_status()
data=reponse.json()
sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now=datetime.now()

print(time_now.hour)







