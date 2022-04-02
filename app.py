import streamlit as st
import datetime
import requests

'''
# TaxiFareModel
'''


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
