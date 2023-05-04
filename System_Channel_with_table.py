import streamlit as st
from xmlrpc.client import ServerProxy
import ssl
import pandas as pd

#These lines define the URLs and login credentials
MANAGER_URL = "https://10.0.0.20/rpc/api"
MANAGER_LOGIN = "sumaadmin"
MANAGER_PASSWORD = "exadmin"

# Create an SSL context and ServerProxy object for making API requests
context = ssl._create_unverified_context()
client = ServerProxy(MANAGER_URL, context=context)

# Authenticate with the API using the login credentials
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)

# Retrieve a list of available channels from the API
SYSTEMS = client.channel.listSoftwareChannels(key)
names1 = [d['parent_label'] for d in SYSTEMS]

# Retrieve a list of all registered systems from the API
systems = client.system.listActiveSystems(key)
names2 = [d['name'] for d in systems]
names3 = [int(d['id']) for d in systems]

# Define a Streamlit form for selecting a channel and system to update
with st.form(key='apply_channel_form'):
    channels_name = st.selectbox('Enter Channel Names', options=names1)
    system_id = st.selectbox('Select system id', options=names3)
    submit_button = st.form_submit_button(label='Change')

# If the form is submitted, update the base channel for the selected system
if submit_button:
    client.system.setBaseChannel(key, system_id, channels_name)
    st.success(f"Channel '{channels_name}' has been applied to the system '{system_id}'")

# Retrieve the updated list of systems from the API
systems = client.system.listActiveSystems(key)

# Create a table with the updated system IDs and channel names
data = {'System ID': [], 'System Name': []}
for system in systems:
    data['System ID'].append(int(system['id']))
    data['System Name'].append(system['name'])

df = pd.DataFrame(data)
st.write(df)

#logout
client.auth.logout(key)
