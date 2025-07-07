import streamlit as st
from streamlit_tags import st_tags
import time
from serverNew import *

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Server Side</h1>", unsafe_allow_html=True)

Bool1 = False
val1 = val2 = 0
with st.container(height=450):
    con1, con2, con3 = st.columns([2,3,1.5], gap="large")
    devices = 0
    loop = 0
    preDATA = []
    with con1:
        with st.form("my_form1"):
            st.subheader("Configurations")
            devices = st.selectbox('How many devices you want to connect?',(2, 3, 4, 5))
            loop = st.selectbox('How many loops you want to run?',(1, 2, 3, 4, 5))
            preDATA = [loop]
            val1 = st.form_submit_button('Submit')

    # This is outside the form
    with con2:
        keyword = st_tags(label='### Enter Client IPs :', text='Press enter to add more', value=[], suggestions=[], maxtags = devices, key='2')
        i=0
        for client in keyword:
            st.markdown(f"Client {i}: {client}")
            i=i+1
        val2 = st.button('Submit')
        # print(val2)
        
    with con3:
        st.subheader("Server IP :")
        Serverip = wlan_ip()
        PORT = 5555
        st.subheader(Serverip)
        st.subheader("Port No:")
        st.subheader(PORT)
        st.metric(label='Number of Clients :', value=devices)
        st.metric(label='Number of Loops :', value=loop)
      
         
with st.container():
    if st.button('Start Server',disabled=False if val2 == True else True):
        for i in range(loop):
            #step1
            st.info(f'Loop {i+1}')
            loaded_models =  receive_models_from_clients(devices)
            
            #step2
            st.info('Current Model:')
            st.code(f"{i} => {loaded_models}")
            print(f"{i} => {loaded_models}")
            
            #step3
            stacking_model = modelAggreation(loaded_models, devices)
            st.success(f"Aggreation of model done successfully.", icon="✅")

            #step3
            model_bytes = pickle.dumps(stacking_model)
            model_share(model_bytes, keyword)
            st.success(f"Aggreated model sharing done successfully.", icon="✅")
            
        

        




















# for i in range(loop):
#     progress_text = "Operation in progress. Please wait."
#     my_bar = st.progress(0, text=progress_text)

#     for percent_complete in range(100):
#         time.sleep(0.05)
#         my_bar.progress(percent_complete + 1, text=progress_text)
#     time.sleep(1)

#     st.write(f"loop:{i}")
#     my_bar.empty()



# import streamlit as st

# col1, col2, col3 = st.columns(3, gap=("large"))

# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")
