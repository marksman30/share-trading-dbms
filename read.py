import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data
from database import find_users
from database import view_history
from database import share_list
import matplotlib.pyplot as plt
def read():
    result=find_users()
    choice=st.selectbox("select user",tuple([i for i in result[0]]))
    



    if st.button('Find account info'):
        result=view_all_data(choice)
        purchase_history=view_history(choice)
        shares=share_list(choice)
       
        [(user_id,name,acc_id,invested_value,current_value)]=result
        print(invested_value,current_value)
        df1=pd.DataFrame(purchase_history, columns=['PURCHASE ID', 'PURCHASE VALUE', 'QTY', 'DATE PURCHASED', 'COMPANY SYMBOL'])
        df1.index = [i+1 for i in df1.index]
        df2=pd.DataFrame(shares,columns=["COMPANY SYMBOL","SECTOR","EXCHANGE","VALUE/SHARE","QUANTITY"])
        df2.index = [i+1 for i in df2.index]


        tab1, tab2,tab3 = st.tabs(["Portfolio", "Summary","Purchase history"])
        with tab1:
            # st.dataframe(df)
            st.markdown('<h4 class="big-font" style="font-family:Verdana;color:#CCCCCC">Name: '+name+'</h4>', unsafe_allow_html=True)
            st.markdown('<h4 class="big-font" style="font-family:Verdana;color:#CCCCCC">Account Id: '+acc_id+'</h4>', unsafe_allow_html=True)
            st.markdown('<br><br>', unsafe_allow_html=True)
            st.write("List of purchased shares:")
            st.dataframe(df2)

        with tab2:
            col1, col2= st.columns(2)
            col1.metric("Invested Value", "₹"+str(invested_value))
            col2.metric("Current Value", "₹"+str(current_value), "₹"+str(current_value-invested_value))
        with tab3:
            
            st.dataframe(df1)

        



        
    