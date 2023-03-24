from bs4 import BeautifulSoup
import requests

# url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
# keyword = input("검색 단언 입력 : ")
#
# serach_url = f"{url}{keyword}"
#
# response = requests.get(serach_url)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# item = soup.select(".news_tit")
#
# for idx , i in enumerate(item, 1):
#     print(f"{idx} : {i.text}")


url = "https://news.ycombinator.com/newest"
response = requests.get(url)
web_page_text = response.text
soup = BeautifulSoup(web_page_text, "html.parser")

article_texts = []
article_links = []
articles = soup.find_all("span", {"class": "titleline"})
for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.find("a").get("href")
    article_texts.append(text)
    article_links.append(link)
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", {"class" : "score"})]



# print(article_texts)
# print(article_links)
print(article_upvotes)
print(article_texts[article_upvotes.index(max(article_upvotes))])

#
# pick_titleline = soup.select(".titleline")
#
# pick_titeline2 = soup.find_all("tr", {"class" : "athing"})
# pick_titeline3 = soup.select_one(".athing")
# print(pick_titeline3)
# pick_subtext = soup.find_all("span", {"class" : "score"})
#
# # print(pick_titeline2)
# for item in pick_titeline2:
#     pick_score = soup.find("span",{"id": f"score_{item['id']}"})
#     if pick_score != None:
#         pass
#         # print(item)
#         # print("_____")
#         # print(f"{item.text} : {pick_score.text}")
#     else:
#         # print("noew")
#         pass
#     # print(item.text)
#
