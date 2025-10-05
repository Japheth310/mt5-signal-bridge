from fastapi import FastAPI, HTTPException
import MetaTrader5 as mt5
from pydantic import BaseModel

app = FastAPI(title="MT5 Signal Bridge", version="1.0.0")

# --- MT5 Connection ---
if not mt5.initialize():
    raise HTTPException(status_code=500, detail="Failed to connect to MT5")

# --- Define request body ---
class SignalRequest(BaseModel):
    symbol: str
    timeframe: str
    strategy: str = "full_analysis"

@app.post("/signal")
def generate_signal(req: SignalRequest):
    symbol = req.symbol.upper()
    timeframe = req.timeframe.upper()

    # Check suffix automatically
    symbols = [s.name for s in mt5.symbols_get()]
    suffix = ""
    for s in symbols:
        if s.startswith(symbol):
            suffix = s.replace(symbol, "")
            break

    symbol_full = symbol + suffix

    # --- Placeholder logic for signal generation ---
    # (You’ll expand later with real analysis)
    result = {
        "symbol": symbol_full,
        "timeframe": timeframe,
        "analysis": "Candle broke above resistance. Trend bullish.",
        "entry": "Buy above 1.0850",
        "stop_loss": "1.0830",
        "tp1": "1.0880",
        "tp2": "1.0900",
        "tp3": "1.0950",
    }
    return result
