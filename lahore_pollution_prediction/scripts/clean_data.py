import requests
from sqlalchemy import create_engine
import pandas as pd
# Connect to the database
engine = create_engine('sqlite:///air_quality.db')
# Read the data from the database
df = pd.read_sql("SELECT * FROM pollution", engine)
print(df.head())

# Clean the data (e.g., handle missing values)
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.sort_values("datetime")
df = df.drop_duplicates()
df = df.dropna()

df["hour"] = df["datetime"].dt.hour
df["day"] = df["datetime"].dt.day
df["month"] = df["datetime"].dt.month
df["day_of_week"] = df["datetime"].dt.dayofweek


import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(10, 6))
plt.plot(df["datetime"], df["pm2_5"])
plt.title("PM2.5 Over Time")
plt.show()