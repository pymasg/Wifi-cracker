import streamlit as st
from wifipasswords import WifiPasswords

st.set_page_config(page_icon="python.ico", page_title="Wifi Cracker")
st.header(body="Wifi cracker", divider="rainbow")

code = st.text_input(label="", placeholder="Enter Code to use: ")

btn = st.button(label="Check")

if btn:
    if code == "#code1":
        try:
            wifi = WifiPasswords()
            password = wifi.get_currently_connected_passwords()[-1][1]

            st.success(body=f"Wifi passwords is **{password}**.", icon="🔥")
        except:
            st.warning("Please connect to a wifi to continue attack.")

    else:
        st.warning("Invalid code\nYour are not my owner.")
