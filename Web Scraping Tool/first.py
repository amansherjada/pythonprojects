import requests

def fetchsave(url, path):
    r =requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/mumbai"

fetchsave(url, "files/times.html")