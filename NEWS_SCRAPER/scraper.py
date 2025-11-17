import requests
from bs4 import BeautifulSoup
# user-agent 
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
url = "https://news.ycombinator.com"

try:
    response =  requests.get(url, headers = headers, timeout = 10)
    response.raise_for_status() # Raise error if status is not 200
    print("Website loaded sucessfully!")
except requests.exceptions.RequestException as e:
    print("Error while fetching webpage:", e)
    exit()
    print("Failed to load website:",response.status_code)

# Parse the HTML
soup = BeautifulSoup(response.text,"html.parser")

# Extract headlines
headlines = soup.select("span.titleline a")
if not headlines:
    print("No headlines found! Website structure may have changed")
else:
    print(f"Found {len(headlines)} headlines!")

# save the headlines to a file
try:
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            file.write(h.get_text(strip =True) + "\n")
    print("Headlines saved to headlines.txt")
except Exception  as e:
    print("Error  writing to file:", e)