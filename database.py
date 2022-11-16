# pip install mysql-connector-python
import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(**st.secrets["mysql"])
c = mydb.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
#               'dealer_street TEXT)')


def add_data(usr_id,name,phone_no,DOB,password,Aadhar_number,gender,pan_number,acc_id,bank_balance):
    c.execute('INSERT INTO User VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (usr_id,name,phone_no,DOB,password,Aadhar_number,gender,pan_number))
    c.execute('insert into account_summary values (%s,'+str(bank_balance)+')',(acc_id))
    mydb.commit()


def view_all_data(usr_id):
    c.execute('select a.*,b.current_value from (select acc.usr_id,u.name,acc.acc_id,acc.invested_value from user u,account_summary acc where u.usr_id=acc.usr_id) a,(select usr_id,sum(current_value*qty) as current_value from (select h.*,c.current_value from holdings h,company c where h.company_id=c.company_id) as cv group by cv.usr_id) b where a.usr_id=b.usr_id and a.usr_id="'+usr_id+'"')
    data = c.fetchall()
    return data

def find_users():
    c.execute('select usr_id from user')
    data=c.fetchall()
    return data

def view_history(usr_id):
    c.execute('select h.purchase_id,h.purchase_value,h.qty,h.date_purchased,c.company_name from holdings h,company c where h.company_id=c.company_id and usr_id="'+usr_id+'"')
    data=c.fetchall()
    return data

def share_list(usr_id):
    c.execute("select c.company_name,c.sector,c.exchange,c.current_value,a.net_qty from (select company_id,sum(qty) as net_qty  from holdings where usr_id='{}' group by usr_id) a,company c where a.company_id=c.company_id".format(usr_id))
    data=c.fetchall()
    # print(data)
    return data

def view_shares():
    c.execute("select * from holdings")
    data=c.fetchall()
    return data

# def view_only_dealer_names():
#     c.execute('SELECT dealer_name FROM DEALER')
#     data = c.fetchall()
#     return data


# def get_dealer(dealer_name):
#     c.execute('SELECT * FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
#     data = c.fetchall()
#     return data


# def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
#     c.execute("UPDATE DEALER SET dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s WHERE "
#               "dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s", (new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
#     mydb.commit()
#     data = c.fetchall()
#     return data


# def delete_data(dealer_name):
#     c.execute('DELETE FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
#     mydb.commit()