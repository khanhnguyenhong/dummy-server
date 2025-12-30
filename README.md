# Dummy Server

A simple FastAPI application for scraping text from URLs.

## Prerequisites

- Python 3.8+
- `pip` (Python package installer)

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd dummy-server
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment**:
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Start the FastAPI server using `uvicorn`:

```bash
./venv/bin/uvicorn main:app --reload --port 8000
```

The server will start at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Manual Testing

You can use `curl` or the Swagger UI to test the endpoints.

### Health Check
```bash
curl http://127.0.0.1:8000/
```
Expected response: `{"status": "Dummy Server is running"}`

### Scrape a URL
```bash
curl -X POST "http://127.0.0.1:8000/scrape" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

### Get Saved Data
```bash
curl http://127.0.0.1:8000/data
```

## Connecting from a Client App

Your API is configured to allow requests from **any origin** (`allow_origins=["*"]`), so you can easily connect from a local React, Angular, or Vue app.

**Base URL**: `http://127.0.0.1:8000`

### Example (JavaScript/Fetch)
```javascript
const response = await fetch('http://127.0.0.1:8000/api/scrape', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ url: 'https://example.com' })
});
const data = await response.json();
console.log(data);
```
