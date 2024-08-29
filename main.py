import streamlit as st
import requests

st.set_page_config(layout="wide", page_title="Daily Dashboard")
col1, col2, col3 = st.columns([1,3,1])

col2.title("Daily Dashboard")
col3.title("Calendar and To-Do List")

api_key = "40caf51a9f31f946b01e55a07df484f3"
lat = 40
lon = -73
api_url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial")


response = requests.get(api_url)
api_data = response.json()

col1.title("Weather")
col1.write(f'{api_data["main"]["temp"]}°')
col1.write(f'{api_data["weather"][0]["description"]}')

col1.image(f'https://openweathermap.org/img/wn/{api_data["weather"][0]["icon"]}@2x.png',width=50,)