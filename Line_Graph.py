import requests
import streamlit as st
import pandas as pd
import altair as alt

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

# Create line chart
chart = alt.Chart(df).mark_line().encode(
    x='Channel Label',
    y='Num Systems'
)

# Display chart using Streamlit
st.write("Channel data:")
st.altair_chart(chart)

# Logout
requests.post(MANAGER_URL + '/auth/logout', cookies=cookies, verify=False)
