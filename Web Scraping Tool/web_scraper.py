from bs4 import BeautifulSoup
import requests
import json

# URL and headers for the request
url = "https://www.theguardian.com/sport/article/2024/aug/18/ufc-305-dricus-du-plessis-israel-adesanya-steve-erceg-kai-kara-france-tai-tuivasa-jairzinho-rozenstruik-perth"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Send the request
try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # Raise an exception for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the response
soup = BeautifulSoup(r.text, "html.parser")

# Extracting the date
date = soup.find(class_="dcr-u0h1qy")
date_text = date.string if date else "No date found"

# Extracting the title
title = soup.find(class_="dcr-u0152o")
title_text = title.string if title else "No title found"

# Extracting the description
description_elements = soup.find_all(class_="dcr-yu4i55")
descriptions = [desc.get_text(strip=True) for desc in description_elements]
description_text = "\n".join(descriptions) if descriptions else "No description found"

# Extracting the first link from the main content
main_content = soup.find(id="maincontent")
link = main_content.find("a") if main_content else None
link_href = link.get("href") if link else "No link found"

# Extracting related topics or categories
related = soup.find(class_="dcr-n9r616")
related_text = related.string if related else "No related topic found"

# Creating a dictionary to store the data
scraped_data = {
    "Date": date_text,
    "Title": title_text,
    "Description": description_text,
    "Link": link_href,
    "Related Topic": related_text
}

# Print the scraped data
print(json.dumps(scraped_data, indent=4))

# Save the data to a JSON file
output_file = "scraped_data.json"
try:
    with open(output_file, "w") as json_file:
        json.dump(scraped_data, json_file, indent=4)
    print(f"Data successfully saved to {output_file}")
except IOError as e:
    print(f"Error saving data to JSON file: {e}")
