from stock_data import get_stock_data
from llm import ask_llm

stock = get_stock_data("TCS.NS")

prompt = f"""
You are a professional equity research analyst.

Only use the information provided.

Do not make up facts.

If information is unavailable, explicitly state that.

Generate:

1. Business Overview

2. Financial Health Analysis

3. Growth Analysis

4. Risk Analysis

5. Investment Thesis

6. Missing Information Needed Before Investing
"""

response = ask_llm(prompt)

print(response)