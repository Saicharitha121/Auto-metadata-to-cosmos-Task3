# Auto-metadata-to-cosmos-Task3


This project automatically indexes metadata and text details from blobs uploaded into the documents container. When a new blob is created, Event Grid triggers a Function App, which extracts metadata + content and stores an indexed record in Cosmos DB.

1. Prerequisites
Azure Resources Required

-Storage Account

Must have a documents container.

Event Grid must be enabled for blob-created events.

- Azure Function App

Language: Python 

Must support Event Grid trigger.

- Cosmos DB (Core SQL API)

Database: DocumentsDB

Container: Documents (Partition key: /id)

Unique key: /id (to prevent duplicates)

2. Local Development Requirements

- Visual Studio Code / Visual Studio

- Azure Functions Core Tools

- Python Libaries: azure-functions , azure-storage-blob , azure-cosmos

3. Event Flow Overview

- A new blob is uploaded to documents container.

- Storage Account sends BlobCreated event to Event Grid.

- Event Grid triggers Azure Function.

Function extracts:
blobName
container
URL
contentType
size
title (first H1 or first line)
wordCount (for text files)

- Inserts/upserts document into Cosmos DB with the given data


4. Expected Output

Cosmos DB contains a record for every uploaded blob.

Re-uploading the same file updates the existing document.

Function logs show successful indexing.
