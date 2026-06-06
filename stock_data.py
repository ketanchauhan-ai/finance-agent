import yfinance as yf

def get_stock_data(symbol):

    stock = yf.Ticker(symbol)

    info = stock.info

    return {
        "company": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "roe": info.get("returnOnEquity"),
        "profit_margin": info.get("profitMargins"),
        "revenue_growth": info.get("revenueGrowth"),
        "earnings_growth": info.get("earningsGrowth"),
        "debt_to_equity": info.get("debtToEquity")
    }