# Finance Agent

An AI-powered financial research assistant built with Python, Ollama, Qwen, and Yahoo Finance.

The application combines market data, financial metrics, and news intelligence with a locally hosted LLM to generate structured research insights for a selected stock.

## Why I Built This

The goal was to explore how an AI agent can combine:

- External financial data
- Structured data processing
- News retrieval
- Local LLM inference
- Deterministic data retrieval
- AI-generated reasoning

into a single research workflow.

## Architecture

```text
User
  |
  v
Application / UI
  |
  v
Finance Agent
  |
  +------------------+
  |                  |
  v                  v
Stock Data        News Data
Yahoo Finance    News Sources
  |                  |
  +--------+---------+
           |
           v
      Data Processing
           |
           v
       Local LLM
     Ollama / Qwen
           |
           v
   Research / Analysis