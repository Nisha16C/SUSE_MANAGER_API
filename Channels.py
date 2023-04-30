import requests
import streamlit as st
import pandas as pd
# from pprint import pprint
import plotly.graph_objs as go

#These lines define the URLs and login credentials
MANAGER_URL = "https://10.0.0.20/rhn/manager/api"
MANAGER_LOGIN = "sumaadmin"
MANAGER_PASSWORD = "exadmin"

# Authenticate and get cookies
data = {"login": MANAGER_LOGIN, "password": MANAGER_PASSWORD}
response = requests.post(MANAGER_URL + '/auth/login', json=data, verify=False)
cookies = response.cookies

# Get channel data and create DataFrame
res2 = requests.get(MANAGER_URL + '/channel/listAllChannels', cookies=cookies, verify=False)
# pprint(res2.json())
data = [(r['label'], r['systems']) for r in res2.json()['result']]
df = pd.DataFrame(data, columns=['Channel Label', 'Num Systems'])
# pprint(data)

# Display table using Streamlit
st.write("Channel data:")
st.dataframe(df)

# Create a graph using Plotly
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df['Channel Label'],
    y=df['Num Systems'],
    marker_color = 'rgb(0, 118, 5)'
))
fig.update_layout(title='Channel Labels vs. Systems', xaxis_title='Channels', yaxis_title='Systems')
st.plotly_chart(fig)

# Logout
requests.post(MANAGER_URL + '/auth/logout', cookies=cookies, verify=False)
