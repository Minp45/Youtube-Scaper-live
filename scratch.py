import requests  # requests is a library to import
from bs4 import BeautifulSoup

# first download the page
YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

print('Hello World')

# does not run javascripe
response = requests.get(YOUTUBE_TRENDING_URL)

# respons object: if 200 mean success and if 404 mean it fails or not found
print('Status Code', response.status_code)

doc = BeautifulSoup(response.text, 'html.parser')

print("Page Title", doc.title.text)

# find all video div
video_divs = doc.find_all('div', class_='ytd-video-renderer')

# f string allow you to add with in a string
print(f'Found {len(video_divs)} videos')
