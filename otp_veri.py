import random
import streamlit as st  
import smtplib
import smtplib
otp=random.randint(10000,99999)
st.title(" welcome Otp Verification💻")
a=st.text_input("enter your email address")
#b=st.text_input("enter your password ")
but=st.button("generate otp ")
if a:
    if but:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        #kukp jjjd tzod ctdz
        server.login("innocentboy9472@gmail.com","tafx qtji xblg xkid")
        from_address="innocentboy@gmail.com"
        a=str(a)
        subject="otp from shivam Enterprises"
        body=f' please find the one time otp {otp}  otp is valid for only 10 min '
        email=f'subject :{subject} \n\n {body}{ otp}'
        server.sendmail(from_address,a,email)
        server.quit()

op=st.text_input("enter otp")
        #b1=st.button("verify")
v1=st.button("verify otp")
if v1:
    if op==otp:
        st.write("login succesfully")
    else:
        st.write("your Otp is Wrong")
         
        
