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

with col2:
    uppercase = st.button('Uppercase Element')
    def toUpperCase(items):
        elements = [item.upper() for item in items]
        st.write(elements)

    if uppercase:
        toUpperCase(listItem)

with col3:
    lengthOfList = st.button('Length Of List')
    def lengthList(items):
        st.write(len(items))
    
    if lengthOfList:
        lengthList(listItem)