# Import the FastAPI class to create the application and Query to capture URL query parameters.
from fastapi import FastAPI, Query

# Import the httpx library to make asynchronous HTTP requests.
import httpx

# Create an instance of the FastAPI application.
app = FastAPI()

# Define the base URL of the BetterAnime API, where searches will be made.
BASE_URL = "https://betteranime.net/autocompleteajax?term="


# Define the '/search' route that will respond to GET requests.
@app.get("/search")
async def search_anime(query: str = Query(..., min_length=1)):
    """
    Function to search for animes on BetterAnime based on the provided search term.
    The 'query' parameter comes from the URL.
    """
    # Make the asynchronous HTTP request using the httpx client.
    # 'async with' ensures that the client will be closed after making the request.
    async with httpx.AsyncClient() as client:

        # Perform the GET request to BetterAnime, including the search term in the URL.
        response = await client.get(BASE_URL + query)

    # Check if the response status code is not 200 (which indicates success).
    # If not, return an error.
    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    # If the request is successful, return the data in JSON format (usually a list of animes).
    return response.json()

# The FastAPI server will be run with the following command in the terminal (outside the code):
# uvicorn main:app --reload
# URL to see the anime search: http://127.0.0.1:8000/search?query=Chi.:%20Chikyuu%20no%20Undou%20ni%20Tsuite
