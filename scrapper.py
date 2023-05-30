import requests
from bs4 import BeautifulSoup
import re

def scrape_emails(url):
    """
    Args: URL of the webpage to scrape
    Returns: List of email addresses found
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all email addresses using regular expressions
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, soup.get_text())
    emails = list(dict.fromkeys(emails))

    if len(emails) == 0:
        return None
    else:
        return emails

def main():
    url = input("Enter the URL to scrape: ")
    # check if the url is valid
    if not url.startswith("http"):
        url = "https://" + url
    # check if the url exists
    try:
        req = requests.get(url)
        print(req)
    except:
        print("Invalid URL")
        return
    emails = scrape_emails(url)
    # Saving the emails to a file
    if emails:
        file_name = input("Enter the name of the file to save the results to: ")
        with open(f"results/{file_name}.txt", "w") as f:
            for email in emails:
                f.write(email + "\n")
        print(f"Emails saved to results/{file_name}.txt")
    # if the response is None, print an error message
    else:
        print("No emails found...")

if __name__ == "__main__":
    main()
