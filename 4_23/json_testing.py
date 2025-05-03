import json

# JSON data as a multi-line string
json_data = '''
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.85,
    "feels_like": 281.94,
    "temp_min": 281.51,
    "temp_max": 284.01,
    "pressure": 1019,
    "humidity": 85,
    "sea_level": 1019,
    "grnd_level": 1015
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.06,
    "deg": 0
  },
  "clouds": {
    "all": 13
  },
  "dt": 1745455725,
  "sys": {
    "type": 1,
    "id": 1414,
    "country": "GB",
    "sunrise": 1745469938,
    "sunset": 1745521877
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
'''

weather_data = json.loads(json_data)

print(weather_data)
