import requests

url = "https://manga-kakalot.p.rapidapi.com/chapter"

querystring = {"url": "https://readmanganato.com/manga-aa951409/chapter-1045"}

headers = {
    "X-RapidAPI-Host": "manga-kakalot.p.rapidapi.com",
    "X-RapidAPI-Key": "41f7cfb0efmsha3ad411c601544dp17b9afjsn3d15d9bbe2c1"
}

response = requests.request("GET", url, headers=headers, params=querystring)
res = response.json()
img = res[0]["img_url"]
