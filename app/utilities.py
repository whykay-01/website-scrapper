def set_api_key(
    apikey: str = "<SCRAPER_API_KEY>",
):
    """
    Creates a .env file with the API key
    """
    with open(".env", "w") as f:
        f.write(f"SCRAPER_API_KEY={apikey}")
