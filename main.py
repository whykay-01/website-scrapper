import click
import os

# from app import (
#     address,
#     connection,
#     email,
#     image,
#     phone_num,
#     social_media_accounts,
#     urls,
# )
from app.connection import check_connection
from app.connection import url_validity_check


@click.command()
@click.option(
    "--link", prompt="Enter the link to scrap", help="The link of the website to scrap"
)
def scrap_webpage(link):
    if check_connection():
        url_validity_check(link)
    else:
        click.echo("No internet connection! Try again!")
        exit(1)


if __name__ == "__main__":
    scrap_webpage()
