import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
import pydeck as pdk


st.set_page_config(layout="wide")

'''
# alestamm TaxiFareModel
'''

def map(lat, lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/alestamm/cl1i42zfc006o15ry1fzqr0ag",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        ))

st.write(map(40.6650, -73.7821, 12))

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

"Please enter:"

p_date = st.date_input("Date:", datetime.datetime(2019, 7, 6, 10, 10, 10))

p_time = st.time_input('Time', datetime.time(8, 45, 10))

p_long = st.number_input("Pickup Longitude:", min_value=1.0, step=0.1)

p_lat =  st.number_input("Pickup latitude:", min_value=1.0, step=0.1)

d_long = st.number_input("Dropoff Longitude:", min_value=1.0, step=0.1)

d_lat = st.number_input("Dropoff Latitude:", min_value=1.0, step=0.1)

p_count = int(st.number_input("Passenger Count:", min_value=1, step=1))





# Let's build a dictionary containing the parameters for our API..."

payload = {
    "pickup_datetime": str(datetime.datetime.combine(p_date, p_time)),
    "pickup_longitude": p_long,
    "pickup_latitude": p_lat,
    "dropoff_longitude": d_long,
    "dropoff_latitude": d_lat,
    "passenger_count": p_count
}

# Let's call our API using the `requests` package..."

url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url, params=payload).json()

# Let's retrieve the prediction from the **JSON** returned by the API..."

prediction = round(response['fare'], 2)

## Finally, we can display the prediction to the user

st.write(f"Your predicted fare is:{prediction}")
