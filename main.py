import streamlit as st
import string 
import random

low = list(string.ascii_lowercase)
upp = list(string.ascii_uppercase)
dig = list(string.digits)
let = list(string.ascii_letters)

st.title("password generator")

txt = st.text_input("enter number of password upper of 6 numbers")
but = st.button("generate")
if but:    
    if int(txt)<6:
        st.warning("your password are low")
    if int(txt)>=6:
        st.success("success")
        
    random.shuffle(dig)
    random.shuffle(let)
    password = []
    part1 = round(float(txt) * (70/100))
    part2 = round(float(txt) * (30/100))

    for i in range(part1):
        password.append(let[i])
    for j in range(part2):
        password.append(dig[j])

    code = "".join(password)
    st.write(f"password is {code}")
