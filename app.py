import streamlit as st

from stock_data import get_stock_data
from llm import ask_llm

st.title("Finance Agent")

symbol = st.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

if st.button("Analyze"):

    st.write("Button clicked")

    stock_data = get_stock_data(symbol)

    st.write("Stock data fetched")

    st.write(stock_data)

    prompt = f"""
    Analyze this company:

    {stock_data}
    """

    result = ask_llm(prompt)

    st.write("LLM response received")

    st.write(result)