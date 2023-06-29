import requests


def check_connection():
    """
    checks if the user is connected to the internet
    Args: None
    Returns: True if connected, False otherwise
    """
    try:
        # it's not really important which website we use as long it is a stable link
        requests.get("https://google.com")
        return True
    except:
        return False


def url_validity_check(url):
    """
    checks the validity of the connection
    Args: URL of the webpage to scrape
    Returns: URL if valid, None otherwise
    """
    # TODO: add more checks

    # validity
    if not url.startswith("http"):
        url = "https://" + url

    # existense
    try:
        req = requests.get(url)
        print("Scrapping...")
    except:
        print("Invalid URL")
        return None

    return url
