import requests

api_key = 'eaf68ffb413d707283399af330d02c3f'
city = 'London'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
print(response)
print(response.json())
print(f"Status code: {response.status_code}")
print(f"Response text: {response.text[:100]}...")  # Print first 100 chars of response