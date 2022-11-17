# import mysql.connector
# import streamlit as st
# cnx = mysql.connector.connect(**st.secrets["mysql"])
# print(cnx)
# cursor = cnx.cursor()
# query = ("select * from holdings")
# cursor.execute(query)
# for item in cursor:
#     print(item)
# cursor.close()
# cnx.close()

import streamlit as st
import mysql.connector

from create import create
# from delete import delete
# from database import create_table
# from delete import delete
from read import read
from purchase import buy
from sell import sell 
# from update import update

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()
#
# c.execute("CREATE DATABASE ebike")


def main():
    st.title("Share trading app")
    menu = ["Add", "View", "Buy", "Sell"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # create_table()
    if choice == "Add":
        
        st.subheader("Enter Dealer Details:")
        create()

    elif choice == "View":
        
        st.subheader("View User infos")
        read()

    elif choice == "Buy":
        
        st.subheader("Purchase share")
        buy()
        

    elif choice == "Sell":
        st.subheader("Sell Share")
        sell()

    # else:
    #     st.subheader("About tasks")


if __name__ == '__main__':
    main()