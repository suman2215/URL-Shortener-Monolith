# URL Shortener

## Project Overview

This is a simple URL Shortener application built using Flask and Flask-RESTful in Python. The application allows users to shorten URLs and store them in a MongoDB database. The shortened URLs can be used to redirect to the original URLs. The application also uses Memcached for caching, improving performance by reducing the load on the database.

### Features

- **URL Shortening:** Converts long URLs into short, manageable links.
- **Redirection:** Redirects the shortened URLs to their original destinations.
- **Caching:** Utilizes Memcached to cache the shortened URLs, reducing the need for frequent database queries.
- **Error Handling:** Graceful error handling and logging for unexpected issues.
- **CORS Support:** Cross-Origin Resource Sharing is enabled to allow requests from different origins.

## Installation

### Prerequisites

- Python 3.x
- MongoDB
- Memcached

### Clone the Repository

```bash
git clone https://github.com/suman2215/URL-Shortener-Monolith.git
cd URL-Shortener-Monolith
```

### Set Up Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configuration

The configuration settings for MongoDB and Memcached are located in the `config.py` file.

```python
class Config:
    MONGO_URI = "mongodb://localhost:27017/urlshortener"
    MEMCACHED_SERVER = ['127.0.0.1:11211']
    BASE_URL = "http://localhost:5000/"
```

Make sure your MongoDB and Memcached services are running and accessible at the specified URIs.

## Running the Application

Before starting the server, the application will check if MongoDB and Memcached are properly connected. If the connections fail, the server will not start.

Start the server using:

```bash
python3 app.py
```

The server will run on `http://localhost:5000` by default.

## API Endpoints

### 1. Shorten URL

**Endpoint:** `/shorten`  
**Method:** `POST`  
**Description:** Shortens a given URL.

**Request Body:**

```json
{
  "url": "http://example.com"
}
```

**Response:**

```json
{
  "shortened_url": "http://localhost:5000/abc123"
}
```

### 2. Redirect to Original URL

**Endpoint:** `/<short_id>`  
**Method:** `GET`  
**Description:** Redirects to the original URL corresponding to the given short ID.

**Example:**

```bash
http://localhost:5000/abc123
```

This will redirect the user to the original URL stored in the database.

## Testing the Application

### Shorten a URL

To test the URL shortening functionality, use a tool like `curl` or Postman to send a POST request:

```bash
curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url": "http://example.com"}'
```

You should receive a response with a shortened URL.

### Redirect Using Shortened URL

After shortening a URL, you can test the redirection by navigating to the shortened URL in your browser:

```bash
http://localhost:5000/abc123
```

This should redirect you to the original URL.

### Error Handling

You can test error handling by:

- Disconnecting MongoDB or Memcached and attempting to start the server.
- Sending invalid requests (e.g., missing URL field in the POST request).

The server should handle these gracefully and provide appropriate error messages.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
