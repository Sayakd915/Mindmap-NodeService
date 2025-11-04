# MindMap+ Node Service

A FastAPI-based microservice for managing nodes in the MindMap+ application. This service provides node creation, storage, and similarity search capabilities using machine learning embeddings.

## Features

- **Node Management**: Create and manage nodes with title, description, tags, and reminders
- **Semantic Search**: Find similar nodes using ML-based embeddings and cosine similarity
- **Firestore Integration**: Scalable cloud database storage using Google Cloud Firestore
- **RESTful API**: Clean and well-documented API endpoints
- **Docker Support**: Easy deployment with Docker

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Google Cloud Firestore**: NoSQL database for storing nodes
- **Sentence Transformers**: ML model for generating text embeddings
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

## Prerequisites

- Python 3.10 or higher
- Google Cloud account with Firestore enabled
- Firebase Admin SDK credentials JSON file

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Mindmap-NodeService
```

2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
```bash
# On Windows
env\Scripts\activate

# On Linux/Mac
source env/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add the following variable:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=./firebase_admin.json
   ```

6. Configure Firebase:
   - Place your Firebase Admin SDK credentials file as `firebase_admin.json` in the root directory
   - Ensure Firestore is enabled in your Google Cloud project

## Running the Application

### Local Development

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

The API will be available at `http://localhost:8080`

### Using Docker

1. Build the Docker image:
```bash
docker build -t mindmap-node-service .
```

2. Run the container:
```bash
docker run -p 8080:8080 mindmap-node-service
```

## API Documentation

Once the service is running, you can access:
- **Interactive API Docs**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`

## API Endpoints

### Create a Node

**POST** `/nodes`

Create a new node in the system.

**Request Body:**
```json
{
  "title": "My Node Title",
  "description": "Node description",
  "tags": ["tag1", "tag2"],
  "reminder": "Optional reminder text"
}
```

**Response:**
```json
{
  "id": "node_id",
  "title": "My Node Title",
  "description": "Node description",
  "tags": ["tag1", "tag2"],
  "embedding": [0.123, ...],
  "created_at": "2024-01-01T00:00:00"
}
```

### Find Similar Nodes

**GET** `/nodes/{node_id}/similar`

Find nodes similar to a given node using semantic similarity.

**Query Parameters:**
- `threshold` (float, default: 0.7): Minimum similarity score (0-1)
- `top_k` (int, default: 5): Maximum number of results to return

**Response:**
```json
[
  {
    "id": "similar_node_id",
    "title": "Similar Node Title",
    "similarity": 0.85
  }
]
```

## Project Structure

```
Mindmap-NodeService/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── api.py           # API routes and endpoints
│   ├── db.py            # Firestore database operations
│   ├── models.py        # Pydantic models for data validation
│   ├── ml.py            # ML embeddings and similarity functions
│   └── config.py        # Configuration management
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in repo)
├── firebase_admin.json  # Firebase credentials (not in repo)
└── README.md           # This file
```

## Dependencies

- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `pydantic`: Data validation
- `sentence-transformers`: ML embeddings model
- `google-cloud-firestore`: Firestore database client
- `numpy`: Numerical operations
- `python-dotenv`: Environment variable management

## Environment Variables

- `GOOGLE_APPLICATION_CREDENTIALS`: Path to Firebase Admin SDK credentials JSON file

## License

See LICENSE file for details.