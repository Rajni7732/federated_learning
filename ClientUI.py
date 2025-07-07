

import streamlit as st
from streamlit_tags import st_tags
import time
from clientNew import *
import random

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Client Side</h1>", unsafe_allow_html=True)

Bool1 = False
val1 = val2 = 0
with st.container(height=360):
    con1, con2, con3 = st.columns([2,3,1.5], gap="large")
    devices = 0
    loop = 0
    preDATA = []
    with con1:
        with st.form("my_form1"):
            st.subheader("Configurations")
            st.write(f'How many devices you want to connect:')
            st.info("1 (By defalut for client)")
            loop = st.selectbox('How many loops you want to run?',(None, 1, 2, 3, 4, 5))
            #preDATA = [loop]
            val1 = st.form_submit_button('Submit')

    # This is outside the form
    with con2:
        Bool = False
        keyword = st_tags(label='### Enter Server IPs :', text='Press enter to add more', value=[], suggestions=[], maxtags = 1, key='2')
        print(keyword)
        if keyword:
            st.info(f"Server Ip : {keyword[0]}")
            Bool = True
        print(False if Bool == True else True)
        val2 = st.button('Submit',disabled=False if Bool == True else True)
        # print(val2)
        
    with con3:
        Serverip = wlan_ip()
        PORT = 5555

        st.info(f"Client IP : {Serverip}", icon="ℹ")
        st.info(f"Port No: {PORT}", icon="ℹ")
        st.info(f"Number of Server: {1}", icon="ℹ")
        st.info(f"Number of Loops: {loop}", icon="ℹ")
      
         
with st.container():
    col1,col2,col3 = st.columns(3)
    if col2.button('Start Client',disabled=False if val2 == True else True):
        # Your's IP address
        YOUR_IP = "0.0.0.0"
        YOUR_PORT = 5555

        # Server's IP address
        SERVER_HOST = keyword[0] #"192.168.80.28" 
        SERVER_PORT = 5555

        # Model Path
        MODEL_PATH = ".\model\pretrained_model.pkl"
        DATABASE_DIR = "database"

        # Couter
        COUNTER = 1

        FILE_DIR = os.listdir(DATABASE_DIR)       
        
        random.shuffle(FILE_DIR) # Suffling FILE_DIR

        for file in FILE_DIR:
            #step1
            st.info(f'Loop {COUNTER}')
            #COUNTER = COUNTER + 1

            FILE_PATH = os.path.join(DATABASE_DIR, file)
            print(FILE_PATH)
            st.success(FILE_PATH)
            
            #step2
            with st.spinner(f"Local model creating..."):
                MODEL_BYTES, X_train, X_test, y_train, y_test =  model_train(FILE_PATH, COUNTER)
                time.sleep(3)
            st.success(f"Local model training done successfully.", icon="✅")

            #step3
            with st.spinner(f"Waiting for share model..."):
                model_share(MODEL_BYTES, SERVER_HOST, SERVER_PORT)
            st.success(f"Model shared successfully.", icon="✅")
            
            with st.spinner(f"Waiting for New Model..."):
                waitingFornewModel(YOUR_IP, YOUR_PORT, MODEL_PATH)
                #time.sleep(3)
            st.success(f"New Model Recevied successfully.", icon="✅")

            with st.spinner(f"Waiting for Model Evolution..."):
                modelEvolution(X_train, y_train, X_test, y_test, MODEL_PATH)
                time.sleep(3)
            st.success(f"Model Evolution done successfully.", icon="✅")

            if COUNTER == loop:
                break
            
            COUNTER += 1
            
        

        




















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


# import streamlit as st
# from streamlit_tags import st_tags
# import time
# from clientNew import *

# st.set_page_config(layout="wide")

# st.markdown("<h1 style='text-align: center;'>Client Side</h1>", unsafe_allow_html=True)

# Bool1 = False
# val1 = val2 = 0
# with st.container(height=360):
#     con1, con2, con3 = st.columns([2,3,1.5], gap="large")
#     devices = 0
#     loop = 0
#     preDATA = []
#     with con1:
#         with st.form("my_form1"):
#             st.subheader("Configurations")
#             st.write(f'How many devices you want to connect:')
#             st.info("1 (By defalut for client)")
#             loop = st.selectbox('How many loops you want to run?',(None, 1, 2, 3, 4, 5))
#             #preDATA = [loop]
#             val1 = st.form_submit_button('Submit')

#     # This is outside the form
#     with con2:
#         Bool = False
#         keyword = st_tags(label='### Enter Client IPs :', text='Press enter to add more', value=[], suggestions=[], maxtags = 1, key='2')
#         print(keyword)
#         if keyword:
#             st.info(f"Server Ip : {keyword[0]}")
#             Bool = True
#         print(False if Bool == True else True)
#         val2 = st.button('Submit',disabled=False if Bool == True else True)
#         # print(val2)
        
#     with con3:
#         Serverip = wlan_ip()
#         PORT = 5555

#         st.info(f"Client IP : {Serverip}", icon="ℹ️")
#         st.info(f"Port No: {PORT}", icon="ℹ️")
#         st.info(f"Number of Server: {1}", icon="ℹ️")
#         st.info(f"Number of Loops: {loop}", icon="ℹ️")
      
         
# with st.container():
#     col1,col2,col3 = st.columns(3)
#     if col2.button('Start Client',disabled=False if val2 == True else True):
#         # Your's IP address
#         YOUR_IP = "0.0.0.0"
#         YOUR_PORT = 5555

#         # Server's IP address
#         SERVER_HOST = keyword[0] #"192.168.80.28" 
#         SERVER_PORT = 5555

#         # Model Path
#         MODEL_PATH = ".\model\pretrained_model.pkl"
#         DATABASE_DIR = "database"

#         # Couter
#         COUNTER = 1

#         FILE_DIR = os.listdir(DATABASE_DIR)       

#         for file in FILE_DIR:
#             #step1
#             st.info(f'Loop {COUNTER}')
#             #COUNTER = COUNTER + 1

#             FILE_PATH = os.path.join(DATABASE_DIR, file)
#             print(FILE_PATH)
#             st.success(FILE_PATH)
            
#             #step2
#             with st.spinner(f"Local model creating..."):
#                 MODEL_BYTES, X_train, X_test, y_train, y_test =  model_train(FILE_PATH, COUNTER)
#                 time.sleep(3)
#             st.success(f"Local model training done successfully.", icon="✅")

#             #step3
#             with st.spinner(f"Waiting for share model..."):
#                 model_share(MODEL_BYTES, SERVER_HOST, SERVER_PORT)
#                 time.sleep(3)
#             st.success(f"Model shared successfully.", icon="✅")
            
#             with st.spinner(f"Waiting for New Model..."):
#                 waitingFornewModel(YOUR_IP, YOUR_PORT, MODEL_PATH)
#                 time.sleep(3)
#             st.success(f"New Model Recevied successfully.", icon="✅")

#             with st.spinner(f"Waiting for Model Evolution..."):
#                 modelEvolution(X_train, y_train, X_test, y_test, MODEL_PATH)
#                 time.sleep(3)
#             st.success(f"Model Evolution done successfully.", icon="✅")

#             if COUNTER == loop:
#                 break

#             COUNTER += 1
            
        

        




















# # for i in range(loop):
# #     progress_text = "Operation in progress. Please wait."
# #     my_bar = st.progress(0, text=progress_text)

# #     for percent_complete in range(100):
# #         time.sleep(0.05)
# #         my_bar.progress(percent_complete + 1, text=progress_text)
# #     time.sleep(1)

# #     st.write(f"loop:{i}")
# #     my_bar.empty()



# # import streamlit as st

# # col1, col2, col3 = st.columns(3, gap=("large"))

# # with col1:
# #    st.header("A cat")
# #    st.image("https://static.streamlit.io/examples/cat.jpg")

# # with col2:
# #    st.header("A dog")
# #    st.image("https://static.streamlit.io/examples/dog.jpg")
