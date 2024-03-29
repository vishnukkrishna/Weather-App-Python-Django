from django.shortcuts import render

from bs4 import BeautifulSoup

# Create your views here.


def get_html_content(city):
  import requests
  city = city.replace(' ', '+')
  USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
  LANGUAGE = "en-US,en;q=0.9"
  session = requests.Session()
  session.headers['User-Agent'] = USER_AGENT
  session.headers['Accept-Language'] = LANGUAGE
  session.headers['Content-Language'] = LANGUAGE
  html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
  return html_content


def home(request):
  weather = None
  if 'city' in request.GET:
    # Fetch weather data
    city = request.GET.get('city')
    html_content = get_html_content(city)
    soup = BeautifulSoup(html_content, 'html.parser')
    weather = dict()
    weather['region'] = soup.find('div', attrs={'id': 'wob_loc'}).text
    weather['dayhour'] = soup.find('div', attrs={'id': 'wob_dts'}).text
    weather['status'] = soup.find('span', attrs={'id': 'wob_dc'}).text
    weather['temp'] = soup.find('span', attrs={'id': 'wob_tm'}).text
    print(weather)

  return render(request, 'weather.html', {'weather': weather})