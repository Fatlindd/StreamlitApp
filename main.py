import streamlit as st

st.title('My First App on Streamlit')
inputString = st.text_input('Your input below: ')
listItem = inputString.split()

col1, col2, col3 = st.columns(3)
with col1:
    convertToList = st.button('Convert To List')
    def createList(listItem):
        elements = listItem[:]
        st.write(elements)

    if convertToList:
        createList(listItem)