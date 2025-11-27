import logging
import azure.functions as func
import requests
from datetime import datetime
from azure.cosmos import CosmosClient
import os
app = func.FunctionApp()
@app.event_grid_trigger(arg_name="event")
def BlobIndexerFunction(event: func.EventGridEvent):

    logging.info("Event Received from Blob Storage")
    data = event.get_json()
    url = data["url"]
    blob_name = url.split("/")[-1]
    container = url.split("/")[-2]

    logging.info(f"File: {blob_name} | Container: {container}")

    res = requests.get(url)
    content = res.content
    content_type = res.headers.get("Content-Type", "")
    size = len(content)

    title = None
    word_count = None

    if content_type.startswith("text/") or blob_name.endswith(".txt"):
        text = content.decode("utf-8", errors="ignore")
        lines = text.splitlines()
        title = next((l.strip() for l in lines if l.strip()), "Untitled")
        word_count = len(text.split())

    cosmos_endpoint = os.getenv("AccountEndpoint=https://charithacosmo.documents.azure.com:443/;AccountKey=cHqjZTGeOmc9TULESoX9YDscLpD7F4XOpjfSpN4cJrtQL17x8Wl0BqSwA4zlfGmetSt1jzGbfoRUACDbiJDlBw==;")
    cosmos_key = os.getenv("cHqjZTGeOmc9TULESoX9YDscLpD7F4XOpjfSpN4cJrtQL17x8Wl0BqSwA4zlfGmetSt1jzGbfoRUACDbiJDlBw==")
    
    client = CosmosClient(cosmos_endpoint, cosmos_key)
    db = client.get_database_client("DocumentIndexDB")
    col = db.get_container_client("Documents")

    document = {
        "id": blob_name,
        "url": url,
        "container": container,
        "size": size,
        "contentType": content_type,
        "title": title,
        "wordCount": word_count,
        "uploadedOn": datetime.utcnow().isoformat()
    }

    col.upsert_item(document)
    logging.info("Stored metadata in Cosmos DB successfully")

