import easyocr
import streamlit as st
import pandas as pd
from PIL import Image
from new_source import *
from sql_source import *
import pymysql
database_dit = {}
check_dit = {}

db_Table = "new_t"
database_name = "new_db"
st.title("Hello_Bizcard")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_b():
    st.session_state.clicked = True

with st.sidebar:
    opt = st.selectbox("action", ('Upload', 'Modifiy'))
    
    if opt == "Modifiy":
        st.write ('select colums')
        sql_create_connection(database_name)
        get_colums = sql_get_columns(db_Table)
        
        colum_value = st.selectbox("colums", get_colums, key=1)
        get_value = sql_colums_value(db_Table, colum_value)
        
        value = st.selectbox("vlaue", get_value, key=2)
        id_list = sql_prime_number(db_Table, colum_value, value, "person_id")
        id = st.selectbox("id" ,id_list, key=3)
        
        st.button("get data", on_click=click_b)
            
            
            
        
if opt == "Modifiy":
    detail = sql_get_detail_prime_num(db_Table, id, "person_id")
    di = dict(zip(get_colums, detail))
    
    if st.session_state.clicked:
        check_dit["name"]= st.text_input('Name', di.get("name"))
        check_dit["designation"] = st.text_input('designation', di.get("designation"))
        check_dit["mail"]= st.text_input('Mail', di.get("mail"))
        check_dit["web"] = st.text_input('Web', di.get("web"))
        check_dit["num1"]  = st.text_input('Num1', di.get("num1"))
        check_dit["num2"]  = st.text_input('Num2', di.get("num2"))
        check_dit["area_city"] = st.text_input('area,city', di.get("area_city"))
        check_dit["district"]= st.text_input('district', di.get("district"))
        check_dit["state_pincode"]= st.text_input('State,pincode', di.get("state_pincode"))
        check_dit["company_name"]= st.text_input('company name', di.get("company_name")) 
        
        if st.button("upload"):
            output = dictionary_compare(di, check_dit)
            for key in output:
                sql_modify_table(db_Table, key, output[key], id)
            st.write('complete')
      

if opt == "Upload":
    st.session_state.clicked = False
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Enter any caption here')
        st.write("image working")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        reader = easyocr.Reader(['en'])
        output_1 = reader.readtext(bytes_data, detail = 0)
        dic = (img_all_detail(output_1))


        database_dit["name"]= st.text_input('Name', dic.get("name"))
        database_dit["job"] = st.text_input('designation', dic.get("job"))
        database_dit["mail"]= st.text_input('Mail', dic.get("mail"))
        database_dit["web"] = st.text_input('Web', dic.get("web"))
        database_dit["num1"]  = st.text_input('Num1', dic.get("num1"))
        database_dit["num2"]  = st.text_input('Num2', dic.get("num2"))
        database_dit["address_1"] = st.text_input('area,city', dic.get("address_1"))
        database_dit["address_2"]= st.text_input('district', dic.get("address_2"))
        database_dit["address_3"]= st.text_input('State,pincode', dic.get("address_3"))
        database_dit["address_4"]= st.text_input('company name', dic.get("address_4"))


        if st.button('upload'):
            mydb = sql_create_database(database_name)
            sql_create_connection(database_name)
            sql_create_table(db_Table)
            sql_insert(db_Table , database_dit)    
            st.write('upload success')



    
