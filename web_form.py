import requests
import streamlit as st
import pandas as pd

MANAGER_URL = "https://10.0.0.20/rhn/manager/api"
MANAGER_LOGIN = "sumaadmin"
MANAGER_PASSWORD = "exadmin"

# Authenticate and get cookies
data = {"login": MANAGER_LOGIN, "password": MANAGER_PASSWORD}
response = requests.post(MANAGER_URL + '/auth/login', json=data, verify=False)
cookies = response.cookies

# Create the form using Streamlit
st.write("Enter the following details:")
channel_name = st.text_input("Channel Name")
num_systems = st.number_input("Number of Systems", min_value=1, step=1)
system_names = []
for i in range(num_systems):
    system_names.append(st.text_input(f"System Name #{i+1}"))
submit_button = st.button("Submit")

# When the submit button is clicked
if submit_button:
    # Check if the channel exists
    res1 = requests.get(MANAGER_URL + f'/channel/details?label={channel_name}', cookies=cookies, verify=False)
    if res1.status_code != 200:
        st.write(f"Error: Channel '{channel_name}' not found.")
    else:
        # Add each system to the channel
        system_ids = []
        for system_name in system_names:
            # Check if the system exists
            res2 = requests.get(MANAGER_URL + f'/system/details?name={system_name}', cookies=cookies, verify=False)
            if res2.status_code != 200:
                st.write(f"Error: System '{system_name}' not found.")
            else:
                # Add the system to the channel
                system_id = res2.json()['result']['id']
                system_ids.append(system_id)
        if len(system_ids) == num_systems:
            channel_id = res1.json()['result']['id']
            res3 = requests.post(MANAGER_URL + f'/channel/addSystemsToChannel', json={'channelId': channel_id, 'systemIds': system_ids}, cookies=cookies, verify=False)
            if res3.status_code == 200:
                st.write(f"The following systems have been added to channel '{channel_name}': {', '.join(system_names)}.")
            else:
                st.write(f"Error: {res3.text}")
