import streamlit as st
import requests
import datetime

# TaxiFareModel Front
st.title('Taxi Fare Prediction')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# Asking for user inputs (date, time, coordinates, passenger count)
st.markdown("## Please input the ride details:")

# Input fields
date_time = st.date_input("Select Date", value=datetime.date.today())
time_input = st.time_input("Select Time", value=datetime.time(12, 0))

pickup_longitude = st.number_input('Pickup Longitude', value=40.7128)
pickup_latitude = st.number_input('Pickup Latitude', value=-74.0060)
dropoff_longitude = st.number_input('Dropoff Longitude', value=40.7831)
dropoff_latitude = st.number_input('Dropoff Latitude', value=-73.9712)
passenger_count = st.number_input('Passenger Count', value=1, min_value=1)

# Combining date and time into a single string
pickup_datetime = f"{date_time} {time_input}"

# Preparing the dictionary for the API request
data = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

# URL of the API (Le Wagon API as default)
api_url = 'https://taxifare.lewagon.ai/predict'

# When user clicks the button, send the data to the API and get the prediction
if st.button('Predict Fare'):
    try:
        response = requests.get(api_url, params=data)
        response.raise_for_status()  # Raise an error if the API call is unsuccessful
        prediction = response.json().get('fare', 'No fare returned')

        # Display the prediction result
        st.write(f"The predicted fare is: ${prediction:.2f}")

    except requests.exceptions.RequestException as e:
        st.write(f"API request failed: {e}")
    except ValueError:
        st.write("Invalid response format (not JSON).")

st.markdown('''
## Steps for the Taxi Fare Prediction:
1. The user inputs the ride details such as date, time, coordinates, and passenger count.
2. The application sends these inputs to the prediction API (in this case, Le Wagon API).
3. The fare prediction is retrieved and displayed to the user.
''')
