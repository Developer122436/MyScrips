from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

# Challenge
article_link = soup.find_all(class_="titleline")
article_score = soup.find_all(class_="subline")

max_score = 0
max_index = 0

for i, (link_tag, score_tag) in enumerate(zip(article_link, article_score)):
    title = link_tag.find(name="a").text
    link = link_tag.find(name="a").get("href")
    score = int(score_tag.find(name="span").text.split()[0])
    print(title)
    print(link)
    print(score)
    print()

    if score > max_score:
        max_score = score
        max_index = i

link_tag = article_link[max_index]
print("Highest upvoted article:")
print(link_tag.find(name="a").text)
print(link_tag.find(name="a").get("href"))

