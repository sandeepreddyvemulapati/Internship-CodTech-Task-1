import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Replace with your own OpenWeatherMap API key
API_KEY = "2ed684e5a4b91aa55f0d404ac7b4c235"
CITY = "Anantapur"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from OpenWeatherMap
response = requests.get(URL)
data = response.json()

# Extract relevant data
dates = []
temperatures = []
humidities = []

for entry in data['list']:
    dt_txt = entry['dt_txt']
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']
    
    # Convert to datetime object
    dt = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
    
    dates.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)

# Plotting
plt.figure(figsize=(14, 6))

# Temperature Line Plot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temperatures, color='red')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

# Humidity Line Plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidities, color='blue')
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
