import requests
import streamlit as st

import pandas as pd
# from pprint import pprint

#These lines define the URLs and login credentials
MANAGER_URL = "https://10.0.0.20/rhn/manager/api"
MANAGER_LOGIN = "sumaadmin"
MANAGER_PASSWORD = "exadmin"

# Authenticate and get cookies
data = {"login": MANAGER_LOGIN, "password": MANAGER_PASSWORD}
response = requests.post(MANAGER_URL + '/auth/login', json=data, verify=False)
cookies = response.cookies

res2 = requests.get(MANAGER_URL + '/system/listActiveSystems', cookies=cookies, verify=False)
data = [(r['id'], r['name'], r['last_checkin'], r['last_boot']) for r in res2.json()['result']]
df = pd.DataFrame(data, columns=['id', 'name','last_checkin', 'last_boot'])
st.write("system data:")
st.dataframe(df)

