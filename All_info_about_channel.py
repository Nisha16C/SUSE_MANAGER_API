import requests
import streamlit as st
import pandas as pd

MANAGER_URL = "https://10.0.0.20/rhn/manager/api"
MANAGER_LOGIN = "sumaadmin"
MANAGER_PASSWORD = "exadmin"

data = {"login": MANAGER_LOGIN , "password": MANAGER_PASSWORD}
response = requests.post(MANAGER_URL + '/auth/login', json=data, verify=False)

cookies = response.cookies
res2 = requests.get(MANAGER_URL + '/channel/listAllChannels', cookies=cookies, verify=False)

data = []
for i in range(len(res2.json()['result'])):
    channel_id = res2.json()['result'][i]['id']
    channel_name = res2.json()['result'][i]['name']
    channel_label = res2.json()['result'][i]['label']
    num_systems = res2.json()['result'][i]['systems']
    providers = res2.json()['result'][i]['provider_name']
    packages = res2.json()['result'][i]['packages']
    arch_name = res2.json()['result'][i]['arch_name']
    data.append((channel_id,channel_name, channel_label, num_systems, providers, packages, arch_name ))

df = pd.DataFrame(data, columns=['id', 'channel_name', 'Channel Label', 'Num Systems', 'providers', 'packages', 'arch_name' ])

st.table(df)

requests.post(MANAGER_URL + '/auth/logout', cookies=cookies, verify=False)