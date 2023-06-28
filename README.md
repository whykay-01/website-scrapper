# Website scrapper

This is a simple program that will help you to scrap the webpage and extract some routine and repetitve information from it.

It is supposed to help a user to scrap for certain things, such as email addresses, phone numbers, URLs, and etc. through providing a link for the website. 

After that, you could specify where do you want the program to save the results (CSV files, Excel files, TXT files, etc.)

# Quick Start

1. Clone the repo 

```
git clone PUT THE LINK HERE
```

Go to the working directory
```
cd website-scrapper
```

Create the virtual environment for all the dependencies:
```
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

2. Now that we have the VENV installed, let's install the requirements for the project:
```
pip install -r requirements.txt
```

or if you are using pip3:
```
pip3 install -r requirements.txt
```

3. Run the program
<!-- ```
python3 scrapper.py 
``` -->
```
pyscrappy --url <url> --file <file_name>
```

4. Enter the url of the website you want to scrap

5. Enter the name of the file you want to save the email addresses to (the file will be saved to the results folder by default)

### TODO: The program will have to scrap the entire website if the tick --all is provided
### TODO: Scraper works with the website that requires login
### TODO: Scraping the website that requires captcha
<!-- 
### For the websites that require login, you can use the following command
```
python scrapper.py --username <your_username> --password <your_password>
``` -->

6. The program will create a file with the name you entered and save all the email addresses to it

# I am also working on the easier ways of deploying the program. One way of doing so is the CLI inteface.

For any contirbutions to the project -- feel free to submit the pull request. I will review it as soon as possible and merge it to the master branch if relevant.