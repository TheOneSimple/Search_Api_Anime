# BetterAnime Search API

This API is designed to perform web scraping to search for anime directly from the BetterAnime website.

## Overview

The BetterAnime Search API allows users to search for anime titles by querying the BetterAnime website. It uses FastAPI to handle HTTP requests and httpx for asynchronous HTTP requests.

## Features

- **Search Anime**: Perform a search for anime titles based on a query term.
- **Asynchronous Requests**: Utilizes asynchronous HTTP requests for efficient data retrieval.

## Endpoints

### GET /search

Search for anime titles based on a query term.

**Parameters:**
- `query` (str): The search term for the anime. Must be at least 1 character long.

**Example Request:**
```
GET /search?query=Naruto
```

**Example Response:**
```json
[
    {
        "title": "Naruto",
        "url": "https://betteranime.net/anime/naruto"
    },
    {
        "title": "Naruto Shippuden",
        "url": "https://betteranime.net/anime/naruto-shippuden"
    }
]
```

## Setup

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install fastapi httpx uvicorn
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

To search for an anime, navigate to the following URL in your browser or use a tool like `curl` or Postman:
```
http://127.0.0.1:8000/search?query=YourSearchTerm
```

Replace `YourSearchTerm` with the anime title you want to search for.

## License

This project is licensed under the MIT License.