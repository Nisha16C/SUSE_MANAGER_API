import requests
import streamlit as st
import pandas as pd

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
data = [(r['label'], r['systems']) for r in res2.json()['result']]
df = pd.DataFrame(data, columns=['Channel Label', 'Num Systems'])

# Display table and chart using Streamlit
st.write("Channel data:")
st.dataframe(df)

st.write("Number of systems per channel:")
st.bar_chart(df.set_index('Channel Label'))
