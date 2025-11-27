
# Auto-Index Blob Metadata into Cosmos DB  
### (Event Grid Trigger + Azure Function + CosmosDB)

This project automatically indexes files uploaded to Azure Blob Storage into Azure Cosmos DB.
Whenever a file is placed inside the `documents` container, Event Grid triggers an Azure Function
which extracts metadata like word count, file size, content type, and title — and stores it in Cosmos DB.

---

## 🚀 Features
- Event Grid Trigger
- Azure Functions (Python 3.11)
- Automatic Blob Metadata Extraction
- Title Extraction (from first non-empty line for text files)
- Word Count for `.txt` files
- Cosmos DB Upsert (Prevents Duplicate Inserts)
- Fully Serverless + Scalable

---

## 📁 Project Structure
```
Auto-Blob-Indexer/
│── function_app.py
│── local.settings.json
│── requirements.txt
│── host.json
│── .venv/
```

---

## 🛠 Setup Instructions

### 1️⃣ Create Virtual Environment
```
py -3.11 -m venv .venv
.\.venv\Scripts\activate
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Configure Local Settings  
Create `local.settings.json`:

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "<your-storage-connection-string>",
    "COSMOS_ENDPOINT": "<your-cosmos-endpoint>",
    "COSMOS_KEY": "<your-primary-key>"
  }
}
```

---

## ▶ Run Function Locally
```
func start
```

Upload any file inside Blob Storage → `documents` container.  
Function should auto-trigger and push data into CosmosDB.

---

## 🧪 Output Sample Stored in Cosmos DB

```json
{
  "id": "notes.txt",
  "url": "https://<storage>.blob.core.windows.net/documents/notes.txt",
  "size": 2542,
  "contentType": "text/plain",
  "title": "My Meeting Notes",
  "wordCount": 243,
  "uploadedOn": "2025-11-26T12:45:10Z"
}
```

---

## ☁ Deploy to Azure

### 1. Deploy using VS Code
Right-click project → Deploy to Function App

### 2. Add App Settings in Azure
| Name | Value |
|------|------------------|
| COSMOS_ENDPOINT | CosmosDB URI |
| COSMOS_KEY | Primary key |
| AzureWebJobsStorage | Storage connection string |

Save → 🔄 Restart Function App

### 3. Create Event Grid Subscription
```
Storage Account → Events ➝ Event Subscription ➝ BlobCreated  
Container Filter: documents  
Endpoint: Azure Function → BlobIndexerFunction
```

Upload a blob again → Metadata should appear in CosmosDB.

---

## ✔ Requirements Checklist
| Task | Status |
|---|---|
| Blob Trigger via Event Grid | ✔ |
| Metadata Extraction | ✔ |
| Title Extraction (H1 / First Line) | ✔ |
| Word Count | ✔ |
| CosmosDB Upsert (No Duplicates) | ✔ |
| Tested Locally + Azure Deployment | ✔ |
| README.md Included | ✔ |

---

## 🎉 Project Completed Successfully!

![alt text](<Screenshot 2025-11-26 174433.png>)

