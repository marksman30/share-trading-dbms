# pip install mysql-connector-python
import streamlit as st
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(**st.secrets["mysql"])
c = mydb.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
#               'dealer_street TEXT)')


def add_data(usr_id,name,phone_no,DOB,password,Aadhar_number,gender,pan_number,acc_id,bank_balance):
    try:
        
        c.execute("insert into user values (%s, %s, %s,%s,%s,%s,%s,%s)",(usr_id,name,phone_no,DOB,password,Aadhar_number,gender,pan_number))
        c.execute("insert into  account_summary values(%s,%s,%s,%s)",(acc_id,0,bank_balance,usr_id))
        mydb.commit()    
        st.success("Successfully added user")
    except:
        mydb.rollback()
        st.error("There was a error entering the data in database",icon="🚨")

    
    
    


def view_all_data(usr_id):
    c.execute('select a.*,b.current_value from (select acc.usr_id,u.name,acc.acc_id,acc.invested_value from user u,account_summary acc where u.usr_id=acc.usr_id) a,(select usr_id,sum(current_value*qty) as current_value from (select h.*,c.current_value from purchase_history h,company c where h.company_id=c.company_id) as cv group by cv.usr_id) b where a.usr_id=b.usr_id and a.usr_id="'+usr_id+'"')
    data = c.fetchall()
    return data

def find_users():
    c.execute('select usr_id from user')
    data=c.fetchall()
    return data

def view_history(usr_id):
    c.execute('select h.purchase_id,h.purchase_value,h.qty,h.date_purchased,c.company_name from purchase_history h,company c where h.company_id=c.company_id and usr_id="'+usr_id+'"')
    data=c.fetchall()
    return data

def share_list(usr_id):
    # c.execute("select c.company_name,c.sector,c.exchange,c.current_value,a.net_qty from (select company_id,sum(qty) as net_qty  from purchase_history where usr_id='{}' group by usr_id,company_id) a,company c where a.company_id=c.company_id".format(usr_id))
    c.execute("select c.company_name,c.sector,c.exchange,c.current_value,s.qty from shares s,company c where s.company_id=c.company_id and s.usr_id='{}'".format(usr_id))
    data=c.fetchall()
    # print(data)
    return data

def find_company():
    c.execute("select company_name from company")
    data=c.fetchall()
    return data

def view_share(company_name):
    print(company_name)
    c.execute("select * from company where company_name=%(c_name)s",{'c_name':company_name})
    data=c.fetchall()
    return data

def purchase_share(uid,company_name,current_value,qty,cid):
    c.execute("select count(*) from purchase_history where usr_id=%(usr_id)s",{'usr_id':uid})
    data=c.fetchall()
    counter=data[0][0]
    print(str(uid)+'_p'+str(counter+1))
    c.execute("insert into purchase_history values (%s,%s,%s,%s,%s,%s)",(str(uid)+'_p'+str(counter+1),current_value,qty,date.today(),cid,uid))
    cost=qty*current_value
    c.execute("update account_summary set invested_value=invested_value+%(cr)s where usr_id=%(usid)s",{'cr':cost,'usid':uid})
    c.execute("update account_summary set bank_bal=bank_bal-%(cr)s where usr_id=%(usid)s",{'cr':cost,'usid':uid})
    c.execute("select qty from shares where usr_id=%(usid)s and company_id=%(cmid)s",{'usid':uid,'cmid':cid})
    data=c.fetchall()
    print(data)
    if len(data)==0:
        c.execute("insert into shares values(%s,%s,%s)",(uid,cid,qty))
    else:
        count=data[0][0]
        c.execute("update shares set qty=%(qty)s where company_id=%(cid)s and usr_id=%(uid)s",{'uid':uid,'cid':cid,'qty':(count+qty)})
    mydb.commit()



def find_share_name_user(usr_id):
    print(usr_id)
    c.execute('select c.company_name from shares s,company c where s.company_id=c.company_id and s.usr_id=%(uid)s',{'uid':usr_id})
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