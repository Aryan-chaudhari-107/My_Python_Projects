# If response code is 1XX: HOLD ON
# If response code is 2XX: HERE YOU GO
# If response code is 3XX: GO AWAY
# If response code is 4XX: YOU SCREWED UP
# If response code is 5XX: I SCREWED UP (for more you can visit httpstatuses.com)

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)