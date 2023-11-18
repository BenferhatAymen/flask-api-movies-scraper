# importing necessary libraries
import requests
from lxml import html

baseUrl = "https://weciimaa.online/"


def setQueue(text):
    return text.replace(" ", "+")


def searchShow(searchQueue):
    searchQueue = setQueue(searchQueue)
    page = requests.get(
        "https://weciimaa.online/search/{}/#webpage".format(searchQueue)
    )
    tree = html.fromstring(page.text)
    showLinks = tree.xpath('//div[@class="Thumb--GridItem"]/a/@href')
    showNames = tree.xpath('//div[@class="Thumb--GridItem"]/a/@title')

    return showNames, showLinks


def getWatchLinks(showLink):
    page = requests.get(showLink)
    tree = html.fromstring(page.text)
    watchLinks = tree.xpath('//ul[@class="WatchServersList"]/ul/li/btn/@data-url')
    serverNames = tree.xpath('//ul[@class="WatchServersList"]/ul/li/btn/strong/text()')

    return watchLinks, serverNames


# print(
#     getWatchLinks(
#         "https://weciimaa.online/watch/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-avengers-endgame-2019-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/"
#     )
# )
