import streamlit as st
import os
import time
st.set_page_config(page_title="LabelOCR", layout="wide", page_icon = "./halologo.png")
hide_menu_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html= True)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        margin-left: -400px;
    }
     
    """,
    unsafe_allow_html=True,
)
# @st.cache
if "check" not in st.session_state:
    st.session_state.check = 1
list_image = os.listdir("./ocr_text")
# check = 0
user, count = st.columns(2)
# user_name = user.text_input("User name")
# if user_name == "tlinh":
col1, col2 = st.columns(2)
def change():
    try:
        if st.session_state.tlinh.replace(" ", "") != "":
            with open("./annotation.txt", "a") as f:
                f.write("image/" +  list_image[start] + "\t" + st.session_state.tlinh + "\n")
            st.session_state.tlinh = ""
            with open("./flag.txt", "w") as f:
                f.write(str(start + 1))
        else:
            st.session_state.tlinh == 1
            st.session_state.tlinh = ""
            with open("./flag.txt", "w") as f:
                f.write(str(start + 1))
    except:
        pass
    # check = 1

with open("./flag.txt", "r") as f:
    start = int(f.readline())
count.write(str(start) +  "/" + str(len(list_image)))
if st.session_state.check == 1:
    name = list_image[start]
    st.session_state.check = 0 
    print(name)  
else:
    print("AHHAHAH")
    name = list_image[start + 1]
    print(name)
col1.image(os.path.join("./ocr_text",name), use_column_width = "always")


text = col2.text_input(label = "Text input", on_change = change(), key = "tlinh")
# elif user_name == "xlinh":
#     col1, col2 = st.columns(2)
#     def change():
#         try:
#             if st.session_state.xlinh.replace(" ", "") != "":
#                 with open("./x_annotation.txt", "a") as f:
#                     f.write("image/" +  list_image[start] + "\t" + st.session_state.xlinh + "\n")
#                 st.session_state.xlinh = ""
#                 with open("./xlinh_flag.txt", "w") as f:
#                     f.write(str(start + 1))
#             else:
#                 st.session_state.xlinh == 1
#                 st.session_state.xlinh = ""
#                 with open("./xlinh_flag.txt", "w") as f:
#                     f.write(str(start + 1))
#         except:
#             pass
#         # check = 1

#     with open("./xlinh_flag.txt", "r") as f:
#         start = int(f.readline())
#     count.write(str(start) + "/" + str(len(list_image)))
#     if st.session_state.check == 1:
#         name = list_image[start]
#         st.session_state.check = 0 
#         print(name)  
#     else:
#         print("AHHAHAH")
#         name = list_image[start + 1]
#         print(name)
#     col1.image(os.path.join("./ocr_text",name), use_column_width = "always")

   
#     text = col2.text_input(label = "Text input", on_change = change(), key = "xlinh")