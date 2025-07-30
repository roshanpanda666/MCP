from fastapi import APIRouter
from models.model import Thing
from config.database import collection
from schema.schema import list_serial
from regression_model.predict_stream import start_data_monitor
import threading
from regression_model.regression_engine import predict_prices
from config.database import db
from schema.schema2 import list_serial

router = APIRouter()

# ✅ Define your prediction handler here
def on_new_data(data):
    print("🚀 Detected new data in DB:", data)
    # 🔮 Replace this with your actual prediction logic
    # result = predict(data) or any ML model inference
    print("🧠 Run your prediction here...")
    future_predictions = predict_prices()
    print("\n🧾 Returned Predictions List:")
    print(future_predictions)

# 🚨 Global flag to make sure the thread is only started once
monitor_thread_started = False

@router.get("/")
async def get_todo():
    things = list_serial(collection.find())
    return things

@router.post("/")
async def create_todo(todo: dict):
    global monitor_thread_started

    collection.insert_one(todo)

    if not monitor_thread_started:
        threading.Thread(
            target=start_data_monitor, 
            args=(on_new_data,), 
            daemon=True
        ).start()
        monitor_thread_started = True
        print("🧠 Background monitor thread started...")

    return {"msg": "Todo added successfully!"}


@router.get("/predictions")
async def get_predictions():
    predicted_collection = db["predicted-data"]  # 🌌 Collection name from Atlas
    predicted_docs = list_serial(predicted_collection.find())  # 🧼 Clean data
    return predicted_docs