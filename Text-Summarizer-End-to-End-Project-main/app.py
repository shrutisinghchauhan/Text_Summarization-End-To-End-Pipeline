from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response, HTMLResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

text: str = "What is Text Summarization?"

app = FastAPI()


@app.get("/", tags=["frontend"], response_class=HTMLResponse)
async def index():
    # serve the summarizer page; read as a plain file so JS/CSS braces
    # are not treated as Jinja template syntax
    with open("templates/index.html", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
