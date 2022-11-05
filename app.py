from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    url = 'https://economictimes.indiatimes.com/topic/data-science'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page{}'.formaT(url))
    page_contents = response.text
    doc = BeautifulSoup(page_contents, 'html.parser')

    title_tags = doc.find_all('h2')
    title = []
    for tag in title_tags[0:5]:
        title.append(tag.text)

    time_tags = doc.find_all('time')
    time = []
    for tag in time_tags[0:5]:
        time.append(tag.text)

    news_0 = "1. "+title[0] + " - " + time[0]
    news_1 = "2. "+title[1] + " - " + time[1]
    news_2 = "3. "+title[2] + " - " + time[2]
    news_3 = "4. "+title[3] + " - " + time[3]
    news_4 = "5. "+title[4] + " - " + time[4]

    get_news = "\n" + news_0 + "\n" + news_1 + "\n" + news_2 + \
        "\n" + news_3 + "\n" + news_4

    return render_template("index.html", News=get_news)
