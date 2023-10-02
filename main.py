from fastapi import FastAPI
import yfinance as yf

#df = pd.read_csv('company_names.csv')
#df['company_name'] = df['company_name'].str.lower()
app = FastAPI()

@app.get("/stockprice/{company_name}")
async def root(company_name : str):
    ticker = yf.Ticker(company_name).info
    market_price = ticker['currentPrice']
    company_name = ticker['longName']
    #previous_close_price = ticker['regularMarketPreviousClose']
    return {"Stock price of "+company_name+" is": market_price}

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)