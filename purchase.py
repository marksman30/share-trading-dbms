from database import find_users
from database import view_share
import streamlit as st
import pandas as pd
from database import find_company
from database import purchase_share

def buy():
    counter=1
    result=find_users()
    companies=find_company()
    
    
    choice=st.selectbox("select user",tuple([i[0] for i in result]))
    company=st.selectbox("select company",tuple([i[0] for i in companies]))     
    share_info=view_share(company)
    print(share_info)
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Company ID: '+share_info[0][0]+'</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Exchange: '+share_info[0][3]+'</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Name of Company: '+share_info[0][1]+'</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Total shares: '+str(share_info[0][4])+'</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Sector: '+share_info[0][2]+'</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family:Verdana;color:#CCCCCC">Current value: '+str(share_info[0][5])+'</div>', unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    num_input=st.number_input("quantity of shares",min_value=0,step=1)
    st.write('share price:'+str(num_input*share_info[0][5]))
    
    if st.button("buy"):
        if num_input==0:
            st.error("Cannot purchase 0 shares")
        else:
            purchase_share(choice,company,share_info[0][5],num_input,share_info[0][0])
            st.success('share purchased sucessfully')

    

