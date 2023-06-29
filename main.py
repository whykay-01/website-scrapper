import click
import os
from app import connection, address, email, phone, name, image, social_media_accounts, urls, 


@click.command()
@click.option(
    "--link", prompt="Enter the link to scrap", help="The link of the website to scrap"
)
def scrap_webpage(link):
    connection.check_connection(link)
    connection.url_validity_check(link)
    click.echo("Test success!")


if __name__ == "__main__":
    scrap_webpage()
