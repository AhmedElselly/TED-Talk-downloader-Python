import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit('Error: Please enter the TED Talk URL')

# url = 'https://www.ted.com/talks/liam_young_planet_city_a_sci_fi_vision_of_an_astonishing_regenerative_future'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

for val in soup.find_all('script'):
    if(re.search('talkPage.init', str(val))) is not None:
        result = str(val)

result_mp4 = re.search('(?P<url>https?://[^\s]+)(mp4)', result).group('url')

mp4_url = result_mp4.split('"')[4]
print(mp4_url)

print('Downloading video from ...' + mp4_url)

file_name = mp4_url.split('/')[len(mp4_url.split('/')) - 1].split('?')[0]

print('Storing video in ...' + file_name)

res = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(res.content)

print('Download process finished!')