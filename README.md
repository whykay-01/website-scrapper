# Website scrapper

This is a simple program that will help you to scrap the webpage and extract all the email addresses from it.

# Quick Start

1. Clone the repo

2. Install the requirements
```
pip install -r requirements.txt
```

3. Run the program
```
python scrapper.py 
```

4. Enter the url of the website you want to scrap

5. Enter the name of the file you want to save the email addresses to (the file will be saved to the results folder by default)

### Note: The program will only scrap the first page of the website
<!-- 
### For the websites that require login, you can use the following command
```
python scrapper.py --username <your_username> --password <your_password>
``` -->

6. The program will create a file with the name you entered and save all the email addresses to it

# As of May 31st, 2023 this project is considered complete. However, I am currently working on the newe ways of scraping the webpages. Stay tuned for the updates! In particular, I am working on the following features:

- [ ] Scraping multiple pages
- [ ] Scraping the entire website
- [ ] Scraping the website that requires login
- [ ] Scraping the website that requires captcha
- [ ] Scraping the website that requires JavaScript
- [ ] Scraping the website that requires scrolling

Finally, I am also working on the easier ways of deploying the program. One way of doing so is the CLI inteface. I am currently in the stage of choosing the right environment for the CLI interface. 

For any contirbutions to the project -- feel free to submit the pull request. I will review it as soon as possible.