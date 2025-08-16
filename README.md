# URL Shortener

A simple backend service that shortens URLs using FastAPI and SQLite.

## Features

- Shorten long URLs to compact, shareable links.
- Redirect visitors from short URLs to the original URLs.
- Track the number of times each short URL is accessed.
- Retrieve click statistics for each short URL.

## Technology Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite (via SQLAlchemy ORM)

## API Endpoints

### 1. Create Short URL

- **Endpoint:** `POST /shorten`
- **Request Body:** `{ "url": "<long_url>" }`
- **Response:** `{ "short_url": "<generated_short_url>" }`
- **Description:** Accepts a long URL and returns a shortened URL.

### 2. Redirect to Original URL

- **Endpoint:** `GET /{short_id}`
- **Response:** Redirects the request to the original URL.
- **Description:** When a user accesses a short URL, they are redirected to the original URL, and the click is counted.

### 3. Get Click Statistics

- **Endpoint:** `GET /stats/{short_id}`
- **Response:** 
  ```json
  {
    "short_id": "<short_id>",
    "original_url": "<original_url>",
    "clicks": <number_of_clicks>
  }
  ```
- **Description:** Returns the original URL and the number of times the short URL has been accessed.

### 4. Health Check / Welcome

- **Endpoint:** `GET /`
- **Response:** `{ "message": "Starting URL Shortener" }`
- **Description:** Basic health check or root endpoint.

## Configuration

- SQLite database file is created at `./shortener.db`.
- All URLs and click statistics are stored in the database.

## Deployment Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aigbee17/url-shortner.git
   cd url-shortner
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

3. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.
   - Use an API client like Postman or cURL to interact with the endpoints.

## File Structure

- `app/main.py` - Core FastAPI app and API endpoints.
- `app/database.py` - Database connection and model definitions.
- `shortener.db` - SQLite database (auto-generated).

## License

*No license specified.*

---

For any issues or feature requests, please open an issue at [https://github.com/aigbee17/url-shortner/issues](https://github.com/aigbee17/url-shortner/issues).
