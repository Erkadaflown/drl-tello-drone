from fastapi import FastAPI, WebSocket

app = FastAPI(title="miftaah-drone-backend")

@app.get("/")
async def root():
    return {"status": "ok", "service":"backend"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("hello from backend")
    await ws.close()
