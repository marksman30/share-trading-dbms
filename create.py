import streamlit as st
from database import add_data
def create():
    col1, col2 = st.columns(2)
    with col1:
        usr_id = st.text_input("usr_id:")
        print(usr_id)
        name = st.text_input("name:")
        DOB = st.date_input("Date of birth:")
        print(DOB)
        gender=st.selectbox("Gender:",("M","F"))
        acc_id=st.text_input("Account id:")
    with col2:
        phone_no = st.text_input("phone_no:")
        password = st.text_input("password:")
        Aadhar_number=st.text_input("Aadhar:")
        pan_number=st.text_input("PAN number:")
        bank_balance=st.text_input("Pocket balance:")
    
    
    if st.button("Add Dealer"):
        # pass
        add_data(usr_id,name,phone_no,DOB,password,Aadhar_number,gender,pan_number,acc_id,bank_balance)
        # st.success("Successfully added Dealer: {}".format(dealer_name))