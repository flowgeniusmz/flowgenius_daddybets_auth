import streamlit as st
from supabase import Client, create_client
from config import pagesetup as ps

st.set_page_config(page_title="DaddyBetsGPT", page_icon="👨‍💻", layout="wide")
ps.get_page_styling()
ps.display_background_image()


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)




client = create_client(supabase_key=st.secrets.supabase.api_key_admin, supabase_url=st.secrets.supabase.url)


username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Validate user against Supabase 'users' table
    response = client.table('users').select('*').eq('username', username).eq('password', password).execute()
    data = response.data
    if data:
        user = data[0]
        username = user['username']
        url = f"https://daddybetsgpt.com/chat.html?username={username}"
        nav_to(url=url)
    else:
        st.error("Unable to authenticate. Please try again.")
        



