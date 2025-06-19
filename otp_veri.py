import random
import streamlit as st  
import smtplib
import smtplib
st.title(" welcome Otp Verification💻")
a=st.text_input("enter your email address")
#b=st.text_input("enter your password ")
but=st.button("generate otp ")
if a:
    if but:
        ot=random.randint(10000,99999)
        with open('otp.txt','w') as f:
            f.write(str(ot))   
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        #kukp jjjd tzod ctdz
        server.login("innocentboy9472@gmail.com","tafx qtji xblg xkid")
        from_address="innocentboy@gmail.com"
        a=str(a)
        subject="otp from shivam Enterprises"
        with open('otp.txt','r') as f:
            t=f.read()
        body=f' please find the one time otp {t}  otp is valid for only 10 min '
        email=f'subject :{subject} \n\n {body}{t}'
        server.sendmail(from_address,a,email)
        server.quit()

op=st.text_input("enter otp")
        #b1=st.button("verify")
v1=st.button('Verify Otp')

if v1:
    with open('otp.txt','r') as f:
        f=f.read()
        f=str(f)
    if f==op:
        st.success("Login Succesfully")
        st.balloons()
    else:
        st.info("your Otp is Wrong")
         
         
        
