from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

span_tag = soup.find_all(name="span", class_="titleline")
article_upvotes = soup.find_all(name="span", class_="score")
articles = {}

try:
    for index in range(0, len(span_tag)):
        articles[span_tag[index].a.getText()] = {
            "link": span_tag[index].a.get("href"),
            "upvotes": int(article_upvotes[index].getText().split()[0])
        }
except IndexError:
    pass

print(articles)