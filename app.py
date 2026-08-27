import streamlit as st

from stock_data import get_stock_data
from news_data import get_company_news
from llm import ask_llm


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Finance Agent",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("📈 Finance Agent")

    st.markdown("""
    ### Current Features

    ✅ Stock Analysis

    ✅ News Intelligence

    🚧 Annual Report Analyzer (RAG)

    🚧 Portfolio Intelligence

    🚧 WealthOS
    """)

    st.divider()

    st.markdown("""
    ### Supported Examples

    - TCS.NS
    - INFY.NS
    - RELIANCE.NS
    - HDFCBANK.NS
    """)


# -----------------------------------
# Main Page
# -----------------------------------

st.title("📈 Finance Agent")
st.caption("AI-Powered Stock Research Assistant")

symbol = st.text_input(
    "Enter Stock Symbol",
    value="TCS.NS"
)

# -----------------------------------
# Analyze Button
# -----------------------------------

if st.button("Analyze"):

    try:

        with st.spinner("Fetching stock data..."):

            stock_data = get_stock_data(symbol)

        # ---------------------------
        # Metrics Section
        # ---------------------------

        st.subheader("📊 Key Metrics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Price",
            stock_data.get("price", "N/A")
        )

        col2.metric(
            "PE Ratio",
            stock_data.get("pe_ratio", "N/A")
        )

        col3.metric(
            "Sector",
            stock_data.get("sector", "N/A")
        )

        col4.metric(
            "Market Cap",
            stock_data.get("market_cap", "N/A")
        )

        # ---------------------------
        # News
        # ---------------------------

        company_name = stock_data.get("company")

        with st.spinner("Fetching latest news..."):

            if company_name:
                news = get_company_news(company_name)
            else:
                news = []

        # ---------------------------
        # Prompt
        # ---------------------------

        prompt = f"""
You are a professional equity research analyst.

Use ONLY the information provided below.

Do NOT invent facts.

If information is missing, explicitly mention it.

STOCK DATA:
{stock_data}

LATEST NEWS:
{news}

Generate a structured report with:

1. Business Overview

2. Financial Health Analysis

3. Key News Developments

4. Risks

5. Investment Thesis

6. Missing Information Needed Before Investing
"""

        # ---------------------------
        # LLM Analysis
        # ---------------------------

        with st.spinner("Analyzing company..."):

            result = ask_llm(prompt)

        # ---------------------------
        # Tabs
        # ---------------------------

        tab1, tab2, tab3 = st.tabs(
            [
                "📈 Analysis",
                "📰 News",
                "⚙️ Raw Data"
            ]
        )

        # ---------------------------
        # Analysis Tab
        # ---------------------------

        with tab1:

            st.subheader("AI Research Report")

            st.markdown(result)

        # ---------------------------
        # News Tab
        # ---------------------------

        with tab2:

            st.subheader("Latest Headlines")

            if news:

                for item in news:
                    st.markdown(f"- {item}")

            else:

                st.warning("No news available")

        # ---------------------------
        # Raw Data Tab
        # ---------------------------

        with tab3:

            st.subheader("Stock Data")

            st.json(stock_data)

        st.success("Analysis Complete")

    except Exception as e:

        st.error(f"Error: {str(e)}")