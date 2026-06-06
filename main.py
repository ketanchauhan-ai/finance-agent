from stock_data import get_stock_data
from news_data import get_company_news
from llm import ask_llm

stock_data = get_stock_data("TCS.NS")

news = get_company_news("TCS")

prompt = f"""
You are a professional equity research analyst.

Use ONLY the information below.

STOCK DATA:
{stock_data}

LATEST NEWS:
{news}

Generate:

1. Business Overview

2. Financial Analysis

3. News Impact Analysis

4. Risks

5. Investment Thesis

6. Missing Information Required
"""

response = ask_llm(prompt)

print(response)