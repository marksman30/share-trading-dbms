from database import find_users
from database import view_share
import streamlit as st
import pandas as pd
from database import find_company
from database import purchase_share
from database import find_share_name_user
from database import share_quantity
from database import sell_shares

def sell():
    
    user=find_users()
    choice_1=st.selectbox("select user",tuple([i[0] for i in user])) #choice_1=users
    companies=find_share_name_user(choice_1)
    if len(companies)==0:
        st.error("The user has not purchased any shares")
    else:
        choice_2=st.selectbox("select shares",tuple([i[0] for i in companies]))
        share_info=view_share(choice_2)
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
        qty=share_quantity(choice_1,share_info[0][0])
        num_input=st.number_input("quantity of shares",min_value=0,max_value=qty,step=1)
        st.write('share price:'+str(num_input*share_info[0][5]))

        switch=False
        if num_input==0:
            switch=True
        if st.button("Sell",disabled=switch):
            sell_shares(choice_1,share_info[0][0],num_input,share_info[0][5])
        
        

    
    
