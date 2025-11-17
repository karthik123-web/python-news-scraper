.

📰 News Headlines Web Scraper

A simple Python script that scrapes the latest news headlines from a public website using requests and BeautifulSoup.
The scraped headlines are saved into a text file for offline viewing.

🚀 Features

Fetches live HTML content from a news website

Extracts all headlines (using HTML <h2> tags)

Saves all headlines into a headlines.txt file

Shows how many headlines were collected



🛠️ Technologies Used

Python 3

requests (for downloading webpage)

BeautifulSoup (bs4) (for parsing HTML)

📦 How to Run the Project
1️⃣ Install dependencies
pip install requests
pip install beautifulsoup4

2️⃣ Run the script
python scraper.py

3️⃣ Check output

After running the script, you will find a file named:

headlines.txt


This file contains all scraped headlines, one per line.

📄 Example Output (headlines.txt)
Breaking News: Global Markets Rise
Tech Giants Release New AI Models
Sports Update: Team Wins Championship
...


🎯 This task teaches:

HTTP requests

HTML parsing

Web scraping

File handling

Automation using Python


