from database import find_users
from database import view_shares
import streamlit as st
import pandas as pd

def buy():
    result=find_users()
    choice=st.selectbox("select user",tuple([i for i in result[0]]))
    if st.button('Proceed'):
        result=view_shares()
        print(len(result))
        df1=pd.DataFrame(result, columns=['COMPANY ID', 'COMPANY NAME', 'SECTOR', 'EXCHANGE', 'TOTAL SHARES','CURRENT VALUE'])
        
        df1.index = [i+1 for i in df1.index]
        st.dataframe(df1)
