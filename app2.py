import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

col1.title('Calculator')
col2.image('https://help.apple.com/assets/630670789D0ECE568E327B6C/6306707F9D0ECE568E327BA0/en_US/91433b868ad67ee9e2a087cca75de95c.png', width=100)

st.header('App Description')
st.markdown (''' ### This is a demo app for Streamlit
* This is a demo app for Streamlit
* This is a demo app for Streamlit
* This is a demo app for Streamlit
* This is a demo app for Streamlit
''')


num1 = st.number_input('Pick a number', 0, 100)
num2 = st.number_input('Pick another number', 0, 100)

col1, col2, col3 = st.columns(3)
df = pd.DataFrame({'Number1':[num1], 'Number2':[num2]})
col2.write(df)
summ = num1 + num2
subt = num1 - num2

if st.button('Calculate'):
    st.write('Sum = ', summ)
    st.write('Sub= ', subt)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.metric('Sales', 2500 , -10)

