import requests
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

#cords of any city in this case I am using the coordinates of lahore
LAT = 31.5204
LON = 74.3587

API_KEY = "2ca6683871594f02986d09860936fa30"

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
response = requests.get(url)
data = response.json()

# Extracting relevant data
pollution = data['list'][0]

row = {
    "datetime": datetime.now(),
    "aqi": pollution["main"]["aqi"],
    "pm2_5": pollution["components"]["pm2_5"],
    "pm10": pollution["components"]["pm10"],
    "no2": pollution["components"]["no2"],
    "o3": pollution["components"]["o3"],
    "co": pollution["components"]["co"]
}#LKU

df = pd.DataFrame([row])
# Save to database
engine = create_engine('sqlite:///air_quality.db')
df.to_sql("pollution", engine, if_exists="append", index=False)#LKU
print("Data collected and stored in database.")